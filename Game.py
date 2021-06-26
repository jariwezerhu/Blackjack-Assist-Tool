import Player
import Deck
import Card_Statistics


def game():
    """Runs the game"""
    deck = Deck.initiate_deck()
    full_deck = deck.copy()
    players = Player.initiate_players()
    time_limit = Card_Statistics.sim_time()
    while True:
        Card_Statistics.blackjack_prob_tostring(Card_Statistics.blackjack_probability(deck, full_deck),
                                                Card_Statistics.odd_improvement(
                                                    Card_Statistics.blackjack_probability(deck, full_deck)))
        dealer = []
        Player.round_start(players, deck, dealer)
        position = 1
        hit_count = 0
        for hand in players:
            while True:
                mcd = Card_Statistics.monte_carlo_dealer(dealer, deck, time_limit)
                mcp = Card_Statistics.monte_carlo_player(hand, deck, mcd, time_limit)
                Card_Statistics.odds_tostring(mcd, mcp, position)
                turn = Player.turn(deck, position, hand, hit_count)
                if turn == "split":
                    hand_1 = [hand[0]]
                    hand = [hand[1]]
                    while True:
                        mcp = Card_Statistics.monte_carlo_player(hand_1, deck, mcd, time_limit)
                        Card_Statistics.odds_tostring(mcd, mcp, position)
                        if Player.turn(deck, position, hand_1, hit_count) == "end":
                            hit_count = 0
                            break
                        mcd = Card_Statistics.monte_carlo_dealer(dealer, deck, time_limit)
                        hit_count += 1
                if turn == "end":
                    hit_count = 0
                    break
                hit_count += 1
            position += 1
            hand.clear()
        Player.dealer_draw(deck, dealer)
