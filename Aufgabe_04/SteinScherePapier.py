import random

from matplotlib import pyplot as plt


def person_picked(input: str):
    input = input.lower()
    if (input == "rock"):
        return 2
    if (input == "paper"):
        return 3
    if (input == "scissors"):
        return 4
    if (input == "spock"):
        return 0
    if (input == "lizard"):
        return 1
    return None

def computer_picked(input):
    if (input == 2):
        return "rock"
    if (input == 3):
        return "paper"
    if (input == 4):
        return "scissors"
    if (input == 0):
        return "spock"
    if (input == 1):
        return "lizard"
    return None

def pick_person():
    print("Bitte hier eingeben (rock, paper, scissors, spock, lizard): ")
    eingabe = input()
    if eingabe in person_symbol:
        person_symbol[eingabe] += 1
    pick = person_picked(eingabe)
    while (pick is None):
        print("Eingabe fehlgeschlagen!")
        print("Bitte hier eingeben (rock, paper, scissors, spock, lizard): ")
        eingabe = input()
        pick = person_picked(eingabe)
    print(pick)
    return pick

def pick_computer():
    print("Computer-Wahl: ")
    random_number = random.randint(0,4)
    pick = computer_picked(random_number)
    print(pick)
    print(random_number)
    return random_number

def game():
    person = pick_person()
    computer = pick_computer()
    if (person == computer):
        print("Unentschieden!")
        return "unentschieden"
    if (person+2)%5 == computer or (person-1)%5 == computer:
        print("Person hat gewonnen!")
        return "person"
    else:
        print("Computer hat gewonnen!")
        return "computer"

def statistic():
    spieler = list(win_count.keys())
    gewinne = list(win_count.values())

    plt.bar(spieler, gewinne, color=['blue', 'red', 'green'])
    plt.xlabel('Spieler')
    plt.ylabel('Anzahl der Gewinne')
    plt.title('Gewinnstatistik')
    plt.show()

    # Visualisiere die Symbolstatistik
    symbole = list(person_symbol.keys())
    anzahl_symbole = list(person_symbol.values())

    plt.bar(symbole, anzahl_symbole, color='purple')
    plt.xlabel('Symbole')
    plt.ylabel('Anzahl der ausgewählten Symbole')
    plt.title('Menschengewählte Symbole-Statistik')
    plt.show()

if __name__ == "__main__":
    play = 0
    rounds = 10
    win_count = {"person": 0, "computer": 0, "unentschieden": 0}
    person_symbol = {"rock": 0, "paper": 0, "scissors": 0, "spock": 0, "lizard": 0}
    while play < rounds:
        play += 1
        winner = game()
        if winner in win_count:
            win_count[winner] += 1

        print("Aktuelle Gewinnstatistik:")
        for spieler, anzahl in win_count.items():
            print(f"{spieler}: {anzahl}")

        print("\nMenschengewählte Symbol-Statistik:")
        for symbol, anzahl in person_symbol.items():
            print(f"{symbol}: {anzahl}")

    print("Spiel beendet!")
    print("Endgültige Gewinnstatistik:")
    for spieler, anzahl in win_count.items():
        print(f"{spieler}: {anzahl}")

    print("\nEndgültige meschengewählte Symbole-Statistik:")
    for symbol, anzahl in person_symbol.items():
        print(f"{symbol}: {anzahl}")

    statistic()

