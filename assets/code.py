from flet import CupertinoTextField, TextStyle

class OutputCode(CupertinoTextField):
    def __init__(self, num_line = 11, value: str = '', on_click = None):
        super().__init__()
        self.multiline = True
        self.min_lines = num_line
        self.max_lines = num_line
        self.read_only = True
        self.on_click = on_click
        self.data = value
        self.value = value
        self.text_style = TextStyle(font_family='code')

class InputCode(CupertinoTextField):
    def __init__(self):
        super().__init__()
        self.multiline = True
        self.min_lines = 11
        self.max_lines = 11
        self.value = "print('hello world!')"
        self.text_style = TextStyle(font_family='code')