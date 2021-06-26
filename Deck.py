# 1 = Ace, 10 = Jack, 10 = Queen, 10 = King
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
deck = deck * 4

# TODO: Add cut-card functionality


def initiate_deck():
    """Asks the user how many decks are in play and generates the shoe"""
    while True:
        try:
            deck_count = int(input("How many decks in play? (Max: 8)"))
            if not 0 < deck_count < 9:
                raise ValueError
            break
        except ValueError:
            print("Insert a valid count between 0 and 9")
    return sorted(deck * deck_count)
