from flet import ScrollMode
from flet import Container, Column, Text, Row
from assets.code import OutputCode
from .variables import Point, EXEMPLE, load_example, Syntaxe

INTRO = f"{'\t'*4}Une fonction est un bloc de code reutilisable qui effectue une tache specifique; c'est aussi un petit programme qui retourne une valeur."

class Fonction(Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.height = 506
        self.spacing = 10
        self.scroll = ScrollMode.ADAPTIVE
        self.controls = [
            Text(INTRO, font_family='text', size=20),
            Container(height=20),
            Point("1- Definir une fonction"),
            Syntaxe(f"def <nom_fonction>(<liste_param>):\n{'\t'*4}code\n{'\t'*4}return <valeur>   # Optionel", 18),
            Text(f"{'\t'*4}Pour appeler une fonction, on fait suivre son nom de ces parametres effectifs entre parenthese.", font_family='text', size=20),
            Syntaxe("<nom_fonction>(<liste_param>)", 18),
            Row([Text('OU', font_family='text', size=20, expand=True, text_align='center')]),
            Syntaxe("var = <nom_fonction>(<liste_param>)", 18),
            Container(height=20),
            EXEMPLE,
            OutputCode(5, f"def puissance(a, b):\n{'\t'*4}result = a**b\n{'\t'*4}return result\n\nprint(puissance(2, 2))", load_example),
            Container(height=20),
            Point("2- Fonction avec valeur par defaut"),
            EXEMPLE,
            OutputCode(5, f"def ajout(a, b=1):\n{'\t'*4}return a + b\n\nprint(ajout(5))\nprint(ajout(5, 2))", load_example),
            Container(height=20),
            Point("3- Fonction avec retour multiple"),
            Text(f"{'\t'*4}Les fonctions qui reetourne plusieurs valeurs renvoie en realite un tuple.", font_family='text', size=20),
            Container(height=20),
            EXEMPLE,
            OutputCode(6, f"def calcul(a, b):\n{'\t'*4}return a+b, a-b\n\nprint(calcul(2, 3))\nprint('type(calcul(4, 7)) = ', type(calcul(4, 7)))", load_example)
        ]