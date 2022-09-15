import random #benötigt für zufällige generierung von zahlen
import os #benötigt für os.linesep (seperiert zeilen)


m1 = int(1)
m2 = int(2)  #variablen für die zwei auswahlmöglichkeiten


print ("Wähle eine Option aus")
print ("(1)Daten eingeben")
print ("(2)Daten ausgeben")
a = int(input()) #ausgabe der optionen und input des users


if a == m1: #erster teil der if-schleife, welcher die daten abfragt 
    
    
    x = 0
    eingabe = []
    fragen = ["Geben sie ihren Namen ein: ", "Geben sie ihren Nachnamen ein: ", "Sind sie männlich, weiblich oder divers?: ", "In welcher Straße wohnen sie?: ", "Und wie lautet die Hausnummer?: ", "Geben sie ihre Postleitzahl an: ", "In welcher Stadt leben sie?: ", "Wann sind sie geboren? (DD.MM.YYYY): ", ("Geben sie ihre Gehaltsvorstellungen an: "), "Haben sie Vorstrafen? (ja/nein): "]


    while x < 10: #aktion wird 10 mal ausgeführt
    
        print(fragen[x]) #ruft die jeweilige frage ab
        i = input() #benutzereingabe 
        eingabe.append(i) #fügt eingabe ans ende der leeren liste, also platz 0
        x+=1 #erhöht x um 1, sodass die schleife 10 mal läuft
        
                                   
    id = int(random.uniform(1111, 9999)) #user id wird generiert 
    print ("Ihre Bewerbernummer lautet:", id)
    filename = "%s.txt" % id
    
    
    with open(filename, 'w') as file: #textdatei mit bewerbernummer als name wird generiert und geöffnet
         
         
        for platz in eingabe: #führt aktion für jeden platz in der liste aus
            
            
            file.write(platz + os.linesep)
        
     
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

