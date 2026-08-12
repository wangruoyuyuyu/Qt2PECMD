#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ui2pecmd.py - Convert Qt Designer .ui files (XML) to PECMD script.

Now supports conversion from a UI XML string directly, with orientation handling.
"""

import xml.etree.ElementTree as ET
from typing import Dict, List, Optional

class UiToPecmdConverter:
    # Mapping from Qt class names to PECMD control commands
    CONTROL_MAP = {
        'QPushButton': 'ITEM',
        'QLabel': 'LABE',
        'QLineEdit': 'EDIT',
        'QTextEdit': 'MEMO',
        'QPlainTextEdit': 'MEMO',
        'QCheckBox': 'CHEK',
        'QRadioButton': 'RADI',
        'QComboBox': 'LIST',
        'QGroupBox': 'GROU',
        'QProgressBar': 'PBAR',
        'QSlider': 'SLID',
        'QTabWidget': 'TABS',
        'QTableWidget': 'TABL',
    }

    SIGNAL_EVENTS = {
        'clicked()': 'MESS 按钮被点击',
        'toggled(bool)': 'MESS 状态改变',
        'textChanged(QString)': 'MESS 文本改变',
        'currentIndexChanged(int)': 'MESS 选项改变',
        'valueChanged(int)': 'MESS 滑块值改变',   # 新增滑块值变化事件
    }

    def __init__(self, indent: str = '    '):
        self.indent = indent
        self.window_name = "Win1"
        self.controls = []

    def convert(self, ui_input: str) -> str:
        """Convert a .ui file path or XML string to PECMD script."""
        if ui_input.strip().startswith('<') or ui_input.strip().startswith('<?xml'):
            return self.convert_string(ui_input)
        else:
            with open(ui_input, 'r', encoding='utf-8') as f:
                xml_content = f.read()
            return self.convert_string(xml_content)

    def convert_string(self, xml_string: str) -> str:
        """Convert UI XML string directly to PECMD script."""
        root = ET.fromstring(xml_string)
        widget = root.find('widget')
        if widget is None:
            raise ValueError("No <widget> element found in UI XML.")

        self.window_name = widget.get('name', 'Win1')
        title_elem = widget.find('property[@name="windowTitle"]/string')
        window_title = title_elem.text if title_elem is not None else 'My Window'

        geom = self._get_geometry(widget)
        x = geom.get('x', 0)
        y = geom.get('y', 0)
        w = geom.get('width', 640)
        h = geom.get('height', 480)

        script_lines = []
        script_lines.append(f'_SUB {self.window_name},L{x}T{y}W{w}H{h},{window_title},,')

        self.controls = []
        self._process_widget(widget, {'x': x, 'y': y, 'width': w, 'height': h})

        for cmd_line, _ in self.controls:
            script_lines.append(f'{self.indent}{cmd_line}')

        script_lines.append('_END')
        script_lines.append(f'CALL @{self.window_name}')
        return '\n'.join(script_lines)

    def _process_widget(self, widget_elem: ET.Element, parent_geom: Dict[str, int]):
        class_name = widget_elem.get('class')
        if class_name in self.CONTROL_MAP:
            cmd = self.CONTROL_MAP[class_name]
            name = widget_elem.get('name', 'ctrl')
            geom = self._get_geometry(widget_elem)
            if not geom:
                geom = self._compute_geometry_from_layout(widget_elem, parent_geom)
            if not geom:
                geom = {'x': 0, 'y': 0, 'width': 100, 'height': 30}

            text = self._get_property(widget_elem, 'text', '')
            event = self._get_event_command(widget_elem)

            cmd_line = self._build_control_command(cmd, name, geom, text, event, widget_elem)
            extra = self._get_extra_attrs(widget_elem, cmd)
            if extra:
                cmd_line += f',{extra}'

            self.controls.append((cmd_line, name))

        for child in widget_elem.findall('widget'):
            self._process_widget(child, parent_geom)

    def _get_geometry(self, widget_elem: ET.Element) -> Dict[str, int]:
        geom_elem = widget_elem.find('property[@name="geometry"]/rect')
        if geom_elem is None:
            return {}
        result = {}
        for key in ['x', 'y', 'width', 'height']:
            val = geom_elem.find(key)
            if val is not None and val.text:
                result[key] = int(val.text)
        return result

    def _compute_geometry_from_layout(self, widget_elem: ET.Element, parent_geom: Dict[str, int]) -> Dict[str, int]:
        # Simplified: fallback to default size
        return {'x': 0, 'y': 0, 'width': 100, 'height': 30}

    def _get_property(self, widget_elem: ET.Element, prop_name: str, default: str = '') -> str:
        prop = widget_elem.find(f'property[@name="{prop_name}"]')
        if prop is None:
            return default
        for tag in ['string', 'bool', 'number']:
            elem = prop.find(tag)
            if elem is not None and elem.text:
                return elem.text
        return default

    def _get_orientation(self, widget_elem: ET.Element) -> str:
        """
        Return orientation as 'Qt::Horizontal' or 'Qt::Vertical'.
        Default is 'Qt::Horizontal' if not set.
        """
        prop = widget_elem.find('property[@name="orientation"]/enum')
        if prop is not None and prop.text:
            text = prop.text
            # Handle both 'Qt::Horizontal' and 'Qt::Orientation::Horizontal'
            if 'Horizontal' in text:
                return 'Qt::Horizontal'
            elif 'Vertical' in text:
                return 'Qt::Vertical'
        return 'Qt::Horizontal'  # default
    def _get_event_command(self, widget_elem: ET.Element) -> str:
        connections = widget_elem.findall('../connections/connection')
        for conn in connections:
            sender = conn.find('sender')
            signal = conn.find('signal')
            if sender is not None and sender.text == widget_elem.get('name'):
                if signal is not None and signal.text in self.SIGNAL_EVENTS:
                    return self.SIGNAL_EVENTS[signal.text]
        return ''

    def _build_control_command(self, cmd: str, name: str, geom: Dict[str, int],
                               text: str, event: str, widget_elem: ET.Element = None) -> str:
        shape = f"L{geom['x']}T{geom['y']}W{geom['width']}H{geom['height']}"
        text = text.replace('"', '\\"')

        if cmd == 'ITEM':
            return f'{cmd} {name},{shape},{text},{event},,'
        elif cmd == 'LABE':
            return f'{cmd} {name},{shape},{text},{event},,'
        elif cmd == 'EDIT':
            return f'{cmd} {name},{shape},{text},{event},,'
        elif cmd == 'MEMO':
            return f'{cmd} {name},{shape},{text},,,'
        elif cmd == 'CHEK':
            return f'{cmd} {name},{shape},{text},{event},'
        elif cmd == 'RADI':
            return f'{cmd} {name},{shape},{text},{event},,1'
        elif cmd == 'LIST':
            items = 'item1|item2|item3'
            return f'{cmd} {name},{shape},{items},{event},,'
        elif cmd == 'GROU':
            return f'{cmd} {name},{shape},{text},,'
        elif cmd == 'PBAR':
            return f'{cmd} {name},{shape},0,'
        elif cmd == 'SLID':
            # Orientation handling: add 0x40 for horizontal
            orient = self._get_orientation(widget_elem) if widget_elem is not None else 'Qt::Horizontal'
            state = '0x40' if orient == 'Qt::Horizontal' else '0'
            # You can also read min/max/value from properties if needed
            return f'{cmd} {name},{shape},0:100:50,{event},{state}'
        elif cmd == 'TABS':
            pages = 'Page1:page1:Tab1:;Page2:page2:Tab2:'
            return f'{cmd} {name},{shape},{pages},'
        elif cmd == 'TABL':
            return f'{cmd} {name},{shape},50:Col1%TAB%50:Col2,data,'
        else:
            return f'// Unsupported control: {cmd} {name}'

    def _get_extra_attrs(self, widget_elem: ET.Element, cmd: str) -> str:
        return ''


def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python ui2pecmd.py <input.ui> [output.pecmd]")
        sys.exit(1)

    input_arg = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    converter = UiToPecmdConverter()
    script = converter.convert(input_arg)
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(script)
        print(f"PECMD script written to {output_file}")
    else:
        print(script)


if __name__ == '__main__':
    main()