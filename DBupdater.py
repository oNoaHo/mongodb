#!/usr/bin/env python3

from pymongo import MongoClient
from random import randint
import random
import string
import pprint
import time

start_time = time.time()
chars = string.ascii_lowercase + string.digits
client = MongoClient(port=27017)
ddiadmindb = client.ddiadmin
users = ddiadmindb.users


firstname = ['Marie', 'Sophie', 'Maria', 'Noah', 'Marie', 'Emilia', 'Paul', 'Ben', 'Mia', 'Jonas', 'Mila', 'Lina', 'Anton', 'Tom', 'Alexander', 'Emma', 'Leon', 'Anna', 'Lea', 'Felix', 'Elias', 'Oskar', 'Ella', 'Maximilian', 'Liam', 'Theo', 'Jakob', 'Katharina', 'Leo', 'Charlotte', 'Clara', 'Leni', 'Leonard', 'Henry', 'Maximilian', 'Lena', 'Sophia', 'David', 'Luis', 'Moritz', 'Sophie', 'Greta', 'Jonathan', 'Finn', 'Leonie', 'Milan', 'Julian', 'Mats', 'Luca', 'Elif', 'Julius', 'Charlotte', 'Lara', 'Paula', 'Adam', 'Emily', 'Hanna', 'Luisa', 'Mina', 'Elisabeth', 'Johanna', 'Tim', 'Vincent', 'Ida', 'Louis', 'Alexander', 'Elias', 'Elisa', 'Hannah', 'Lukas', 'Johanna', 'Klara', 'Henri', 'Mira', 'Emil', 'Lia', 'Mathilda', 'Matilda', 'Max', 'Paul', 'Sofia', 'Jan', 'Nele', 'Frida', 'Levi', 'Nora', 'Amelie', 'Ali', 'Anna', 'Anton', 'Emilia', 'Emir', 'Frieda', 'Karl', 'Luise', 'Marlene', 'Sophia', 'Tilda', 'Yusuf', 'Lotta', 'Maja', 'Romy', 'Samuel', 'Theodor', 'Benjamin', 'Matteo', 'Niklas', 'Mara', 'Maria', 'Philipp', 'Johann', 'Maya', 'Melina', 'Mika', 'Nur', 'Sarah', 'Amalia', 'Antonia', 'David', 'Ela', 'Laura', 'Lisa', 'Erik', 'Fabian', 'Gabriel', 'Helena', 'Luisa', 'Sara', 'Alina', 'Carla', 'Daniel', 'Isabella', 'Jakob', 'Jana', 'Lian', 'Peter', 'Ali', 'Carlotta', 'Johann', 'Johannes', 'Jonah', 'Josefine', 'Julia', 'Lilly', 'Piet', 'Ava', 'Elena', 'Karl', 'Valentin', 'Adrian', 'Elisa', 'Jasper', 'Juna', 'Louisa', 'Mateo', 'Ole', 'Simon', 'Victoria', 'Alessia', 'Bruno', 'Carl', 'Felix', 'Gabriel', 'Henry', 'Johannes', 'Josef', 'Joshua', 'Malik', 'Olivia', 'Pauline', 'Pauline', 'Philipp', 'Ilyas', 'Leonardo', 'Milo', 'Toni', 'Valentin', 'Victoria', 'Zoe', 'Emil', 'Jannis', 'Jona', 'Karla', 'Luise', 'Luna', 'Thea', 'Zeynep', 'Aaron', 'Benjamin', 'Jonathan', 'Julius', 'Kian', 'Leonard', 'Liya', 'Maria', 'Marlene', 'Marlon', 'Matthias', 'Michael', 'Muhammed', 'Noah', 'Paulina', 'Till', 'Benedikt', 'Constantin', 'Eva', 'Louise', 'Luan', 'Luana', 'Meryem', 'Stella', 'Alessio', 'Elina', 'Emilio', 'Jan', 'Jonte', 'Josefine', 'Josephine', 'Julian', 'Justus', 'Kaan', 'Luca', 'Lukas', 'Merle', 'Mikail', 'Milla', 'Rosa', 'Sofia', 'Su', 'Timo', 'Alma', 'Amelia', 'Amina', 'Carlo', 'Daniel', 'Frederik', 'Hira', 'Kilian', 'Matilda', 'Nils', 'Pia', 'Ferdinand', 'Friedrich', 'Isabel', 'Isabelle', 'Jule', 'Katharina', 'Lennard', 'Leon', 'Levi', 'Liv', 'Lucas', 'Luka', 'Rafael', 'Raphael', 'Rose', 'Sebastian', 'Alva', 'Benno', 'Can', 'Deniz', 'Emilian', 'Finja', 'Florian', 'Fritz', 'Hannes', 'Jannik', 'Jonas', 'Linda', 'Louis', 'Maria', 'Martin', 'Maxim', 'Nick', 'Nina', 'Pepe', 'Sam', 'Viola', 'Alice', 'Arian', 'Ayla', 'Damian', 'Elisabeth', 'Emmi', 'Ferdinand', 'Fiona', 'Georg', 'Isabella', 'Josephine', 'Julia', 'Lana', 'Leyla', 'Linus', 'Louisa', 'Malia', 'Matti', 'Mert', 'Mohammed', 'Nisa', 'Oskar', 'Samuel', 'Theodor', 'Aaliyah', 'Aleyna', 'Amin', 'Anastasia', 'Arthur', 'Aurora', 'Carl', 'Ellen', 'Emilie', 'Finn', 'Frederik', 'Henri', 'Konstantin', 'Lasse', 'Lena', 'Lennox', 'Leo', 'Lias', 'Lio', 'Magdalena', 'Martin', 'Miray', 'Mohamed', 'Mohammad', 'Musa', 'Nela', 'Nicolas', 'Philip', 'Rayan', 'Robin', 'Sophie', 'Valentina', 'Wilhelm', 'Andreas', 'Antonio', 'Aras', 'Aurelia', 'Ayaz', 'Azra', 'Carlotta', 'Christina', 'Diana', 'Elif', 'Elise', 'Elli', 'Emir', 'Emma', 'Enes', 'Enna', 'Enno', 'Eymen', 'Grace', 'Heinrich', 'Henrik', 'Hugo', 'Joel', 'Joel', 'John', 'Laila', 'Lene', 'Levin', 'Liam', 'Liana', 'Marie', 'Mathilda', 'Melissa', 'Mia', 'Milan', 'Milana', 'Mustafa', 'Nico', 'Noel', 'Rosa', 'Silas', 'Sofie', 'Valentina', 'Viktoria', 'Alessandro', 'Alexandra', 'Alicia', 'Aliyah', 'Amira', 'Amy', 'Anni', 'Antonia', 'Aylin', 'Bela', 'Bo', 'Caspar', 'Christian', 'Eleni', 'Elisabeth', 'Ellie', 'Emin', 'Fabian', 'Fatima', 'Filip', 'Franziska', 'Fritz', 'Giulia', 'Helen', 'Helena', 'Ibrahim', 'Jaron', 'Joris', 'Joshua', 'Lennart', 'Lenny', 'Lola', 'Lorena', 'Lotte', 'Luis', 'Mahir', 'Malik', 'Malina', 'Malou', 'Martha', 'Matteo', 'Maxim', 'Melek', 'Michel', 'Milena', 'Mina', 'Miran', 'Mona', 'Nila', 'Ole', 'Pablo', 'Phil', 'Philippa', 'Pina', 'Selma', 'Sofie', 'Theresa', 'Theresa', 'Umut', 'Viktoria', 'Yuna', 'Zehra', 'Adam', 'Adriana', 'Ahmet', 'Alan', 'Bilal', 'Can', 'Cleo', 'Diego', 'Dominik', 'Efe', 'Elena', 'Elia', 'Eliah', 'Elyas', 'Emilio', 'Emin', 'Eric', 'Esila', 'Esma', 'Fabio', 'Felicitas', 'Flora', 'Franz', 'Giuliano', 'Greta', 'Hamza', 'Helene', 'Helene', 'James', 'Jannes', 'Joscha', 'Juri', 'Kaspar', 'Kenan', 'Kerem', 'Kiyan', 'Klara', 'Leana', 'Leonie', 'Lilli', 'Lina', 'Linus', 'Lou', 'Louise', 'Lucia', 'Lucy', 'Lynn', 'Malou', 'Mario', 'Mark', 'Marla', 'Matthias', 'Mattis', 'Max', 'Mayla', 'Moritz', 'Nicolas', 'Nika', 'Noel', 'Oliver', 'Omar', 'Raphael',
             'Rolf', 'Salvatore', 'Sebastian', 'Selim', 'Selina', 'Titus', 'Tobias', 'Abdullah', 'Ahmad', 'Alea', 'Alex', 'Alexandros', 'Alisa', 'Amalia', 'Amelie', 'Amir', 'Anas', 'Angelo', 'Ariana', 'Aron', 'Aurelio', 'Ben', 'Bruno', 'Chiara', 'Christian', 'Christine', 'Dana', 'Eda', 'Ela', 'Eslem', 'Francesco', 'Frederick', 'Giuseppe', 'Gloria', 'Hans', 'Hendrik', 'Ilay', 'Ivan', 'Jaro', 'Jasmin', 'Justus', 'Kaan', 'Kira', 'Leandro', 'Leona', 'Leopold', 'Lia', 'Liah', 'Liara', 'Lion', 'Lionel', 'Liv', 'Lotta', 'Lucia', 'Luke', 'Margarete', 'Marko', 'Maryam', 'Michelle', 'Miriam', 'Nathan', 'Neo', 'Noemi', 'Olivia', 'Oscar', 'Paulina', 'Philip', 'Ronja', 'Rosalie', 'Semih', 'Sena', 'Tara', 'Thiago', 'Tuana', 'Valerie', 'Vanessa', 'Vincent', 'Adrian', 'Adriano', 'Alexandra', 'Alina', 'Amine', 'Annika', 'Antonio', 'Ari', 'Aria', 'Armin', 'Arne', 'Arthur', 'Asaf', 'August', 'Ayoub', 'Benedikt', 'Charlie', 'Charlotte', 'Clara', 'Constantin', 'Dalia', 'Daria', 'Dean', 'Devran', 'Eleni', 'Elian', 'Eliana', 'Eliano', 'Elise', 'Ellen', 'Eren', 'Felicitas', 'Filippa', 'Francesco', 'Frieda', 'Fritzi', 'Halis', 'Hanna', 'Hannes', 'Hasan', 'Helin', 'Ibrahim', 'Jacob', 'Jakub', 'Jano', 'Jasper', 'Jayden', 'Johan', 'Jolina', 'Jonah', 'Julie', 'Karlo', 'Katharina', 'Konstantin', 'Kuzey', 'Lars', 'Leander', 'Leandro', 'Leia', 'Lilia', 'Lilly', 'Linn', 'Livia', 'Lotte', 'Lou', 'Magdalena', 'Malak', 'Marleen', 'Martin', 'Medina', 'Michael', 'Miguel', 'Mio', 'Nevio', 'Niklas', 'Nikolas', 'Nina', 'Philippa', 'Rafael', 'Robert', 'Sami', 'Selin', 'Severin', 'Tessa', 'Theo', 'Thomas', 'Timur', 'Valeria', 'Wilhelm', 'Wolfgang', 'Yannick', 'Zoey', 'Ada', 'Ahmed', 'Ahsen', 'Aliya', 'Alp', 'Andreas', 'Annabell', 'Anouk', 'Arian', 'Arina', 'Arya', 'Asya', 'Aurelia', 'Ava', 'AyÅŸe', 'Barbara', 'Berat', 'Camille', 'Carla', 'Caspar', 'Casper', 'Cataleya', 'Ceylin', 'Christin', 'Christoph', 'Cornelius', 'Damla', 'Devin', 'Edda', 'Edgar', 'Efe', 'Eleonora', 'Eleonore', 'Elijah', 'Ella', 'Emelie', 'Enno', 'Eray', 'Fiete', 'Florentine', 'Florentine', 'Freya', 'Friedrich', 'Fynn', 'Giuseppe', 'Gustav', 'Gustav', 'Hamza', 'Hana', 'Hannah', 'Hedi', 'Hermann', 'Ida', 'Isabel', 'Jack', 'Jacob', 'Jamie', 'Janis', 'Janosch', 'Jolie', 'Jona', 'Jonna', 'Jorin', 'Julie', 'Karim', 'Kerim', 'Konrad', 'Konrad', 'Laurenz', 'Lea', 'Leano', 'Leia', 'Len', 'Leonardo', 'Leonora', 'Levian', 'Lino', 'Luan', 'Luke', 'Lynn', 'Maila', 'Malin', 'Malte', 'Marc', 'Marco', 'Marina', 'Marta', 'Mattia', 'Mattis', 'May', 'Maya', 'Mehmet', 'Melek', 'Meryem', 'Mete', 'Meyra', 'Mick', 'Miguel', 'Mika', 'Mike', 'Milo', 'Musa', 'Natalie', 'Naz', 'Nicklas', 'Nikita', 'Onur', 'Oscar', 'Peter', 'Renate', 'Richard', 'Robert', 'Roman', 'Ruby', 'Salvatore', 'Sara', 'Simon', 'Soraya', 'Stefan', 'Talia', 'Teresa', 'Thilo', 'Thomas', 'Tom', 'Ulrich', 'Uwe', 'Valentino', 'Victor', 'Vivien', 'Yasin', 'Yassin', 'Younes', 'Yusuf', 'Zeynep', 'Ada', 'Adem', 'Adil', 'Ahmad', 'Ahmed', 'Albert', 'Albert', 'Alberto', 'Alexandru', 'Almira', 'Alya', 'Amar', 'Amaru', 'Amilia', 'Anastasia', 'Angelina', 'Angelo', 'Anisa', 'Annabelle', 'Antonella', 'Arion', 'Atilla', 'Bastian', 'Bastian', 'Bela', 'Bennet', 'Bo', 'Bryan', 'Caroline', 'Celina', 'Celina', 'Chiara', 'Chris', 'Christopher', 'Claire', 'Claudia', 'Connor', 'Darian', 'Defne', 'Deniz', 'Dilara', 'Dirk', 'Dominic', 'Dorothea', 'Ece', 'Ediz', 'Eduard', 'Ege', 'Elijah', 'Eliz', 'Elsa', 'Emely', 'Emilian', 'Emre', 'Emre', 'Evin', 'Fatma', 'Fiete', 'Fiona', 'Franziska', 'Fred', 'Freda', 'Freya', 'Frida', 'Gerhard', 'Gioia', 'Hafsa', 'Hasan', 'Hatice', 'Hazal', 'Helen', 'Henning', 'Henrik', 'Hilda', 'Ilyas', 'Iman', 'Isabell', 'Isabelle', 'James', 'Jane', 'Janosch', 'Jara', 'Jari', 'Joleen', 'Josefine', 'Juli', 'Juna', 'Juno', 'Kalle', 'Karl', 'Kasimir', 'Kemal', 'Kevin', 'Koray', 'Kristin', 'Layla', 'Leah', 'Lean', 'Leander', 'Lee', 'Leni', 'Lenn', 'Leopold', 'Letizia', 'Leyla', 'Liliana', 'Lisa', 'Liya', 'Liyan', 'Lorenzo', 'Lucas', 'Lucie', 'Ludwig', 'Luise', 'Luka', 'Madita', 'Madita', 'Mads', 'Magnus', 'Maia', 'Maja', 'Manfred', 'Mara', 'Margaretha', 'Maria', 'Marleen', 'Marlena', 'Martha', 'Matea', 'Matheo', 'Mathilde', 'Mathilde', 'Matti', 'Maurice', 'Maurice', 'Maximilian', 'Melike', 'Melin', 'Melis', 'Mert', 'Merve', 'Michel', 'Mila', 'Mira', 'Mirza', 'Murat', 'Nael', 'Naomi', 'Narin', 'Nelson', 'Neo', 'Neyla', 'Nik', 'Niko', 'Nilay', 'Nour', 'Nova', 'Oliver', 'Pablo', 'Paula', 'Pepe', 'Peter', 'Philine', 'Phillip', 'Pius', 'Renas', 'Renate', 'Romeo', 'Rudolf', 'Runa', 'Ryan', 'Sabine', 'Safiya', 'Said', 'Severin', 'Seyyid', 'Sina', 'Singh', 'Sultan', 'Taavi', 'Talha', 'Thea', 'Theodora', 'Thore', 'Tiara', 'Tristan', 'Valeria', 'Vera', 'Vincenzo', 'Willem', 'Willem', 'Willi', 'William']
lastname = ['Müller', 'Schmidt', 'Schneider', 'Fischer', 'Weber', 'Meyer', 'Wagner', 'Schulz', 'Becker', 'Hoffmann', 'Schäfer', 'Koch', 'Richter', 'Bauer', 'Klein', 'Wolf', 'Schröder', 'Neumann', 'Schwarz', 'Zimmermann', 'Braun', 'Hofmann', 'Krüger', 'Hartmann', 'Lange', 'Schmitt', 'Werner', 'Schmitz', 'Krause', 'Meier', 'Lehmann', 'Schmid', 'Schulze', 'Maier', 'Köhler', 'Herrmann', 'Walter', 'König', 'Mayer', 'Huber', 'Kaiser', 'Fuchs', 'Peters', 'Lang', 'Scholz', 'Möller', 'Weiß', 'Jung', 'Hahn', 'Schubert', 'Vogel', 'Friedrich', 'Günther', 'Keller', 'Winkler', 'Frank', 'Berger', 'Roth', 'Beck', 'Lorenz', 'Baumann', 'Franke', 'Albrecht', 'Schuster', 'Simon', 'Ludwig', 'Böhm', 'Winter', 'Kraus', 'Martin', 'Schumacher', 'Krämer', 'Vogt', 'Otto', 'Jäger', 'Stein', 'Groß', 'Sommer', 'Seidel', 'Heinrich', 'Haas', 'Brandt', 'Schreiber', 'Graf', 'Dietrich', 'Schulte', 'Kühn', 'Ziegler', 'Kuhn', 'Pohl', 'Engel', 'Horn', 'Bergmann', 'Voigt', 'Busch', 'Thomas', 'Sauer', 'Arnold', 'Pfeiffer', 'Wolff', 'Beyer', 'Seifert', 'Ernst', 'Lindner', 'Hübner', 'Kramer', 'Jansen', 'Franz', 'Peter', 'Hansen', 'Wenzel', 'Götz', 'Paul', 'Riedel', 'Barth', 'Kern', 'Hermann', 'Nagel', 'Wilhelm', 'Ott', 'Bock', 'Langer', 'Grimm', 'Ritter', 'Haase', 'Lenz', 'Förster', 'Mohr', 'Kruse', 'Schumann', 'Jahn', 'Thiel', 'Kaufmann', 'Zimmer', 'Hoppe', 'Petersen', 'Fiedler', 'Berg', 'Arndt', 'Marx', 'Lutz', 'Fritz', 'Kraft', 'Michel', 'Walther', 'Böttcher', 'Schütz', 'Eckert', 'Sander', 'Thiele', 'Reuter', 'Reinhardt', 'Schindler', 'Ebert', 'Kunz', 'Schilling', 'Schramm', 'Voß', 'Nowak', 'Hein', 'Hesse', 'Frey', 'Rudolph', 'Fröhlich', 'Beckmann', 'Kunze', 'Herzog', 'Bayer', 'Behrens', 'Stephan', 'Büttner', 'Gruber', 'Adam', 'Gärtner', 'Witt', 'Maurer', 'Bender', 'Bachmann', 'Schultz', 'Seitz', 'Geiger', 'Stahl', 'Steiner', 'Scherer', 'Kirchner', 'Dietz', 'Ullrich', 'Kurz', 'Breuer', 'Gerlach', 'Ulrich', 'Brinkmann', 'Fink', 'Heinz', 'Löffler', 'Reichert', 'Naumann', 'Böhme', 'Schröter', 'Blum', 'Göbel', 'Moser', 'Schlüter', 'Brunner', 'Körner', 'Schenk', 'Wirth', 'Wegner', 'Brand', 'Wendt', 'Stark', 'Schwab', 'Krebs', 'Heller', 'Wolter', 'Reimann', 'Rieger', 'Unger', 'Binder', 'Bruns', 'Döring', 'Menzel', 'Buchholz', 'Ackermann', 'Rose', 'Meißner', 'Janssen', 'Bartsch', 'May', 'Hirsch', 'Jakob', 'Schiller', 'Kopp', 'John', 'Hinz', 'Bach', 'Pfeifer', 'Bischoff', 'Engelhardt', 'Wilke', 'Sturm', 'Hildebrandt', 'Siebert', 'Urban', 'Link', 'Rohde', 'Kohl', 'Linke', 'Wittmann', 'Fricke', 'Köster', 'Gebhardt', 'Weiss', 'Vetter', 'Freitag', 'Nickel', 'Hennig', 'Rau', 'Münch', 'Witte', 'Noack', 'Renner', 'Westphal', 'Reich', 'Will', 'Baier', 'Kolb', 'Brückner', 'Marquardt', 'Kiefer', 'Keil', 'Henning', 'Heinze', 'Funk', 'Lemke', 'Ahrens', 'Esser', 'Pieper', 'Baum', 'Conrad', 'Schlegel', 'Fuhrmann', 'Decker', 'Jacob', 'Held', 'Röder', 'Berndt', 'Hanke', 'Kirsch', 'Neubauer', 'Hammer', 'Stoll', 'Erdmann', 'Mann', 'Philipp', 'Schön', 'Wiese', 'Kremer', 'Bartels', 'Klose', 'Mertens', 'Schreiner', 'Dittrich', 'Krieger', 'Kröger', 'Krug', 'Harms', 'Henke', 'Großmann', 'Martens', 'Heß', 'Schrader', 'Strauß', 'Adler', 'Herbst', 'Kühne', 'Heine', 'Konrad', 'Kluge', 'Henkel', 'Wiedemann', 'Albert', 'Popp', 'Wimmer', 'Karl', 'Wahl', 'Stadler', 'Hamann', 'Kuhlmann', 'Steffen', 'Lindemann', 'Fritsch', 'Bernhardt', 'Burkhardt', 'Preuß', 'Metzger', 'Bader', 'Nolte', 'Hauser', 'Blank', 'Beier', 'Klaus', 'Probst', 'Hess', 'Zander', 'Miller', 'Niemann', 'Funke', 'Haupt', 'Burger', 'Bode', 'Holz', 'Jost', 'Rauch', 'Rothe', 'Herold', 'Jordan', 'Anders', 'Fleischer', 'Wiegand', 'Hartung', 'Janßen', 'Lohmann', 'Krauß', 'Vollmer', 'Baur', 'Heinemann', 'Wild', 'Brenner', 'Reichel', 'Wetzel', 'Christ', 'Rausch', 'Hummel', 'Reiter', 'Mayr', 'Knoll', 'Kroll', 'Wegener', 'Beer', 'Schade', 'Neubert', 'Merz', 'Schüler', 'Strobel', 'Diehl', 'Behrendt', 'Glaser', 'Feldmann', 'Hagen', 'Jacobs', 'Rupp', 'Geißler', 'Straub', 'Hohmann', 'Römer', 'Stock', 'Haag', 'Meister', 'Freund', 'Dörr', 'Kessler', 'Betz', 'Seiler', 'Altmann', 'Weise', 'Metz', 'Eder', 'Busse', 'Mai', 'Wunderlich', 'Schütte', 'Hentschel', 'Voss', 'Weis', 'Heck', 'Born', 'Falk', 'Raab', 'Lauer', 'Völker', 'Bittner', 'Merkel', 'Sonntag', 'Moritz', 'Ehlers', 'Bertram', 'Hartwig', 'Rapp', 'Gerber', 'Zeller', 'Scharf', 'Pietsch', 'Kellner', 'Bär', 'Eichhorn', 'Giese', 'Wulf', 'Block', 'Opitz', 'Gottschalk', 'Jürgens', 'Greiner', 'Wieland', 'Benz', 'Keßler', 'Steffens', 'Heil', 'Seeger', 'Stumpf', 'Gross', 'Bühler', 'Eberhardt', 'Hiller', 'Buck', 'Weigel', 'Schweizer', 'Albers', 'Heuer', 'Pape', 'Hempel', 'Schott', 'Schütze', 'Scheffler', 'Engelmann', 'Wiesner', 'Runge', 'Geyer', 'Neuhaus', 'Forster', 'Oswald', 'Radtke', 'Heim', 'Geisler', 'Appel', 'Weidner', 'Seidl', 'Moll', 'Dorn', 'Klemm', 'Barthel', 'Gabriel', 'Springer', 'Timm', 'Engels', 'Kretschmer', 'Reimer', 'Steinbach', 'Hensel', 'Wichmann', 'Eichler', 'Hecht', 'Winkelmann', 'Heise', 'Noll', 'Fleischmann', 'Neugebauer', 'Hinrichs', 'Schaller', 'Lechner', 'Brandl', 'Mack', 'Gebauer', 'Siegel', 'Zahn', 'Singer', 'Michels',
            'Schuler', 'Scholl', 'Uhlig', 'Brüggemann', 'Specht', 'Bürger', 'Eggert', 'Baumgartner', 'Weller', 'Schnell', 'Börner', 'Brauer', 'Kohler', 'Pfaff', 'Auer', 'Drescher', 'Otte', 'Frenzel', 'Petzold', 'Rother', 'Hagemann', 'Sattler', 'Wirtz', 'Ruf', 'Schirmer', 'Sauter', 'Schürmann', 'Junker', 'Walz', 'Dreyer', 'Sievers', 'Haller', 'Prinz', 'Stolz', 'Hausmann', 'Dick', 'Lux', 'Schnabel', 'Elsner', 'Kühl', 'Gerhardt', 'Klotz', 'Rabe', 'Schick', 'Faber', 'Riedl', 'Kranz', 'Fries', 'Reichelt', 'Rösch', 'Langner', 'Maaß', 'Wittig', 'Geier', 'Finke', 'Kasper', 'Maas', 'Bremer', 'Rath', 'Knapp', 'Dittmann', 'Kahl', 'Volk', 'Faust', 'Harder', 'Biermann', 'Pütz', 'Kempf', 'Mielke', 'Michaelis', 'Yilmaz', 'Abel', 'Thieme', 'Schütt', 'Hauck', 'Cordes', 'Eberle', 'Schaefer', 'Wehner', 'Haug', 'Fritzsche', 'Kilian', 'Eggers', 'Große', 'Matthes', 'Reinhold', 'Paulus', 'Dürr', 'Bohn', 'Thoma', 'Schober', 'Koller', 'Korn', 'Höhne', 'Hering', 'Gerdes', 'Ullmann', 'Jensen', 'Endres', 'Bernhard', 'Leonhardt', 'Eckhardt', 'Schaaf', 'Höfer', 'Junge', 'Rademacher', 'Pilz', 'Hellwig', 'Knorr', 'Helbig', 'Melzer', 'Lippert', 'Evers', 'Bahr', 'Klinger', 'Heitmann', 'Ehrhardt', 'Heinrichs', 'Horstmann', 'Behr', 'Stöhr', 'Drews', 'Rudolf', 'Sieber', 'Theis', 'Groth', 'Hecker', 'Weiler', 'Kemper', 'Rost', 'Lück', 'Claus', 'Hildebrand', 'Steinmetz', 'Götze', 'Trautmann', 'Blume', 'Kurth', 'Augustin', 'Nitsche', 'Janke', 'Jahnke', 'Klug', 'Damm', 'Heimann', 'Strauch', 'Schlosser', 'Uhl', 'Böhmer', 'Ries', 'Hellmann', 'Höhn', 'Hertel', 'Dreher', 'Borchert', 'Huth', 'Sperling', 'Just', 'Stenzel', 'Kunkel', 'Lau', 'Sprenger', 'Schönfeld', 'Pohlmann', 'Heilmann', 'Wacker', 'Lehner', 'Teichmann', 'Kaminski', 'Vogl', 'Gehrke', 'Hartl', 'Vogler', 'Schroeder', 'Thomsen', 'Nitschke', 'Engler', 'Liedtke', 'Wille', 'Starke', 'Friedrichs', 'Kirchhoff', 'Schwarze', 'Balzer', 'Reinhard', 'Heinen', 'Lotz', 'Küster', 'Kretzschmar', 'Schöne', 'Clemens', 'Hornung', 'Ulbrich', 'Renz', 'Hofer', 'Ruppert', 'Lohse', 'Schuh', 'Amann', 'Westermann', 'Stiller', 'Burmeister', 'Alt', 'Hampel', 'Brockmann', 'Wessel', 'Späth', 'Hoyer', 'Mader', 'Bartel', 'Rößler', 'Krieg', 'Grote', 'Schwarzer', 'Schweitzer', 'Scheer', 'Bosch', 'Zink', 'Roos', 'Wagener', 'Oppermann', 'Henze', 'Lehnert', 'Seemann', 'Trapp', 'Reiß', 'David', 'Pfeffer', 'Grau', 'Horst', 'Diekmann', 'Korte', 'Rehm', 'Wilde', 'Schleicher', 'Lampe', 'Grundmann', 'Veit', 'Daniel', 'Eisele', 'Hafner', 'Steinert', 'Sachs', 'Pfister', 'Kühnel', 'Schüller', 'Klatt', 'Bischof', 'Schwabe', 'Wendel', 'Tietz', 'Frick', 'Buschmann', 'Steinke', 'Menke', 'Baumeister', 'Kirschner', 'Loos', 'Ebner', 'Kastner', 'Wolters', 'Orth', 'Stange', 'Becher', 'Reinke', 'Brendel', 'Behnke', 'Schweiger', 'Kolbe', 'Schmidtke', 'Süß', 'Rühl', 'Gläser', 'Heider', 'Seibert', 'Heckmann', 'Reitz', 'Baumgart', 'Riemer', 'Helm', 'Knobloch', 'Wörner', 'Heyer', 'Nguyen', 'Baumgärtner', 'Grund', 'Brüning', 'Ostermann', 'Cremer', 'Schauer', 'Jacobi', 'Ewald', 'Fürst', 'Widmann', 'Otten', 'Büchner', 'Petri', 'Fritsche', 'Kock', 'Ehlert', 'Kleine', 'Eckstein', 'Hacker', 'Brandes', 'Buchner', 'Hagedorn', 'Keck', 'Häusler', 'Muth', 'Apel', 'Heuser', 'Bastian', 'Kersten', 'Stamm', 'Niemeyer', 'Berthold', 'Gehrmann', 'Weinert', 'Schatz', 'Hager', 'Volkmann', 'Michael', 'Wieczorek', 'Wilms', 'Burghardt', 'Schultze', 'Merten', 'Schwartz', 'Kling', 'Rode', 'Neu', 'Mende', 'Thies', 'Böttger', 'Schell', 'Spindler', 'Pabst', 'Grün', 'Weiland', 'Mühlbauer', 'Hanisch', 'Doll', 'Janzen', 'Adams', 'Hermes', 'Haack', 'Cramer', 'Spies', 'Stern', 'Kugler', 'Budde', 'Jakobs', 'Scheller', 'Rösler', 'Reiser', 'Jonas', 'Herr', 'Ebeling', 'Wulff', 'Pauli', 'Löhr', 'Lukas', 'Rahn', 'Sachse', 'Köhn', 'Backhaus', 'Mahler', 'Hille', 'Kowalski', 'Heidrich', 'Brück', 'Gottwald', 'Heidenreich', 'Baumgarten', 'Hamm', 'Körber', 'Kübler', 'Frisch', 'Hardt', 'Enders', 'Bräuer', 'Seidler', 'Küpper', 'Lauterbach', 'Zeidler', 'Eckardt', 'Kreuzer', 'Schiffer', 'Schaper', 'Gehring', 'Hannemann', 'Ortmann', 'Petry', 'Thiemann', 'Tiedemann', 'Grünewald', 'Johannsen', 'Scheel', 'Volz', 'Kunert', 'Dieckmann', 'Bormann', 'Obermeier', 'Knauer', 'Schaub', 'Eilers', 'Berner', 'Pahl', 'Reinecke', 'Herz', 'Henn', 'Brehm', 'Hoff', 'Resch', 'Ochs', 'Krohn', 'Lerch', 'Raabe', 'Ehrlich', 'Hack', 'Friedl', 'Reis', 'Rogge', 'Meurer', 'Thelen', 'Drechsler', 'Hölscher', 'Morgenstern', 'Sommerfeld', 'Ebel', 'Kellermann', 'Rupprecht', 'Post', 'Hillebrand', 'Hill', 'Paulsen', 'Grabowski', 'Bolz', 'Lorenzen', 'Welsch', 'Seibel', 'Kleinert', 'Schröer', 'Jaeger', 'Wächter', 'Boldt', 'Palm', 'Kratz', 'Reimers', 'Pusch', 'Exner', 'Dietze', 'Wüst', 'Andres', 'Heide', 'Kaya', 'Reichardt', 'Kummer', 'Metzner', 'Grube', 'Ewert', 'Grunwald', 'Habermann', 'Zorn', 'Fichtner', 'Emmerich', 'Mangold', 'Reif', 'Ahlers', 'Kästner', 'Küppers', 'Petermann', 'Stratmann', 'Sailer', 'Schuhmacher', 'Hoch', 'Struck', 'Buchmann', 'Rauscher', 'Lüdtke', 'Wendler', 'Dreier', 'Zöller', 'Bucher', 'Siegert', 'Finger', 'Hopf', 'Rieck', 'Friese', 'Hopp', 'Sahin', 'Henrich', 'Spengler']
department = ['Oberarzt', 'Fondsmanager', 'Anwalt', 'Tax Manager', 'Vertirebsingenieur', 'CEO',
              'CFO', 'Programmierer', 'Ingeneur', 'IT-Architekt', 'Architekt', 'Küchenhilfe', 'Kellner']
for x in range(1, 50001):
    fname = firstname[randint(0, (len(firstname) - 1))]
    lname = lastname[randint(0, (len(lastname) - 1))]
    dep = department[randint(0, (len(department) - 1))]
    userid = ''.join(random.choice(chars) for _ in range(6))
    user = {
        'firstname': fname,
        'lastname': lname,
        'id': userid,
        'department': dep,
        'email': fname + '.' + lname + '@13floor.de',
        'networks': [
            {
                'name': "10.1.2.0/24",
                'expire': "01.02.2022"
            },
            {
                'name': "10.4.2.0/24",
                'expire': "01.02.2022"
            },
            {
                'name': "100.67.58.0/24",
                'expire': "01.02.2022"
            },
            {
                'name': "172.16.80.0/20",
                'expire': "01.02.2022"
            },
        ],
        'zones': [
            {
                'name': "13floor.de",
                'rights': {
                    'a': 1,
                    'aaaa': 0,
                    'ptr': 1,
                    'cname': 1,
                    'srv': 0,
                    'mx': 0,
                    'txt': 0,
                    'host': 1
                },
                'expire': "01.02.2022",
                'view': 'default',
                'grid': 'external'
            },
            {
                'name': "de.13floor.de",
                'rights': {
                    'a': 1,
                    'aaaa': 0,
                    'ptr': 1,
                    'cname': 1,
                    'srv': 0,
                    'mx': 0,
                    'txt': 0,
                    'host': 1
                },
                'expire': "01.02.2022",
                'view': 'default',
                'grid': 'internal'
            },
            {
                'name': "ddi.13floor.de",
                'rights': {
                    'a': 1,
                    'aaaa': 0,
                    'ptr': 1,
                    'cname': 1,
                    'srv': 0,
                    'mx': 0,
                    'txt': 0,
                    'host': 1
                },
                'expire': "01.02.2022",
                'view': 'default',
                'grid': 'internal'
            },
        ],
        'groups': [
            {
                'name': "DDIADMIN",
                'expire': "01.02.2022"
            },
            {
                'name': "Feuerbach",
                'expire': "01.02.2022"
            },
            {
                'name': "Server",
                'expire': "01.02.2022"
            },
            {
                'name': "Client",
                'expire': "01.02.2022"
            },
        ],
        'records': [
            {
                'name': "www.13floor.de",
                'rights': {
                    'a': 1,
                    'aaaa': 0,
                    'ptr': 1,
                    'cname': 1,
                    'srv': 0,
                    'mx': 0,
                    'txt': 0,
                    'host': 1
                },
                'expire': "01.02.2022",
                'view': 'default',
                'grid': 'external'
            },
            {
                'name': "server.de.13floor.de",
                'rights': {
                    'a': 1,
                    'aaaa': 0,
                    'ptr': 1,
                    'cname': 1,
                    'srv': 0,
                    'mx': 0,
                    'txt': 0,
                    'host': 1
                },
                'expire': "01.02.2022",
                'view': 'server',
                'grid': 'external'
            },
            {
                'name': "ddiadmin.ddi.13floor.de",
                'rights': {
                    'a': 1,
                    'aaaa': 0,
                    'ptr': 1,
                    'cname': 1,
                    'srv': 0,
                    'mx': 0,
                    'txt': 0,
                    'host': 1
                },
                'expire': "01.02.2022",
                'view': 'default',
                'grid': 'internal'
            },
        ]
    }
    # Step 3: Insert business object directly into MongoDB via isnert_one
#    result = ddiadmindb.users.insert_one(user)
    # Step 4: Print to the console the ObjectID of the new document
#    print('Created {0} of 5000000 as {1}'.format(x, result.inserted_id))
# Step 5: Tell us that you are done
print('finished creating 5000000 business reviews')
end_time = time.time()
# for fivestar in ddiadmindb.users.find({"id": 'gy1tv1'}):
#    pprint.pprint(fivestar)
ASingleReview = users.find_one({"id": 'gy1tv1'})
print('A sample document:')
pprint.pprint(ASingleReview)


# ADD SINGEL RECORD TO ARRAY
result = users.update_one(
    {'_id': ASingleReview.get('_id')},
    {'$addToSet': {'zones': {'name': 'apac.13floor.de', 'expire': '02.02.2022',
                             'view': 'default', 'grid': 'internal', 'rights': {'a': 1, 'aaaa': 0, 'ptr': 1, 'cname': 1, 'srv': 0, 'mx': 0, 'txt': 0, 'host': 1}}}}
)
print('Number of documents modified : ' + str(result.modified_count))

UpdatedDocument = users.find_one({'_id': ASingleReview.get('_id')})
print('The updated document:')
pprint.pprint(UpdatedDocument)

UPDATE SINGLE RECORDS IN ARRAY
ASingleReview = users.find_one({"id": 'gy1tv1'})
print('A sample document:')
pprint.pprint(ASingleReview)

result = users.update_one(
    {'_id': ASingleReview.get('_id'), 'zones.name': 'apac.13floor.de'},
    {'$set': {"zones.$": {'name': 'emea.13floor.de', 'expire': '02.02.2022', 'view': 'default', 'grid': 'internal',
                          'rights': {'a': 1, 'aaaa': 0, 'ptr': 1, 'cname': 0, 'srv': 1, 'mx': 0, 'txt': 1, 'host': 0}}}}
)
print('Number of documents modified : ' + str(result.modified_count))

UpdatedDocument = users.find_one({'_id': ASingleReview.get('_id')})
print('The updated document:')
pprint.pprint(UpdatedDocument)

print("required time to calculate is :", end_time-start_time)
