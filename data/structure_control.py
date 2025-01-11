from flet import ScrollMode
from flet import Container, Column, Text
from assets.code import OutputCode
from .variables import load_example, Syntaxe, EXEMPLE, Point, NB, bold

INTRO = f"{'\t'*5}Les structures de controle en python permettent de gerer le flux d'execution du programme. Elles incluent des instructions conditionnelles, des boucles et des instructions de controle de flux. Voici un resume des principales structures:"
BREAK = f"{'\t'*4}Interrompt la boucle immediatement."
CONTINUE = f"{'\t'*4}Passe directement a l'iteration suivante."
PASS = f"{'\t'*4}Sert de placeholder pour une boucle ou condition vide."

class Structure(Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.height = 506
        self.spacing = 10
        self.scroll = ScrollMode.ADAPTIVE
        self.controls = [
            Text(INTRO, font_family='text', size=20),
            Container(height=20),
            Point("1- Structures conditionnelles"),
            Text(f"{'\t'*5}Elles permettent d'executer du code en fonction d'une condition.", font_family='text', size=20),
            Syntaxe(f"if (condition):\n{"\t"*5}code\nelif (condition):\n{"\t"*5}code\nelse:\n{"\t"*5}code"),
            Container(height=20),
            NB,
            Text(f"{'\t'*5}NE JAMAIS OUBLIE L'INDENTATION.", font_family='text', size=20),
            Container(height=20),
            EXEMPLE,
            OutputCode(6, f"x=10\nif x>0:\n{"\t"*4}print('x est positif')\nelif x == 0:\n{"\t"*4}print('x est nul')\nelse: print('x est negatif')", on_click=load_example),
            Container(height=20),
            Point("2- Boucles (for)"),
            Text(f"{'\t'*5}Elle permet repeter un groupe d'intruction lorsqu'on connait le nombre de fois que cela doit ce faire.", font_family='text', size=20),
            Syntaxe(f"for <compteur> in <sequence>:\n{'\t'*5}code"),
            Container(height=20),
            EXEMPLE,
            OutputCode(2, f"for i in range(5):\n{"\t"*4}print(i)", on_click=load_example),
            OutputCode(3, f"fruits = ['pomme', 'banane', 'cerise']\nfor fruit in fruits:\n{"\t"*4}print(fruit)", on_click=load_example),
            Container(height=20),
            Point("3- Boucles (while)"),
            Text(f"{'\t'*5}Elle permet repeter un groupe d'intruction lorsqu'on ne connait pas le nombre de fois que cela doit ce faire.", font_family='text', size=20),
            Syntaxe(f"while (condition):\n{'\t'*5}code"),
            Container(height=20),
            EXEMPLE,
            OutputCode(4, f"x = 0\nwhile x<5:\n{"\t"*4}print(x)\n{"\t"*4}x += 1", on_click=load_example),
            Container(height=20),
            Point("4 - Instructions de controle de boucle (break, continue, pass)"),
            bold('break'),
            Text(BREAK, font_family='text', size=20),
            bold('continue'),
            Text(CONTINUE, font_family='text', size=20),
            bold('pass'),
            Text(PASS, font_family='text', size=20),
            Container(height=20),
            EXEMPLE,
            OutputCode(6, f"for i in range(10):\n{'\t'*4}if i == 5:\n{'\t'*8}break  # STOP a 5\n{'\t'*4}if i == 2:\n{'\t'*8}continue   # IGNORE 2 \n{'\t'*4}print(i)", load_example),
            Container(height=20),
            Point("5 - Match (equivalent du switch-case)"),
            Text(f"{'\t'*5}Permet une gestion du flux au cas par cas.", font_family='text', size=20),
            Syntaxe(f"match <variable>:\n{'\t'*4}case <valeur1>:\n{'\t'*8}code\n{'\t'*4}case <valeuri>:\n{'\t'*8}code\n{'\t'*4}case _:   # Valeur par defaut\n{'\t'*8}code"),
            Container(height=20),
            EXEMPLE,
            OutputCode(8, f"command = 'start'\nmatch command:\n{'\t'*4}case 'start':\n{'\t'*8}print('Demarrage')\n{'\t'*4}case 'stop':\n{'\t'*8}print('Arret')\n{'\t'*4}case _:\n{'\t'*8}print('Commande inconnue')", on_click=load_example),
        ]