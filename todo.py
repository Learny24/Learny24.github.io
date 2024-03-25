class Aufgabe():    
    def __init__(self,titel, beschreibung, fälligkeitsdatum, status):
        self.titel = titel
        self.beschreibung = beschreibung
        self.fälligkeitsdatum = fälligkeitsdatum
        self.status = status     


class Liste():
    def __init__(self):
        self.task_list = []

    def neueAufgabe(self, task):
        self.task_list.append(task)
    
    def hinzufügen(self):
        titel = input("Gebe den Titelnamen ein: ")
        beschreibung = input("Gebe die Beschreibung ein: ")
        fälligkeitsdatum = input("Wann ist die Deadline?: ")
        self.neueAufgabe(Aufgabe(titel,beschreibung,fälligkeitsdatum,"ausstehend"))

    def liste_anzeigen(self):        
        for index, task in enumerate(self.task_list, start=1):
            print(f"{index}. {task.titel} Status: {task.status}")

    def erledigt(self):
        titel = input("Welche Aufgabe wurde erledigt?:")
        for task in self.task_list:
            if titel == task.titel:
                task.status = "erledigt" 
        print("Folgende Aufgabe wurde erledigt:",titel)


    def details(self):
        titel = input("Welche Aufgabe möchtest du anzeigen?:")
        for task in self.task_list:
            if titel == task.titel:
                print("Titel:", task.titel)
                print("Beschreibung:", task.beschreibung)
                print("Fälligkeitsdatum:", task.fälligkeitsdatum)
                print("Status:", task.status) 

    def offene_anzeigen(self):
        counter = 1
        for task in self.task_list:       
            if task.status == "ausstehend":
                print(f"{counter}. {task.titel}") 
                counter += 1

    def erledigte_anzeigen(self):
        counter = 1
        for task in self.task_list:       
            if task.status == "erledigt":
                print(f"{counter}. {task.titel}") 
                counter += 1 

    def speichern(self, dateiname):
        with open(dateiname, "w", encoding="utf-8") as datei:            
            for task in self.task_list:
                datei.write(f"{task.titel},{task.beschreibung},{task.fälligkeitsdatum},{task.status}\n")

    def laden(self, dateiname):
        with open(dateiname, "r", encoding="utf-8") as datei:
            for zeile in datei:
                titel, beschreibung, fälligkeitsdatum, status = zeile.strip().split(",")
                self.neueAufgabe(Aufgabe(titel,beschreibung,fälligkeitsdatum, status))


      

liste = Liste()
liste.laden("todolist.txt")
start = True

while start:   
    print("""
    1. Aufgabe hinzufügen
    2. Aufgabe erledigt
    3. Offene ToDos anzeigen
    4. Details anzeigen
    5. Erledigte Aufgaben anzeigen
    6. Alle Aufgaben anzeigen
    8. Speichern
    9. Beenden""")
    option = input()
    if option == "1":
        #aufgabe_hinzufügen()        
        liste.hinzufügen()
    elif option == "2":
        liste.erledigt()
    elif option == "3":
        liste.offene_anzeigen()
    elif option == "4":
        liste.details()
    elif option == "5":
        liste.erledigte_anzeigen()
    elif option == "6":
        liste.liste_anzeigen()
    elif option == "8":
        liste.speichern("todolist.txt")
    elif option == "9":
        start = False
        

    

