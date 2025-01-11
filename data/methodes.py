from flet import ScrollMode, DataTable, DataColumn, DataRow, DataCell
from flet import Column, Text, Container
from assets.code import OutputCode
from .variables import Point, EXEMPLE, load_example

INTRO = f"{'\t'*5}Les methodes sont similaires aux fonctions mais elles sont associees a des objets et peuvent acceder ou modifier les donnees de ces objets. Les types primaires (int, str, dict) sont des objets en Python. Voici quelques exemples de methode par type:"

class Methode(Column):
    def __init__(self):
        super().__init__()
        string = [
            ['capitalize()', 'Met en majuscule la premiere lettre'],
            ['title()', 'Met en majuscule la premiere lettre de chaque mot'],
            ['upper()', 'Convertit toute la chaine en majiscules'],
            ['lower()', 'Convertit toute la chaine en minuscules'],
            ['swapcase()', 'Inverse la case'],
            ['strip()', 'Supprime les espaces (ou caracteres) au debut et a la fin'],
            ['replace(ancien, nouveau)', 'Remplace une sous chaine par une autre'],
            ['zfill()', 'Ajoute des zeros a gauche pour atteindre une longueur n'],
            ['index(sous_chaine)', 'Revoie l\'index de la premiere occurence'],
            ['isalpha()', 'Verifie si tous les caracteres sont alphabetique'],
            ['isdigit()', 'Verifie si tous les caracteres sont des chiffres'],
            ['isupper()', 'Verifie si tous les caracteres sont en majiscule'],
            ['split(sep)', 'Decoupe la chaine en une liste selon le separateur'],
        ]
        integer = [
            ['int()', 'Convertir une chaine ou un flottant en entier'],
            ['abs(x)', 'Retourne la valeur absolue de x'],
            ['pow(x, y , z)', 'Calcul de (x **y) % z qui est la puissance modulaire'],
            ['divmod(x, y)', 'Retourne quotient et reste de la division entiere'],
            ['round(x, n)', 'Arrondit un nombre a n decimal'],
            ['hex(x)', 'Retourne la representation hexadecimale de l\'entier'],
        ]
        floatting = [
            ['float()', 'Convertir une chaine ou un entier en flottant'],
            ['pow(x, y)', 'Calcul de (x **y) qui est la puissance'],
            ['abs(x)', 'Retourne la valeur absolue de x'],
            ['is_integer()', 'Verifie si le nombre flottant est un entier'],
        ]
        liste = [
            ['append(x)', 'Ajout un element a la fin de la liste'],
            ['extend(sequence)', 'Ajout chaque element d\'une sequence a la fin de la liste'],
            ['insert(i, x)', 'Inserer l\'element x a la position i'],
            ['remove(x)', 'Supprime la premiere occurence de x'],
            ['pop(i)', 'Supprime et retournel\'element a l\'index i, et le dernier element si pas d\'index'],
            ['clear()', 'Supprime tous les elements de la liste'],
            ['index(x, start, end)', 'Retourne l\'index de la premiere occurence de x'],
            ['count(x)', 'Retourne le nombre d\'occurence de x dans la liste'],
            ['sort()', 'Tri la liste en place'],
            ['reverse()', 'Inverse l\'ordre des elements de la liste'],
            ['copy()', 'Retourne une copie superficielle de la liste'],
            ['len()', 'Retourne la longeur de la liste'],
        ]
        dictonary = [
            ['update()', 'Met a jour la dictionnaire avec un autre dictionnaire ou paire cle-valeur'],
            ['pop(key)', 'Supprime et retourne la valeur associe a key'],
            ['popitem()', 'Supprime et retourne le dernier element insere'],
            ['clear()', 'Supprime tous les elements du dictionnaire'],
            ['get(key, default)', 'Retourne la valeur associe a key, et si la cle n\'existe pas retourne default'],
            ['keys()', 'Retourne une vue contenant toutes les cles du dictionnaire'],
            ['values()', 'Retourne une vue contenant toutes les valeurs du dictionnaire'],
            ['items()', 'Retourne une vue contenant toutes les paires cle-valeurs du dictionnaire'],
        ]
        ensemble = [
            ['add(x)', 'Ajouter l\'element x a l\'ensemble'],
            ['update(x)', 'Ajouter plusieurs elements a partir d\'une sequence'],
            ['remove(x)', 'Supprimer x de l\'ensemble'],
            ['discard(x)', 'Supprimer x sans erreur s\'il n\'existe pas'],
            ['union(*other_sets)', 'Retourne l\'union d\'un ensemble avec d\'autres ensembles'],
            ['intersection(*other_sets)', 'Retourne l\'intersection d\'un ensemble avec d\'autres ensembles'],
            ['difference(*other_sets)', 'Retourne la difference emtre les ensembles'],
        ]
        self.expand = True
        self.height = 506
        self.spacing = 10
        self.scroll = ScrollMode.ADAPTIVE
        self.controls = [
            Text(INTRO, font_family='text', size=20),
            Container(height=20),
            Point("1- Chaine de caractere (str)"),
            DataTable(
                columns=[
                    DataColumn(Text("Methodes")),
                    DataColumn(Text("Descriptions")),
                ],
                rows=[
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
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
            OutputCode(6, "chaine: str = 'python est genial! '\nchaine_modif = chaine.strip()\nchaine_modif = chaine_modif.capitalize()\nchaine_modif = chaine_modif.replace('genial', 'puissant')\nprint(chaine_modif)", load_example),
            Container(height=20),
            Point("2- Entier (int)"),
            Text(f"{'\t'*5}Les entiers en Python utilise generalement des fonctions (souvent du module math) pour effectuer des operations mathematiques.", font_family='text', size=20),
            DataTable(
                columns=[
                    DataColumn(Text("Methodes")),
                    DataColumn(Text("Descriptions")),
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
            OutputCode(4, "num = '-34'\nnum = int(num)\nprint('pow(num, 2) = ', pow(num, 2))\nprint('abs(num) = ', abs(num))", load_example),
            Container(height=20),
            Point("3- Reelles (float)"),
            Text(f"{'\t'*5}Les reels (float) ont quasiment les memes fonctions que les entiers (int) notament:", font_family='text', size=20),
            DataTable(
                columns=[
                    DataColumn(Text("Methodes")),
                    DataColumn(Text("Descriptions")),
                ],
                rows=[
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                ]
            ),
            Container(height=20),
            EXEMPLE,
            OutputCode(3, "reel: str = '2.04'\nreel = float(reel)\nprint(round(reel, 1).is_integer())", load_example),
            Container(height=20),
            Point("4- Liste (list)"),
            DataTable(
                columns=[
                    DataColumn(Text("Methodes")),
                    DataColumn(Text("Descriptions")),
                ],
                rows=[
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
                    DataRow(cells=[]),
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
            OutputCode(6, "liste = [1, 5]\nliste.append(2)\nprint(liste)\nliste.sort()\nliste.reverse()\nprint(liste)", load_example),
            Container(height=20),
            Point("5- Dictionnaire (dict)"),
            DataTable(
                columns=[
                    DataColumn(Text("Methodes")),
                    DataColumn(Text("Descriptions")),
                ],
                rows=[
                    DataRow(cells=[]),
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
            OutputCode(5,"mydict = {'nom': \"Roxane\", 'contact': [655123389, 621453212]}\nmydict['age'] = 27\nmydict.update({'contact': [655900345]})\nprint(mydict)", load_example),
            OutputCode(4,"mydict = {'nom': \"Roxane\", 'contact': [655123389, 621453212], 'age':27}\nfor key in mydict:\n\t\t\t\tprint(key, mydict[key], sep=' = ')", load_example),
            Container(height=20),
            Point("6- Ensemble (set)"),
            DataTable(
                columns=[
                    DataColumn(Text("Methodes")),
                    DataColumn(Text("Descriptions")),
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
            OutputCode(4, "s1 = {1, 3, 5, 7}\ns2 = {2, 5, 4, 8}\ns3 = s1.intersection(s2)\nprint(s1, s2, s3, sep=' __')",load_example),
            Container(height=20),
        ]

        for i, methode in enumerate(string):
            for elmt in methode:
                self.controls[3].rows[i].cells.append(
                    DataCell(Container(Text(elmt, font_family='code', size=12)))
                )
        for i, methode in enumerate(integer):
            for elmt in methode:
                self.controls[10].rows[i].cells.append(
                    DataCell(Container(Text(elmt, font_family='code', size=12)))
                )
        for i, methode in enumerate(floatting):
            for elmt in methode:
                self.controls[17].rows[i].cells.append(
                    DataCell(Container(Text(elmt, font_family='code', size=12)))
                )
        for i, methode in enumerate(liste):
            for elmt in methode:
                self.controls[23].rows[i].cells.append(
                    DataCell(Container(Text(elmt, font_family='code', size=12)))
                )
        for i, methode in enumerate(dictonary):
            for elmt in methode:
                self.controls[29].rows[i].cells.append(
                    DataCell(Container(Text(elmt, font_family='code', size=12)))
                )
        for i, methode in enumerate(ensemble):
            for elmt in methode:
                self.controls[36].rows[i].cells.append(
                    DataCell(Container(Text(elmt, font_family='code', size=12)))
                )