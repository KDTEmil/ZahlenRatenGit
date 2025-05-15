# Main Project File

#This is a change Maxi made

from random import randint as r

def zahlenratespiel():
    geheimzahl = r(1, 100)
    versuche = 0
    print("Willkommen zum Zahlenratespiel!")
    print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Kannst du sie erraten?")

    while True:
        try:
            tipp = int(input("Gib deinen Tipp ein: "))
            versuche += 1
            if tipp < geheimzahl:
                print("Zu niedrig!")
            elif tipp > geheimzahl:
                print("Zu hoch!")
            else:
                print(f"Richtig! Du hast die Zahl in {versuche} Versuchen erraten.")
                break
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")

zahlenratespiel()
