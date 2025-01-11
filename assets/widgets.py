from flet import icons,TextStyle, BoxShadow, Offset, ControlEvent, Page, AlertDialog
from data import variables
from .learn import Title
from .interpreter import interpreter
from flet import Container, Row, Column, AppBar, Text, IconButton
from flet import CupertinoFilledButton, Divider, Page, ControlEvent, CupertinoTextField, TextButton
from .colors import *
from .code import *

class InfoBar(AppBar):
    def __init__(self):
        super().__init__()
        self.center_title = True
        self.title = Text("Preparix", font_family='title', size=50, style=TextStyle(shadow=BoxShadow(2, 1, 'blue', Offset(1, 1))))
        self.actions = [IconButton(icons.SETTINGS, 'white', on_click=self.settings_display)]
    
    def settings_display(self, e: ControlEvent):
        page: Page = e.page
        box = AlertDialog(
            title=Text("A propos", font_family='title1', size=40),
            content=Column(
                controls=[
                    Text("Telegram", font_family='text', size=20),
                    CupertinoTextField(value="https://t.me/xverse3", read_only=True, text_align='center', text_style=TextStyle(font_family='code')),
                ],
                height=50,
                width=400
            ),
            actions=[TextButton("OK", on_click=lambda _: page.close(box))]
        )
        page.open(box)
        page.update()

class Topic(Container):
    def __init__(self):
        super().__init__()
        self.bgcolor = FG2
        self.expand = 1
        self.padding = 10
        self.border_radius = 20
        self.chapitre = Container(variables.Variable())
        self.title = Title("Variables".upper())
        self.content = Column(
            controls=[
                Row([self.title]),
                Divider(),
                self.chapitre
            ]
        )

class Action(CupertinoFilledButton):
    def __init__(self):
        super().__init__()
        self.text = "Interpreter"
        self.expand = True
        self.on_click = self.interprete
        self.icon = icons.TRANSFORM

    def interprete(self, e: ControlEvent):
        page: Page = e.page
        code: str = page.controls[1].controls[1].content.controls[0].value
        output = page.controls[1].controls[1].content.controls[-1]
        output.value = interpreter(code)
        page.update()

class Code(Container):
    def __init__(self):
        super().__init__()
        self.border_radius = 20
        self.padding = 15
        self.expand = True
        self.bgcolor = FG1
        self.content = Column(
            controls=[
                InputCode(),
                Row([Action()]),
                OutputCode()
            ]
        )