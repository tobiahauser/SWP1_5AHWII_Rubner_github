class Knoten:
    def __init__(self, data=None):
        self.data = data
        self.next = None  # Verweis auf den nächsten Knoten

    def __str__(self):
        return str(self.data)

class EinfacheVerketteteListe:
    def __init__(self):
        self.head = None  # Verweis auf den ersten Knoten

    def append(self, data):  # Neuer Knoten am Ende der Liste
        if isinstance(data, int):  # keine Ganzzahl --> wird nicht hinzugefügt
            if not self.head:
                self.head = Knoten(data)  # Liste leer -->, neuer Knoten wird zum ersten Knoten der Liste
            else:  # Knoten wird am Ende der Liste angehängt
                knoten = self.head
                while knoten.next:  # bis zum letzten Knoten
                    knoten = knoten.next
                knoten.next = Knoten(data)  # neuer Knoten wird hinzugefügt
        else:
            print(f"Listenelement ({data}) wurde nicht hinzugefügt, da es keine Ganzzahl ist!")

    def length(self):
        anzahl = 0
        knoten = self.head  # erster Knoten
        while knoten:
            anzahl += 1
            knoten = knoten.next  # nächster Knoten
        return anzahl

    def __iter__(self):  # gibt die Datenwerte der Knoten zurück
        knoten = self.head
        while knoten:
            yield knoten.data  # gibt die Daten nach jedem Schleifendurchgang zurück, ohne die Methode zu beenden
            knoten = knoten.next

    def __str__(self):
        liste = []
        knoten = self.head
        while knoten:
            liste.append(str(knoten.data))  # hinzufügen zur Liste
            knoten = knoten.next
        return ' --> '.join(liste)  # Zeichenkette mit Pfeilen

if __name__ == '__main__':
    vl = EinfacheVerketteteListe()
    vl.append(10)
    vl.append(23)
    vl.append(35)
    vl.append(100)
    vl.append(3685)
    vl.append("H")
    vl.append("K")
    vl.append("HALLO")

    print("Alle Listenelemente, welche Erfolgreich hinzugefügt wurden:")
    for i in vl:
        print(i)
    print(vl.__str__())
    print("Die Liste beinhaltet " + str(vl.length()) + " Einträge")
