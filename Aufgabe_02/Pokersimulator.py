import random
import unittest

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

def pairs(cards, counter):
    values = [card[1] for card in cards]
    for p in values:
        if values.count(p) == 2: #zählt wie oft ein Paar in der Liste vorkommt
            counter += 1
            return True, counter #Es wurde ein Paar gefunden
    return False, counter

def drilling(cards, counter):
    values = [card[1] for card in cards]
    for p in values:
        if values.count(p) == 3: #zählt wie oft ein Drilling in der Liste vorkommt
            counter += 1
            return True, counter #Es wurde ein Drilling gefunden
    return False, counter

def street(cards, counter):
    values = [card[1] for card in cards]
    for p in values:
        if all(values[p + 1] == values[p] + 1 for p in range(len(values) - 1)):  #ChatGPT
            counter += 1
            return True, counter # Eswurde eine Straße gefunden
    return False, counter

def flush(cards,counter):
    values = [card[0] for card in cards]
    for a in values:
        if values.count(a) == 5: #zählt wie oft ein Flush in der Liste vorkommt
            counter += 1
            return True, counter #Es wurde ein Flush gefunden
    return False, counter

def fullhouse(cards,counter):
    values = [card[1] for card in cards]
    for p in values:
        if values.count(p) == 3 and pairs(cards,counter)[0]:  #schaut ob ein Drilling und ein Paar in der Liste vorkommt
            counter += 1    #pairs(cards, counter)[0] schaut ob ein Paar vorhanden ist (True,False) gibt nicht den Counter-Wert zurück
            return True, counter  #Es wurde ein FullHouse gefunden
    return False, counter

def fourofakind(cards, counter):
    values = [card[1] for card in cards]
    for p in values:
        if values.count(p) == 4: #zählt wie oft ein Vierling in der Liste vorkommt
            counter += 1
            return True, counter #Es wurde ein Vierling gefunden
    return False, counter

def straightflush(cards, counter):
    values = [card[0] for card in cards]
    for a in values:
        if values.count(a) == 5:  #schaut ob 5 Karten der gleichen Farbe vorhanden sind
            values2 = [card[1] for card in cards]
            for p in values2:
                if all(values2[p + 1] == values2[p] + 1 for p in range(len(values2) - 1)):  # ChatGPT
                    counter += 1
                    return True, counter  #Es wurde eine Straße gefunden
    return False, counter

def royalflush(cards, counter):
    values = [card[0] for card in cards]
    for a in values:
        if values.count(a) == 5:  #schaut ob 5 Karten der gleichen Farbe vorhanden sind
            values2 = [card[1] for card in cards]
            sorted_values = sorted(values2, reverse=True)  # Sortiere die Werte absteigend
            royal_flush_values = [10, 11, 12, 13, 14]
            if sorted_values[:5] == royal_flush_values:
                counter += 1
                return True, counter  #Es wurde ein RoyalFlush gefunden
    return False, counter

def highcard(cards,counter):
    if not any([pairs(cards, 0)[0], drilling(cards, 0)[0],
        street(cards, 0)[0], flush(cards, 0)[0],
        fullhouse(cards, 0)[0], fourofakind(cards, 0)[0],
        straightflush(cards, 0)[0], royalflush(cards, 0)[0]]): #Keine Kombination kommt vor
        counter += 1
        return True, counter  #Es wurde eine HighCard gefunden
    return False, counter

class TestKartenspiel(unittest.TestCase):
    gamecards = []

    @classmethod
    def setUpClass(self):
        colors = ["Kreuz", "Pik", "Herz", "Karo"]
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        for color in colors:
            for card in cards:
                self.gamecards.append((color, card))

    def test_pickOneCard(self):
        picked_cards = pickOneCard(self.gamecards, 3)
        self.assertEqual(len(picked_cards), 3)

        for card in picked_cards: #kommen die Karten aus gamecards
            self.assertIn(card, self.gamecards)
        pass

    def test_pairs(self):
        random_cards = pickOneCard(self.gamecards, 1)
        sorted_cards = sorted(random_cards, key=lambda x: x[1])
        pair_combination, pair_counter = pairs(sorted_cards,0)
        if pair_combination:
            self.assertTrue(pair_combination)
            self.assertEqual(pair_counter, 1)
        if pair_combination == 0:
            self.assertFalse(pair_combination)
            self.assertEqual(pair_counter, 0)
        pass

    def test_drilling(self):
        random_cards = pickOneCard(self.gamecards, 1)
        sorted_cards = sorted(random_cards, key=lambda x: x[1])
        drilling_combination, drilling_counter = drilling(sorted_cards, 0)
        if drilling_combination:
            self.assertTrue(drilling_combination)
            self.assertEqual(drilling_counter, 1)
        if drilling_combination == 0:
            self.assertFalse(drilling_combination)
            self.assertEqual(drilling_counter, 0)
        pass

if __name__ == "__main__":
    unittest.main()

play = 100000
highcard_counter = 0
pair_counter = 0
drilling_counter = 0
street_counter = 0
flush_counter = 0
fullhouse_counter = 0
fourofakind_counter = 0
straightflush_counter = 0
royalflush_counter = 0

for _ in range(play):
    random_cards = pickOneCard(gamecards, 5)
    sorted_cards = sorted(random_cards, key=lambda x: x[1])
    #print(sorted_cards)
    #print("RandomCards: ", random_cards)
    #print("GameCards: ", gamecards)
    highcard_combination, highcard_counter = highcard(sorted_cards, highcard_counter)
    pair_combination, pair_counter = pairs(sorted_cards, pair_counter)
    drilling_combination, drilling_counter = drilling(sorted_cards, drilling_counter)
    street_combination, street_counter = street(sorted_cards, street_counter)
    flush_combination, flush_counter = flush(sorted_cards, flush_counter)
    fullhouse_combination, fullhouse_counter = fullhouse(sorted_cards, fullhouse_counter)
    fourofakind_combination, fourofakind_counter = fourofakind(sorted_cards, fourofakind_counter)
    straightflush_combination, straightflush_counter = straightflush(sorted_cards, straightflush_counter)
    royalflush_combination, royalflush_counter = royalflush(sorted_cards, royalflush_counter)

print("HighCard_Kombinationen: ", highcard_counter)
print("Paar_Kombinationen: ", pair_counter)
print("Drilling_Kombinationen: ", drilling_counter)
print("Street_Kombinationen: ", street_counter)
print("Flush_Kombinationen: ", flush_counter)
print("FullHouse_Kombinationen: ", fullhouse_counter)
print("Vierling_Kombinationen: ", fourofakind_counter)
print("StraightFlush_Kombinationen: ", straightflush_counter)
print("RoyalFlush_Kombinationen: ", royalflush_counter)
print("Spielzuege: ", play)
print("prozentueller Anteil für eine HighCard: " + str(highcard_counter/play * 100) + " %")
print("prozentueller Anteil für eine HighCard bei 5 Karten (Wikipedia): 50,12 %")
print("prozentueller Anteil für ein Paar: " + str(pair_counter/play * 100) + " %")
print("prozentueller Anteil für ein Paar bei 5 Karten (Wikipedia): 42,26 %")
print("prozentueller Anteil für einen Drilling: " + str(drilling_counter/play * 100) + " %")
print("prozentueller Anteil für einen Drilling bei 5 Karten (Wikipedia): 2,11 %")
print("prozentueller Anteil für eine Straße: " + str(street_counter/play * 100) + " %")
print("prozentueller Anteil für eine Straße bei 5 Karten (Wikipedia): 0,392 %")
print("prozentueller Anteil für einen Flush: " + str(flush_counter/play * 100) + " %")
print("prozentueller Anteil für einen Flush bei 5 Karten (Wikipedia): 0,197 %")
print("prozentueller Anteil für ein FullHouse: " + str(fullhouse_counter/play * 100) + " %")
print("prozentueller Anteil für ein FullHouse bei 5 Karten (Wikipedia): 0,144 %")
print("prozentueller Anteil für einen Vierling: " + str(fourofakind_counter/play * 100) + " %")
print("prozentueller Anteil für einen Vierling bei 5 Karten (Wikipedia): 0,0240 %")
print("prozentueller Anteil für einen StraightFlush: " + str(straightflush_counter/play * 100) + " %")
print("prozentueller Anteil für einen StraightFlush bei 5 Karten (Wikipedia): 0,00139 %")
print("prozentueller Anteil für einen RoyalFlush: " + str(royalflush_counter/play * 100) + " %")
print("prozentueller Anteil für einen RoyalFlush bei 5 Karten (Wikipedia): 0,000154 %")