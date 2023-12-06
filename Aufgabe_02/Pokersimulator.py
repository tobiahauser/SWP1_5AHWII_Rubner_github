import random
from tabulate import tabulate

#Beispiel für count:
values = [2, 4, 6, 2, 8, 10, 4]
for p in values:
    if values.count(p) == 2:
        print("Paar")
    else:
        print("Kein Paar")

colors = ["Kreuz","Pik","Herz","Karo"]
#Bube = 11
#Dame = 12
#König = 13
#Ass = 14
cards = [2,3,4,5,6,7,8,9,10,11,12,13,14]
#print(colors)
#print(cards)

gamecards = []

for color in colors:
    for card in cards:
        gamecards.append((color,card))

#print(gamecards)

def pickOneCard(cards, anz_Karten):
    copy_cards = cards.copy()
    random.shuffle(copy_cards)
    picked_cards = []
    for i in range(anz_Karten):
        zug = random.randint(0, len(copy_cards) - 1 - i)
        picked_card = copy_cards.pop(zug)
        picked_cards.append(picked_card)
    return picked_cards

def pairs(cards):
    counter = 0
    values = [card[1] for card in cards]
    one_counter = 0
    for p in values:
        if values.count(p) == 2:  #zählt wie oft p in der Liste vorkommt und ob es 2 entspricht
            one_counter += 1
            if one_counter == 2: #(bei einem Paar 2 mal)
                counter += 1
                return counter #Es wurde ein Paar gefunden
    return counter


def twopairs(cards):
    counter = 0
    values = [card[1] for card in cards]
    two_counter = 0
    for p in values:
        if values.count(p) == 2:  #zählt wie oft p in der Liste vorkommt und ob es 2 entspricht
            two_counter += 1
            if two_counter == 4: #(bei zwei Paaren 4 mal)
                counter += 1
                return counter #Es wurden zwei Paare gefunden
    return counter

def drilling(cards):
    counter = 0
    values = [card[1] for card in cards]
    for p in values:
        if values.count(p) == 3: #zählt wie oft p in der Liste vorkommt und ob es 3 entspricht
            counter += 1
            return counter #Es wurde ein Drilling gefunden
    return counter

def street(cards):
    counter = 0
    values = [card[1] for card in cards]
    for p in values:
        if all(values[p + 1] == values[p] + 1 for p in range(len(values) - 1)):  #ChatGPT
            counter += 1
            return counter #Es wurde eine Straße gefunden
    return counter

def flush(cards):
    counter = 0
    values = [card[0] for card in cards]
    for a in values:
        if values.count(a) == 5: #zählt wie oft p in der Liste vorkommt und ob es 5 entspricht
            counter += 1
            return counter #Es wurde ein Flush gefunden
    return counter

def fullhouse(cards):
    counter = 0
    values = [card[1] for card in cards]
    for p in values:
        if values.count(p) == 3 and pairs(cards) == 1:  #schaut ob ein Drilling und ein Paar in der Liste vorkommt
            counter += 1
            return counter  #Es wurde ein FullHouse gefunden
    return counter

def fourofakind(cards):
    counter = 0
    values = [card[1] for card in cards]
    for p in values:
        if values.count(p) == 4: #zählt wie oft p in der Liste vorkommt und ob es 4 entspricht
            counter += 1
            return counter #Es wurde ein Vierling gefunden
    return counter

def straightflush(cards):
    counter = 0
    values = [card[0] for card in cards]
    for a in values:
        if values.count(a) == 5:  #schaut ob 5 Karten der gleichen Farbe vorhanden sind (card[0])
            values2 = [card[1] for card in cards]
            for p in values2:
                if all(values2[p + 1] == values2[p] + 1 for p in range(len(values2) - 1)):  # ChatGPT
                    counter += 1
                    return counter  #Es wurde ein StraightFlush gefunden
    return counter

def royalflush(cards):
    counter = 0
    values = [card[0] for card in cards]
    for a in values:
        if values.count(a) == 5:  #schaut ob 5 Karten der gleichen Farbe vorhanden sind (card[0])
            values2 = [card[1] for card in cards]
            sorted_values = sorted(values2, reverse=True)  # Sortiere die Werte absteigend
            royal_flush_values = [10, 11, 12, 13, 14]
            if sorted_values[:5] == royal_flush_values:
                counter += 1
                return counter  #Es wurde ein RoyalFlush gefunden
    return counter

def highcard(cards):
    counter = 0
    if not any([pairs(cards), twopairs(cards), drilling(cards),
        street(cards), flush(cards),
        fullhouse(cards), fourofakind(cards),
        straightflush(cards), royalflush(cards)]): #Keine Kombination kommt vor
        counter += 1
        return counter  #Es wurde eine HighCard gefunden
    return counter

play = 100000 #Spiele 100000 mal
highcard_counter = 0
pair_counter = 0
twopairs_counter = 0
drilling_counter = 0
street_counter = 0
flush_counter = 0
fullhouse_counter = 0
fourofakind_counter = 0
straightflush_counter = 0
royalflush_counter = 0

for _ in range(play):
    random_cards = pickOneCard(gamecards, 5) #Hole 5 Zufallszahlen
    sorted_cards = sorted(random_cards, key=lambda x: x[1]) #Katen sortieren
    highcard_counter += highcard(sorted_cards)
    twopairs_counter += twopairs(sorted_cards)
    if twopairs(sorted_cards) == 0:
        pair_counter += pairs(sorted_cards)
    drilling_counter += drilling(sorted_cards)
    street_counter += street(sorted_cards)
    flush_counter += flush(sorted_cards)
    fullhouse_counter += fullhouse(sorted_cards)
    fourofakind_counter += fourofakind(sorted_cards)
    straightflush_counter += straightflush(sorted_cards)
    royalflush_counter += royalflush(sorted_cards)

    if _ == play - 1:
        table_data = [
            ["HighCard", highcard_counter, highcard_counter/play * 100, "50,12"],
            ["Paar", pair_counter, pair_counter/play * 100, "42,26"],
            ["ZweiPaar", twopairs_counter, twopairs_counter/play * 100, "4,75"],
            ["Drilling", drilling_counter, drilling_counter/play * 100, "2,11"],
            ["Straße", street_counter, street_counter/play * 100, "0,392"],
            ["Flush", flush_counter, flush_counter/play * 100, "0,197"],
            ["FullHouse", fullhouse_counter, fullhouse_counter/play * 100, "0,144"],
            ["Vierling", fourofakind_counter, fourofakind_counter/play * 100, "0,0240"],
            ["StraightFlush", straightflush_counter, straightflush_counter/play * 100, "0,00139"],
            ["RoyalFlush", royalflush_counter, royalflush_counter/play * 100, "0,000154"],
            ["Spielzuege", play],
        ]
        headers = ["Kombination", "Anzahl", "Prozentsatz (berechnet)", "Prozentsatz (Wikipedia)"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
