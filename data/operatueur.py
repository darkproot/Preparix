from flet import ScrollMode, DataCell, DataColumn, DataRow, DataTable
from flet import Container, Column, Text
from assets.code import OutputCode
from .variables import Point, load_example, EXEMPLE

class Operateur(Column):
    def __init__(self):
        super().__init__()
        operateur_log = [
            ['or', 'ou logique', 'True or False'],
            ['and', 'et logique', 'True and False'],
            ['not', 'negation', 'not True'],
        ]
        operateur_art = [
            ['+', 'Addition', '5 + 4'],
            ['-', 'Soustraction', '5 - 4'],
            ['*', 'Multiplication', '5 * 4'],
            ['/', 'Division', '5 / 4'],
            ['//', 'Division entiere', '5 // 4'],
            ['%', 'Modulo', '5 % 4'],
            ['**', 'Exponentiation', '2**3']
        ]
        operateur_com = [
            ['==', 'Egale a', '5 == 3'],
            ['!=', 'Different de', '5 != 3'],
            ['>', 'Superieur a', '2.5 > 3'],
            ['<', 'Inferieur a', '1 < 3'],
            ['>=', 'Superieur ou egale', '5 >= 3'],
            ['<=', 'Inferieur ou egale', '-3 <= 3'],
        ]
        operateur_id = [
            ['is', 'Comparaison des adresses memoire', 'a is b']
        ]
        operateur_in = [
            ['in', 'Verifie si une valeur est dans une sequence', 'a in "app"']
        ]
        self.expand = True
        self.height = 506
        self.spacing = 10
        self.scroll = ScrollMode.AUTO
        self.controls = [
            Text("Il existe plusieurs operateur en python dont:", font_family='text', size=20),
            Container(height=20),
            Point("1- Operateurs logique"),
            Text("Ce sont ceux qui renvoient un booleen.", font_family='text', size=20),
            DataTable(
                columns=[
                    DataColumn(Text("Operateur", font_family='text', size=15)),
                    DataColumn(Text("Description", font_family='text', size=15)),
                    DataColumn(Text("Exemples", font_family='text', size=15)),
                ],
                rows=[
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[])
                ]
            ),
            Container(height=20),
            EXEMPLE,
            OutputCode(4, 'a = True and False\nb = not False\nprint("a = ", a)\nprint("b = ", b)', load_example),
            Container(height=20),
            Point("2- Operateurs arithmetiques"),
            DataTable(
                columns=[
                    DataColumn(Text("Operateur", font_family='text', size=15)),
                    DataColumn(Text("Description", font_family='text', size=15)),
                    DataColumn(Text("Exemples", font_family='text', size=15)),
                ],
                rows=[
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                ]
            ),
            Container(height=20),
            EXEMPLE,
            OutputCode(5, 'a = 2\nb = 3\nprint("a + b = ", a+b)\nprint("a**b = ", a**b)\nprint("b//a = ", b//a)', load_example),
            Container(height=20),
            Point("3- Operateurs de comparaison"),
            Text("Ces Operateurs permettent la comparaison de deux type et renvoie un booleen. ", font_family='text', size=20),
            DataTable(
                columns=[
                    DataColumn(Text("Operateur", font_family='text', size=15)),
                    DataColumn(Text("Description", font_family='text', size=15)),
                    DataColumn(Text("Exemples", font_family='text', size=15)),
                ],
                rows=[
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                ]
            ),
            Container(height=20),
            EXEMPLE,
            OutputCode(5, 'a = 3\nb = 4.5\nprint("a <= b", a <= b)\nprint("b == -a", a == -b)\nprint("a != b + 1.5", a != b + 1.5)', load_example),
            Container(height=20),
            Point("4- Operateurs d'identite"),
            DataTable(
                columns=[
                    DataColumn(Text("Operateur", font_family='text', size=15)),
                    DataColumn(Text("Description", font_family='text', size=15)),
                    DataColumn(Text("Exemples", font_family='text', size=15)),
                ],
                rows=[
                    DataRow(cells=[]),
                ]
            ),
            Container(height=20),
            EXEMPLE,
            OutputCode(5, 'a = 2\nb = 2\nc = 2 != 2\nprint("a is b = ", a is b)\nprint("type(c) is bool", type(c) is bool)', load_example),
            Container(height=20),
            Point("5- Operateurs d'appartenance"),
            DataTable(
                columns=[
                    DataColumn(Text("Operateur", font_family='text', size=15)),
                    DataColumn(Text("Decription", font_family='text', size=15)),
                    DataColumn(Text("Exemples", font_family='text', size=15)),
                ],
                rows=[
                    DataRow(cells=[]),
                ]
            ),
            Container(height=20),
            EXEMPLE,
            OutputCode(3, 'a = "salutation"\nprint("lu" in a)\nprint(2 in {1, 3, 4})', load_example),
            Container(height=20),
        ]
        for i, op in enumerate(operateur_log):
            for elmt in op:
                self.controls[4].rows[i].cells.append(
                    DataCell(Text(elmt, font_family='code'))
                )
        for i, op in enumerate(operateur_art):
            for elmt in op:
                self.controls[10].rows[i].cells.append(
                    DataCell(Text(elmt, font_family='code'))
                )
        for i, op in enumerate(operateur_com):
            for elmt in op:
                self.controls[17].rows[i].cells.append(
                    DataCell(Text(elmt, font_family='code'))
                )
        for i, op in enumerate(operateur_id):
            for elmt in op:
                self.controls[23].rows[i].cells.append(
                    DataCell(Text(elmt, font_family='code'))
                )
        for i, op in enumerate(operateur_in):
            for elmt in op:
                self.controls[29].rows[i].cells.append(
                    DataCell(Column([Text(elmt, font_family='code')], height=10))
                )