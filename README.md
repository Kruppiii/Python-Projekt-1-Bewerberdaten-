# Python-Projekt-1-Bewerberdaten-
import random #benötigt für zufällige generierung von zahlen
import os #benötigt für os.linesep (seperiert zeilen)

m1 = int(1)
m2 = int(2)  #variablen für die zwei auswahlmöglichkeiten

print ("Wähle eine Option aus")d
print ("(1)Daten eingeben")
print ("(2)Daten ausgeben")
a = int(input()) #ausgabe der optionen und input des users

if a == m1: #erster teil der if-schleife, welcher die daten abfragt 
    
    vorname = input("Geben sie ihren Namen ein: ")
    nachname = input("Geben sie ihren Nachnamen ein: ")
    geschlecht = input("Sind sie männlich, weiblich oder divers?: ")
    straße = input("In welcher Straße wohnen sie?: ")
    hausnummer = input("Und wie lautet die Hausnummer?: ")
    plz = input("Geben sie ihre Postleitzahl an: ")
    stadt = input("In welcher Stadt leben sie?: ")
    geburtsdatum = input("Wann sind sie geboren? (DD.MM.YYYY): ")
    gehaltsvorstellung = input("Geben sie ihre Gehaltsvorstellungen an: ")
    vorstrafen = input("Haben sie Vorstrafen? (ja/nein): ") 

    id = int(random.uniform(1111, 9999)) #user id wird generiert
    
    print ("Ihre Bewerbernummer lautet:", id)
    

    filename = "%s.txt" % id
    file = open(filename, 'w') #textdatei mit bewerbernummer als name wird generiert und geöffnet
    
    str_vorname = str(vorname)
    str_nachname = str(nachname)
    str_geschlecht = str(geschlecht)
    str_straße = str(straße)
    str_hausnummer = str(hausnummer)
    str_plz = str(plz)
    str_stadt = str(stadt)
    str_geburtsdatum = str(geburtsdatum)
    str_gehaltsvorstellung = str(gehaltsvorstellung)
    str_vorstrafen = str(vorstrafen) #umwandlung der user eingaben in strings
    
    file.write(str_vorname + os.linesep)
    file.write(str_nachname + os.linesep)
    file.write(str_geschlecht + os.linesep)
    file.write(str_straße + os.linesep)
    file.write(str_hausnummer + os.linesep)
    file.write(str_plz + os.linesep)
    file.write(str_stadt + os.linesep)
    file.write(str_geburtsdatum + os.linesep)
    file.write(str_gehaltsvorstellung + os.linesep)
    file.write(str_vorstrafen + os.linesep) #speichern der user eingaben in einem textdokument mit zeilenabstand
    
    
    
    
    
elif a == m2: #zweite option der if schleife
    n = input("Bitte geben sie ihre Bewerbernummer ein:") #abfrage der bewerbernummer um datei zu öffnen
    bewerber = "%s.txt" % n  #variable mit bewerbernummer wird als dateiname eingesetzt
    daten = open(bewerber, 'r')
    inhalt = daten.readlines()
    l = [x.strip() for x in inhalt]  #liest dokument zeile für zeile und fasst zeilen in eine liste zusammen
    
    print ("Ihr Name lautet", l[0], l[2])
    print ("Sie sind", l[4])
    print ("Ihre Adresse ist", l[6], l[8], "in", l[10], l[12])
    print ("Sie sind geboren am", l[14])
    print ("Ihre Gehaltsvorstellung beträgt", l[16])
    print ("Vorstrafen:", l[18]) #ausgabe der zuvor angegebenen daten
    
    

    
else: #dritte option der if-schleife, falls eine zahl >2 ausgewählt wird
    print ("Fehler")

