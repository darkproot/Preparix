from .colors import SELECTED
from flet import Row, IconButton, Text, ControlEvent, Page, Container, cupertino_icons
from flet import cupertino_colors, AlertDialog, Column, TextButton, CupertinoFilledButton, TextStyle, BoxShadow, Offset
from data.variables import Variable
from data.operatueur import Operateur
from data.structure_control import Structure
from data.methodes import Methode
from data.fonctions import Fonction
from data.fichier import Fichier
from data.exceptions import Exceptions

def changes(e: ControlEvent):
    page: Page = e.page
    # box = page.controls[2]
    # box.open = False
    chapitre = e.control.data
    display = page.controls[1].controls[0].content.controls[-1]
    titre = page.controls[1].controls[0].content.controls[0].controls[0].content.controls[0]
    match chapitre: 
        case 'variables': 
            display.content = Variable()
            titre.value = chapitre.upper()
        case 'operateurs': 
            display.content = Operateur()
            titre.value = chapitre.upper()
        case 'structures': 
            display.content = Structure()
            titre.value = chapitre.upper()
        case 'methodes': 
            display.content = Methode()
            titre.value = chapitre.upper()
        case 'fonctions': 
            display.content = Fonction()
            titre.value = chapitre.upper()
        case 'exceptions': 
            display.content = Exceptions()
            titre.value = chapitre.upper()
        case 'fichiers': 
            display.content = Fichier()
            titre.value = chapitre.upper()
    page.update()

class Title(Container):
    def __init__(self, title: str, icon: str = cupertino_icons.LIST_BULLET, bgcolor: str = cupertino_colors.ACTIVE_BLUE):
        super().__init__()
        self.expand = True
        self.bgcolor = SELECTED
        self.border_radius = 30
        self.title = title
        self.padding = 10
        self.icon = IconButton(icon, 'white', bgcolor=bgcolor, on_click=self.select)
        self.content = Row(
            [
                Text(self.title, expand=True, text_align='left', font_family='fantasy', size=40),
                self.icon
            ]
        )

    def select(self, e: ControlEvent):
        CHAPITRES: list[str] = ['variables', 'operateurs', 'structures', 'methodes', 'fonctions', 'exceptions', 'fichiers']
        page: Page = e.page
        box = AlertDialog(
            content=Column(height=400, width=500),
            title=Text("Chapitres", font_family='title1', size=40, style=TextStyle(shadow=BoxShadow(1, 1, cupertino_colors.ACTIVE_BLUE, Offset(2, 2)))),
            actions=[TextButton("OK", on_click=lambda _: page.close(box))],
            data='chapitres'
        )
        for chapitre in CHAPITRES:
            box.content.controls.append(Row([CupertinoFilledButton(chapitre.capitalize(), expand=True, data=chapitre, on_click=changes)]))
        # page.add(box)
        box.open = True
        page.open(box)
        page.update()