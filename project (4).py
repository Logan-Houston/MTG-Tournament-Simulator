import random
import csv


class Player:
    def __init__(
        self,
    ):
        decks = []
        with open("metagame.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                decks.append(row)
        Meta_Share = []
        for deck in decks:
            meta = deck.get("Meta Share")
            Meta_Share.append(float(meta))
        self._deck = random.choices(decks, weights=Meta_Share, k=1)[0]

    def __str__(self):
        return self.deck.get("Deck Name")

    @property
    def deck(self):
        return self._deck


# Simulates a single elimination MTG tournament with the specified number of players, using a preexisting .csv file of metagame information
# prints a list of the decks wiht the number of occurances, followed by the overall winnercd project
def main():
    decks = []
    player_decks = []
    with open("metagame.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            decks.append(row)
    Players = Generate_Players(int(input("Number of players in Tournament :").strip()))
    for i in range(0, len(Players)):
        player_decks.append(Players[i].deck.get("Deck Name"))
    print("Decks: ")
    for deck in decks:
        print(f"{deck.get('Deck Name')} : {player_decks.count(deck.get('Deck Name'))}")

    winner = Tournament(Players)[0]
    print(f"Winner! {winner}")


# Generates n number of player objects in a list and returns the list
# Raises a ValueError if n is not an even, positive integer greater than 2
def Generate_Players(n):
    if (isinstance(n, int)) == False:
        raise ValueError("Number of players must be an even positive integer greater than 0")
    if (n % 2) != 0:
        raise ValueError("Number of players must be an even positive integer greater than 0")
    if n <= 0:
        raise ValueError("Number of players must be an even positive integer greater than 0")
    players = []
    for _ in range(0, n):
        players.append(Player())
    return players


# compares the winrate of the deck of Player A against Player B, then randomly chooses a winner based on that winrate and returns the winner
def Play_match(A, B):
    players = [A, B]
    winrate_A = A.deck.get("Win Rate vs " + str(B))
    winrate_B = B.deck.get("Win Rate vs " + str(A))
    winner = random.choices(players, weights=[float(winrate_A), float(winrate_B)], k=1)
    return winner


# pairs players against each other in single elimination until 1 remains
def Tournament(participants):
    while len(participants) > 1:
        half_length = len(participants) // 2
        participants_A, participants_B = (
            participants[:half_length],
            participants[half_length:],
        )
        for i in range(0, len(participants_A)):
            winner = Play_match(participants_A[i], participants_B[i])[0]
            if participants_A[i] == winner:
                participants.remove(participants_B[i])
            else:
                participants.remove(participants_A[i])
    return participants


if __name__ == "__main__":
    main()
