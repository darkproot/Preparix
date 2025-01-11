from flet import ScrollMode, ControlEvent, TextStyle, BoxShadow, Offset, Page, colors, FontWeight
from flet import Container, Column, Text, Row
from assets.code import OutputCode
from assets.colors import LIGHT_BLUE, FG1

def load_example(e: ControlEvent):
    """
    Fonction qui permet de charger un exemple dans la zone de code.
    """
    page: Page = e.page
    data: str = e.control.data
    display = page.controls[-1].controls[-1].content.controls[0]
    display.value = data
    page.update()

def bold(text: str) -> Container:
    return Container(content=Text(f'\t{text}', font_family='text', size=20, weight='bold', style=TextStyle(shadow=BoxShadow(1, 1, 'black', Offset(2, 2)))), bgcolor=colors.with_opacity(.7, colors.RED_700), padding=5, border_radius=5)

EXEMPLE = Container(content=Text('\tExemple:', font_family='text', size=20, weight='bold', style=TextStyle(shadow=BoxShadow(1, 1, 'black', Offset(2, 2)))), bgcolor=colors.with_opacity(.7, colors.RED_700), padding=5, border_radius=5)
NB = Container(content=Text('\tNB:', font_family='text', size=20, weight='bold', style=TextStyle(shadow=BoxShadow(1, 1, 'black', Offset(2, 2)))), bgcolor=colors.RED_700, padding=5, border_radius=5)
VAR = f"{'\t'*5}Une variable, c'est juste un nom que l'on associe à une valeur, afin d'indiquer à Python de la conserver en mémoire (de ne pas l’eﬀacer) mais aussi de pouvoir la retrouver (grâce à son nom).\n"
VAR2 = f"Syntaxe:\n{'\t'*5}<nom>: <type> = <valeur>"
VAR3 = f"{'\t'*5}Voici les principaux types en python:"
VAR4 = "int: Entier (ex: 5, -3, 42)\nfloat: Nombres a virgule flottante (ex: 3.14, -0.001)\ncomplex: Nombres complexes (ex: 2 + 4j, -3j)"
VAR5 = f"str: Chaine de caracteres (ex: \"hello\", 'python')\nlist: Listes (ex: [1, 2, 3], [10, 'x', 4.5 + j])\ntuple: Tuples (ex: (1, 5), ('a', 'e', 5))\nrange: Sequence d'entiers (ex: range(10), range(1, 11, 2))\n{'\t'*5}Ces types possedent un operateur unaire d'indexation permettant de selectionner un element precis. (ex: 'nom'[0])"
VAR6 = "set: Ensemble non ordonnes avec des elements uniques (ex: {1, 3, 6})\ndict: Dictionnaire (ex: {'nom': 'Alexandra', 'age': 24})\n      Les dictionnaires sont comme des ensembles (set) de couple cle-valeur separer par '':'' et les couples sont separer par des virgules. Pour indexer un element dans un dictionnaire, on met a l'interieur des crochets la cle (ex: mydict['nom'])\n      Pour indexer un element dans un set on utilise le meme operateur que les sequences."
VAR7 = "bool: Valeur booleennes (ex: True, False)\nEn python tout ce qui existe est considere comme True et False dans les autres cas"
class Variable(Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.height = 506
        self.spacing = 10
        self.scroll = ScrollMode.ADAPTIVE
        self.controls = [
            Text(VAR, font_family='text', size=20),
            Syntaxe("<nom_variable>: <type> = <valeur>"),
            EXEMPLE,
            OutputCode(num_line=1, value='nom: str = "python"', on_click=load_example),
            Row([Text('OU',font_family='text', size=20, text_align='center', expand=True),]),
            OutputCode(num_line=1, value='nom = "python"', on_click=load_example),
            Text(VAR3,font_family='text', size=20),
            Container(height=40),
            Point("1- Type numeriques"),
            Text(VAR4,font_family='text', size=20),
            EXEMPLE,
            OutputCode(num_line=3, value='nombre = 7\npi = 3.14\ncoordonne: complex = 3 + 5j', on_click=load_example),
            Container(height=40),
            Point("2- Type de sequence"),
            Text(VAR5,font_family='text', size=20),
            EXEMPLE,
            OutputCode(num_line=5, value="nom = 'Roxane'\ncontact = [655234523, 621456288]\nresidence = ('Biyem-assi', 'melen')\nsequence = range(5)\nprint('residence[0] = ', residence[0])", on_click=load_example),
            Container(height=40),
            Point("3- Type d'ensemble et de mappage"),
            Text(VAR6,font_family='text', size=20),
            EXEMPLE,
            OutputCode(num_line=4, value="N = {1, 2, 3, 4, 5}\nmydict = {'nom': 'Roxane', 'age': 27}\nprint(\"mydict['nom'] = \", mydict['nom'])\nprint(\"mydict['age'] = \", mydict['age'])", on_click=load_example),
            Container(height=40),
            Point("4- Type Booleens"),
            Text(VAR7,font_family='text', size=20),
            EXEMPLE,
            OutputCode(num_line=2, value="valeur1 = [2]     # True\nvaleur2 = ''     # False", on_click=load_example),
            Container(height=40),
            Point("5- Type Special"),
            Text("NoneType: Represente l'absence de valeur (ex: None).\nNone est equivalent au void en language c",font_family='text', size=20),
            EXEMPLE,
            OutputCode(num_line=1, value="data = None", on_click=load_example),
            Container(height=40),
            NB,
            Text(f"{'\t'*5}Pour recuper le type d'une variable on utilise la fonction type(), et on l'affiche dans la console avec la fonction print()",font_family='text', size=20),
            EXEMPLE,
            OutputCode(num_line=6, value="nom = 'Roxane'\nage = 27\ncelibataire = False\nprint(nom, type(nom))\nprint(age, type(age))\nprint(celibataire, type(celibataire))", on_click=load_example),
            Container(height=20),
        ]

class Point(Container):
    def __init__(self, title: str):
        super().__init__()
        self.text = Text(title, font_family='text', size=20, expand=True, weight=FontWeight.W_800,text_align='center', style=TextStyle(shadow=BoxShadow(1, 1, 'black', Offset(2, 2))))
        self.padding = 5
        self.border_radius = 10
        self.bgcolor = colors.with_opacity(.8, LIGHT_BLUE)
        self.content = Row([self.text])

class Syntaxe(Container):
    def __init__(self, syntaxe: str, font_size: int = 20):
        super().__init__()
        self.padding = 10
        self.border_radius = 20
        self.bgcolor = colors.with_opacity(.6, FG1)
        self.content = Column(
            [
                Text("Syntaxe:", font_family='text', size=20, weight=FontWeight.BOLD, style=TextStyle(shadow=BoxShadow(1, 1, 'black', Offset(2, 2)))),
                Row([
                    Container(width=20),
                    Text(syntaxe, font_family='code', size=font_size, style=TextStyle(shadow=BoxShadow(1, 1, 'black', Offset(2, 2))))
                ])
            ],
            spacing=5
        )