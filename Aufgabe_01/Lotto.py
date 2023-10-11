import random

def Liste(wert):
    return list(range(1, wert + 1))


def Woerterbuch(wert):
    woerterbuch = {}
    for i in range(1, wert + 1):
        woerterbuch[i] = 0
    return woerterbuch


def Lottoziehung(liste, anz_Ziehungen):
    for i in range(anz_Ziehungen):
        zug = random.randint(0, len(liste) - 1 - i)
        liste[zug], liste[len(liste) - 1 - i] = liste[len(liste) - 1 - i], liste[zug]
    return liste[-anz_Ziehungen:]


def hinzufuegenZuListe(woerterbuch, liste):
    for i in liste:
        woerterbuch[i] += 1
    return woerterbuch


for i in range(1000):
    hinzufuegenZuListe(Woerterbuch(45), Lottoziehung(Liste(45), 6))
    print(Lottoziehung(Liste(45), 6))
