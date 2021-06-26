def initiate_players():
    """Asks the user how players are at the table. User should be able to change this at any time."""
    while True:
        try:
            player_count = int(input("How many players? (Max: 7)"))
            if not 0 < player_count < 8:
                raise ValueError
            break
        except ValueError:
            print("Insert a valid between 0 and 8")
    players = [[] for _ in range(0, player_count)]
    return players


def draw_card(deck, hand):
    """Asks the player which card the dealer draws and removes it from the deck if valid. This value is then used in
    calculations """  # TODO: Automate in future using "RAIN MAN 2.0"
    while True:
        card = (input("What card was drawn:").lower())
        if card == "":
            return "end"
        if card in ["king", "queen", "jack", "k", "q", "j"]:
            card = 10
        if card in ["ace", "a"]:
            card = 1
        try:
            if card == '0':
                return "end"
            if 0 < int(card) < 11:
                card = int(card)
                if card in deck:
                    deck.remove(card)
                    if card == 1:
                        card = 11
                    hand.append(card)
                    break
                else:
                    print("That card should not be available in the deck. Make sure you are playing with the correct "
                          "amount of decks and that you have been keeping track of the cards properly. The card has "
                          "NOT been removed from the deck.")
                    continue
            else:
                raise ValueError
        except ValueError:
            print("Please select a valid card. This can be any card that's found in a deck. (i.e. 8, Ace, 3, jack)")
            continue


def action(hand, hit_count):
    """Asks for player's action. First checks compatibility, then returns string of chosen action."""
    while True:
        if sum(hand) == 21:
            print("Player stands with 21")
            pass
        if len(hand) == 2:
            if hit_count == 0 and hand[0] == hand[1]:
                player_action = input('Choose: "Hit", "Stand", "Double", "Split":').lower()
                try:
                    if player_action in ["hit", "stand", "double", "split"]:
                        return player_action
                    else:
                        raise ValueError
                except ValueError:
                    print('Please choose between "Hit", "Stand", "Double", "Split".')
        if hit_count == 0 or len(hand) == 1:
            player_action = input('Choose: "Hit", "Stand", "Double":').lower()
            try:
                if player_action in ["hit", "stand", "double"]:
                    return player_action
                else:
                    raise ValueError
            except ValueError:
                print('Please choose between "Hit", "Stand", "Double".')
        else:
            player_action = input('Choose: "Hit", "Stand":').lower()
            try:
                if player_action in ["hit", "stand"]:
                    return player_action
                else:
                    raise ValueError
            except ValueError:
                print('Please choose between "Hit", "Stand".')


def check_bust(hand):
    """Checks if player gets Blackjack. Checks if player busts. Ends his turn if he stands."""
    if sum(hand) == 21:
        print("Player stands with 21")
        return True
    if sum(hand) > 21:
        if 11 in hand:
            hand[hand.index(11)] = 1
        else:
            print("Player busts")
            return True


def dealer_draw(deck, hand):
    """Draws dealer's cards until he busts or stands"""
    print("\nDealer's turn:")
    while sum(hand) < 17:
        print("Dealer has {} (total: {})".format(hand, sum(hand)))
        card = draw_card(deck, hand)
        if card == "end":
            break
        if sum(hand) > 21:
            if 11 in hand:
                hand[hand.index(11)] = 1
                pass
            print("Dealer has bust with a total of {}\n".format(sum(hand)))
        elif sum(hand) > 16:
            print("Dealer stands with a total of {}\n".format(sum(hand)))


def round_start(players, deck, dealer_cards):
    """Sets up the round: User inputs every player's initial cards and the dealer's card"""
    count = 1
    for i in range(0, len(players)):
        # User inserts cards drawn per player TODO: Automate in future using "RAIN MAN 2.0"
        print("\nPlayer {}'s first card:".format(count))
        draw_card(deck, players[i])
        print("Player {}'s second card:".format(count))
        draw_card(deck, players[i])
        if sum(players[i]) == 21:
            print("Blackjack!")
        if players[i][0] == 11 and players[i][1] == 11:
            players[i][0] = 1
        count += 1
    print("\nDealer's hand:")
    draw_card(deck, dealer_cards)


def turn(deck, position, hand, hit_count=0):
    """Continues the round: User inputs every player's play; and dealer's result"""
    print("\nPlayer {} has {} (total: {})".format(position, hand, sum(hand), position))
    # User inserts player's action
    if sum(hand) == 21:
        return "end"
    act = action(hand, hit_count)
    if act == "hit":
        draw_card(deck, hand)
        if check_bust(hand):
            return "end"
    elif act == "stand":
        return "end"
    elif act == "double":
        draw_card(deck, hand)
        return "end"
    elif act == "split":
        return "split"
