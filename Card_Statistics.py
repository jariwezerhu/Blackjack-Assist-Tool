import math
import random
import time


# TODO: The following code was planned to be used with a dynamic programming solution for the Perfect Sum problem.
#  However, I could only successfully program a non-dynamic solution, which has a time-value of 2^N, meaning it was
#  not efficient. I plan to still implement a dynamic solution in the future. Read about it in the documentation.
#
# standard_statistics = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
#
#
# def card_probability(card, deck):
#     """Calculates the odds of a specific card being drawn next"""
#     occurrence = deck.count(card)
#     deck_size = len(deck)
#     probability = occurrence / deck_size
#     return probability
#
#
# def deck_probability(deck):
#     """Calculates all card odds, returns them in a dictionary"""
#     deck_statistics = standard_statistics
#     for i in deck:
#         deck_statistics[i] = card_probability(i, deck)
#     return deck_statistics


def blackjack_prob_tostring(lst, improvement):
    full_deck_prob = lst[0]
    deck_prob = lst[1]
    print("\nBlackjack odds are {}, compared to full deck odds of {}\nOdd improvement: {} (higher is better)".format
          (deck_prob, full_deck_prob, improvement))


def sim_time():
    """Asks user how long to run simulations"""
    while True:
        try:
            secs = int(input("Enter the time limit for the simulation in seconds.\n"
                             "Increase for higher accuracy or press enter to keep default: "))
            return secs
        except ValueError:
            print("Default time limit (10 seconds) is being used")
            return 10


def blackjack_probability(deck, full_deck):
    """Calculates the odds of hitting blackjack and compares it to full deck odds. This calculation is made with this
    formula: Probability of a blackjack: (A * T) / C(R, 2), where A = remaining aces, T = remaining tens, C(R,
    2) is all combinations of 2 of the remaining cards in the deck.
    https://forums.saliu.com/blackjack-natural-odds-probability.html """
    probabilities = []

    # Full deck probability
    aces_remaining = full_deck.count(1)
    tens_remaining = full_deck.count(10)
    cards_remaining = len(full_deck)
    bj_probability_full = ((aces_remaining * tens_remaining) / math.comb(cards_remaining, 2))
    probabilities.append(bj_probability_full)

    # Current deck probability
    aces_remaining = deck.count(1)
    tens_remaining = deck.count(10)
    cards_remaining = len(deck)
    bj_probability = ((aces_remaining * tens_remaining) / math.comb(cards_remaining, 2))
    probabilities.append(bj_probability)
    return probabilities


def odd_improvement(lst):
    """Calculates the improvement of odds compared to their base values. The higher above 0, the more the odds
    improved from base-value. The lower under 0, the more the odds deteriorated. Used
    https://en.wikipedia.org/wiki/Logit as a source for this formula. """

    base_probability = lst[0]
    current_probability = lst[1]
    improvement = math.log(current_probability / (1 - current_probability)) - math.log(
        base_probability / (1 - base_probability))
    return improvement


def draw_random(hand, deck, mn=17):
    """Draws random cards until the mx is reached, default=17 for dealer. For a player this is gonna be the dealers
    result """
    total = sum(hand)
    ace_count = 0
    temp_deck = deck.copy()
    while total < mn:
        deal = random.choice(temp_deck)
        temp_deck.remove(deal)
        if deal == 1:
            if total + 11 <= 21:
                deal = 11
                ace_count += 1
        if total > 21 and ace_count > 0:
            ace_count -= 1
            total -= 10
        total += deal
    return total


def monte_carlo_dealer(hand, deck, time_limit):
    """Simple simulation to get close estimation of dealer's odds at each possibility."""
    # TODO: Compare results to full deck odds
    dealer_odds = {17: 0, 18: 0, 19: 0, 20: 0, 21: 0, "bust": 0}
    end_time = time.time() + (time_limit / 2)
    count = 0
    while time.time() <= end_time:
        count += 1
        total = draw_random(hand, deck)
        if total > 21:
            dealer_odds["bust"] += 1
            pass
        else:
            for i in dealer_odds:
                if total == i:
                    dealer_odds[i] += 1
                    pass

    for i in dealer_odds:
        dealer_odds[i] /= count

    return dealer_odds


def mcd_tostring(dealer_odds):
    """Turns the dealer odds into strings for the user to read"""
    print("\nDealer odds:")
    for i in dealer_odds:
        print("   {}: {}%".format(i, round((dealer_odds[i] * 100), 3)))


def monte_carlo_player(hand, deck, dealer_odds, time_limit):
    """Calculates the winning odds of the player when standing and when hitting by using a Monte Carlo simulation"""
    temp_hand = hand.copy()
    player_total = sum(hand)
    stand_odds = {"win": 0, "tie": 0, "lose": 0}
    hit_odds = {"win": 0, "tie": 0, "lose": 0, "bust": 0}

    # Calculates odds when standing
    for i in dealer_odds:
        if i == "bust":
            stand_odds["win"] += dealer_odds[i]
            pass
        elif i < player_total:
            stand_odds["win"] += dealer_odds[i]
            pass
        elif i == player_total:
            stand_odds["tie"] += dealer_odds[i]
            pass
        else:
            stand_odds["lose"] += dealer_odds[i]
            pass

    # Calculates odds when hitting
    end_time = time.time() + (time_limit / 2)
    count = 0
    for i in range(0, len(temp_hand)):
        if temp_hand[i] == 11:
            temp_hand[i] = 1
    while time.time() <= end_time:
        player_total = draw_random(temp_hand, deck, sum(temp_hand) + 1)
        if player_total > 21:
            hit_odds["bust"] += 1
            hit_odds["lose"] += 1
        else:
            for i in dealer_odds:
                if i == "bust":
                    hit_odds["win"] += dealer_odds[i]
                else:
                    if i < player_total:
                        hit_odds["win"] += dealer_odds[i]
                    elif i == player_total:
                        hit_odds["tie"] += dealer_odds[i]
                    elif i > player_total:
                        hit_odds["lose"] += dealer_odds[i]
        count += 1
    for i in hit_odds:
        hit_odds[i] /= count
    return stand_odds, hit_odds


def mcp_tostring(player_odds, position):
    """Puts the player's odds into strings for the user to read"""
    stand_odds = player_odds[0]
    hit_odds = player_odds[1]
    print("\nPlayer {}'s odds when standing:".format(position).ljust(40) + "Player {}'s odds when hitting: (does not "
                                                                           "work very well with aces)".format(
        position))
    for i in stand_odds:
        print("   Odds to {}: {}%".format(i, round((stand_odds[i] * 100), 3)).ljust(40)
              + "   Odds to {}: {}%".format(i, round((hit_odds[i] * 100), 3)))
    print("\nPlayer {}'s chance to bust when hitting: {}%".format(position, round((hit_odds["bust"] * 100), 3)))


def odds_tostring(mcd, mcp, position):
    """Combines the strings and gives a recommendation to the user"""
    mcd_tostring(mcd)
    mcp_tostring(mcp, position)
    if (mcp[1]["win"] + mcp[1]["tie"]) > 65:
        print("\nPlayer should hit or double")
        pass
    if mcp[1]["bust"] == 0:
        print("\nPlayer should hit")
        pass
    elif mcp[0]["lose"] < mcp[1]["lose"]:
        print("\nPlayer should stand")
        pass
    else:
        print("\nPlayer should hit")
