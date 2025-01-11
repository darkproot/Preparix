from flet import ScrollMode
from flet import Container, Column, Text
from assets.code import OutputCode
from data.variables import EXEMPLE, load_example, Point, Syntaxe, bold

INTRO = f"{'\t'*4}Une exception est un erreur detectee pendant l'execution du programme. Les exceptions sont utilisees pour gerer des situation imprevues ou des erreur et eviter que le programme ne se termine brutalement. Voici une presentation des exceptions en python."

class Exceptions(Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.height = 506
        self.spacing = 10
        self.scroll = ScrollMode.ADAPTIVE
        self.controls = [
            Text(INTRO, font_family='text', size=20),
            Container(height=20),
            Point("1- Lever une exception: raise"),
            Text(f"{'\t'*4}Pour signaler une exception manuellement, on utilise le mot-cle 'raise'.", font_family='text', size=20),
            Syntaxe("raise <Nom_Exception>(message)"),
            Container(height=20),
            EXEMPLE,
            OutputCode(7, f"def cal(a, b):\n{'\t'*4}if type(a) != type(b):\n{'\t'*8}raise TypeError('Vos donnees sont de type different')\n{'\t'*4}return a + b\n\ncal(2, '1')", load_example),
            Container(height=20),
            Point("2- Gestion des exceptions: try et except"),
            Text(f"{'\t'*4}Pour intercepter et gerer les exceptions, on utilise un bloc 'try' suivi d'un ou plusieurs blocs 'except'", font_family='text', size=20),
            Syntaxe(f"try:\n{'\t'*4}code\nexcept <Exception-1>:\n{'\t'*4}code\nexcept <Exception-i>:\n{'\t'*4}code"),
            Container(height=20),
            EXEMPLE,
            OutputCode(7, f"def cal(a, b):\n{'\t'*4}try:\n{'\t'*8}return a + b\n{'\t'*4}except TypeError:\n{'\t'*8}return int(a) + int(b)\n\nprint(cal(2, '1'))", load_example),
            Container(height=20),
            Point("3- Structure complete d'un bloc try"),
            Syntaxe(f"try:\n{'\t'*4}code\nexcept <Exception-1>\n{'\t'*4}code\nexcept <Exception-i>:\n{'\t'*4}code\nelse:\n{'\t'*4}code1\nfinally:\n{'\t'*4}code2"),
            bold("Code1"),
            Text(f"{'\t'*4}C'est le code qui s'execute si aucune exception ne se produit.", font_family='text', size=20),
            bold("Code2"),
            Text(f"{'\t'*4}C'est le code qui s'execute dans tous les cas", font_family='text', size=20),
            Container(height=20),
            EXEMPLE,
            OutputCode(9, f"def div(a, b):\n{'\t'*4}try: return a/b\n{'\t'*4}except TypeError:\n{'\t'*8}try: return int(a)/int(b)\n{'\t'*8}except ZeroDivisionError:\n{'\t'*12}return False\n{'\t'*4}except ZeroDivisionError: return False\n\nprint(div(1, '0'))", load_example),
            Container(height=20),
            Point("4- Type d'exceptions courantes"),
            bold("ValueError"),
            Text(f"{'\t'*4}Une operation recoit un type de donnee valide mais une erreur inappropriee.", font_family='text', size=20),
            bold("TypeError"),
            Text(f"{'\t'*4}Une operation ou une fonction est applique a un type de donnee inapproprie.", font_family='text', size=20),
            bold("IndexError"),
            Text(f"{'\t'*4}Un indice est en dehors des limites d'une liste ou d'un tuple.", font_family='text', size=20),
            bold("KeyError"),
            Text(f"{'\t'*4}Une cle demandee n'existe pas dans un dictionnaire.", font_family='text', size=20),
            bold("ZeroDivisionError"),
            Text(f"{'\t'*4}Une division ou un modulo pas zero a ete tente.", font_family='text', size=20),
            bold("FileNotFoundError"),
            Text(f"{'\t'*4}Le fichier ou le repertoire demande est introuvable.", font_family='text', size=20),
            bold("IOError"),
            Text(f"{'\t'*4}Une erreur d'entree/sortie se produit.", font_family='text', size=20),
            bold("ImportError"),
            Text(f"{'\t'*4}Une tentative d'importation d'un module a echoue.", font_family='text', size=20),
            bold("NameError"),
            Text(f"{'\t'*4}Une variable ou un nom defini est reference.", font_family='text', size=20),
            bold("AttributeError"),
            Text(f"{'\t'*4}Une tentative d'acces a un attribut inexistant dans un objet est effectuee.", font_family='text', size=20),
            bold("RuntimeError"),
            Text(f"{'\t'*4}Une erreur generique liee a l'execution du programme.", font_family='text', size=20),
        ]