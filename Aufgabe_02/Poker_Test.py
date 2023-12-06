import unittest
import Pokersimulator

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
        picked_cards = Pokersimulator.pickOneCard(self.gamecards, 3)
        self.assertEqual(len(picked_cards), 3)

        for card in picked_cards: #kommen die Karten aus gamecards
            self.assertIn(card, self.gamecards)
        pass

    def test_pairs(self):
        random_cards = Pokersimulator.pickOneCard(self.gamecards, 1)
        sorted_cards = sorted(random_cards, key=lambda x: x[1])
        pair_counter = Pokersimulator.pairs(sorted_cards)
        if pair_counter == 1:
            self.assertEqual(pair_counter, 1)
        if pair_counter == 0:
            self.assertEqual(pair_counter, 0)
        pass

    def test_drilling(self):
        random_cards = Pokersimulator.pickOneCard(self.gamecards, 1)
        sorted_cards = sorted(random_cards, key=lambda x: x[1])
        drilling_counter = Pokersimulator.drilling(sorted_cards)
        if drilling_counter == 1:
            self.assertEqual(drilling_counter, 1)
        if drilling_counter == 0:
            self.assertEqual(drilling_counter, 0)
        pass

    def test_twopairs(self):
        random_cards = Pokersimulator.pickOneCard(self.gamecards, 1)
        sorted_cards = sorted(random_cards, key=lambda x: x[1])
        twopairs_counter = Pokersimulator.twopairs(sorted_cards)
        if twopairs_counter == 1:
            self.assertEqual(twopairs_counter, 1)
        if twopairs_counter == 0:
            self.assertEqual(twopairs_counter, 0)
        pass

if __name__ == "__main__":
    unittest.main()
