# Main Project File

from random import randint as r

geheimzahl = r(1, 100)
versuche = 0
print("Willkommen zum Zahlenratespiel!")
print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Kannst du sie erraten?")

while True:
    tipp = int(input("Gib deinen Tipp ein: "))
    versuche += 1
    if tipp < geheimzahl:
        print("Zu niedrig!")
    elif tipp > geheimzahl:
        print("Zu hoch!")
    else:
        print(f"Richtig! Du hast die Zahl in {versuche} Versuchen erraten.")
        break


