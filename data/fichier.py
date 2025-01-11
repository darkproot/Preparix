from flet import DataCell, DataColumn, DataTable, DataRow, ScrollMode
from flet import Container, Column, Text
from assets.code import OutputCode
from .variables import EXEMPLE, load_example, Point, Syntaxe, NB, bold

INTRO = f"{'\t'*4}En Python, la gestion des fichiers se fait facilement avec les fonctions integrees, ce qui permet de lire, ecrire, modifier et supprimer des fichiers."

class Fichier(Column):
    def __init__(self):
        super().__init__()
        modes =[
            ['r', 'read(), readlines()'],
            ['w', 'write(), writelines()'],
        ]
        self.expand = True
        self.height = 506
        self.spacing = 10
        self.scroll = ScrollMode.ADAPTIVE
        self.controls = [
            Text(INTRO, font_family='text', size=20),
            Container(height=20),
            Point("1- Ouvrir et fermer un fichier"),
            Text("La fonction open() est utilisee pour ouvrir un fichier et close() pour le fermer. Elle retourne un objet fichier.", font_family='text', size=20),
            Syntaxe("<nom_variable> = open(<chemin_fichier>, <mode>)\n<nom_variable>.close()", 14),
            Container(height=20),
            bold("'r'"),
            Text("Ouvre le fichier en mode lecture (par defaut). Le fichier doit exister.", font_family='text', size=20),
            bold("'w'"),
            Text("Ouvre le fichier en mode ecriture. Si le fichier existe, il est vide. Sinon, il est cree.", font_family='text', size=20),
            bold("'a'"),
            Text("Ouvre le fichier en mode ajout. Si le fichier n'existe pas il est cree. Les donnees sont ajoutees a la fin.", font_family='text', size=20),
            bold("'b'"),
            Text("Ouvre le fichier en mode binaire.", font_family='text', size=20),
            bold("'r+'"),
            Text("Ouvre le fichier en mode lecture et ecriture. Le fichier doit exister.", font_family='text', size=20),
            bold("'w+'"),
            Text("Ouvre le fichier en mode lecture et ecriture. Le fichier est vide s'il existe. Sinon, il est cree.", font_family='text', size=20),
            DataTable(
                columns=[
                    DataColumn(Text("MODES")),
                    DataColumn(Text("METHODES")),
                ],
                rows=[
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                ]
            ),
            Container(height=20),
            EXEMPLE,
            OutputCode(4, "file = open('data.txt', 'w')\nret = file.write('Roxane')\nfile.close()\nprint(ret)", load_example),
            Container(height=20),
            NB,
            Text(f"{'\t'*4}TOUJOURS FERMER UN FICHIER.\n{'\t'*4}Pour eviter des oublies de fermeture de fichier ou une interruption du programme empechant sa fermeture, il existe le mot cle 'with' qui assure l'ouverture et la fermeture d'un fichier.", font_family='text', size=20),
            Syntaxe(f"with open(fichier, mode) as <nom>:\n{'\t'*4}codes", 18),
            Container(height=20),
            EXEMPLE,
            OutputCode(3, f"def data_write(path, data):\n{'\t'*4}with open(path, 'w') as f:\n{'\t'*8}return f.write(data)", load_example)
        ]
        for i, mode in enumerate(modes):
            for elmt in mode:
                self.controls[18].rows[i].cells.append(
                    DataCell(Container(Text(elmt, font_family='code', size=12)))
                )