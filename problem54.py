# https://projecteuler.net/problem=54

V, S = 0, 1     # Define V and S to the indicies of Value and Suit in the card strings, so each can be accessed as card[S] and card[V]
POSSIBLE_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
POSSIBLE_SUITS = ['H', 'C', 'D', 'S']

getValues = lambda cards: [card[V] for card in cards]
getSuits = lambda cards: [card[S] for card in cards]

def rankHand(hand):

    values = getValues(hand)
    suits = getSuits(hand)
    maxValue = sorted(values, key=lambda value: POSSIBLE_VALUES.index(value))[4]

    # Return is a tupule containing the rank of the hand and the highest card that makes up the rank

    # Royal Flush (Ten, Jack, Queen, King, Ace, in same suit.)
    if len(set(suits)) == 1 and sorted(values) == ['A', 'J', 'K', 'Q', 'T']:
        return (0, 'A')
    # Straight Fulsh (All cards are consecutive values of same suit.)
    elif len(set(suits)) == 1 and sorted(values) in [sorted(POSSIBLE_VALUES[x:x+5]) for x in range(0, len(POSSIBLE_VALUES)-4)]:
        return (1, maxValue)
    # Four of a Kind (Four cards of the same value.)
    elif values.count(max(values, key=values.count)) == 4:
        return (2, max(values, key=values.count))
    # Full House (Three of a kind and a pair.)
    elif len(set(values)) == 2 and values.count(max(values, key=values.count)) == 3:
        return (3, max(values, key=values.count))
    # Flush (All cards of the same suit.)
    elif len(set(suits)) == 1:
        return (4, maxValue)
    # Straight (All cards are consecutive values.)
    elif sorted(values) in [sorted(POSSIBLE_VALUES[x:x+5]) for x in range(0, len(POSSIBLE_VALUES)-4)]:
        return (5, maxValue)
    # Three of a Kind (Three cards of the same value.)
    elif len(set(values)) == 3 and values.count(max(values, key=values.count)) == 3:
        return (6, max(values, key=values.count))
    # Two Pairs (Two different pairs.)
    elif len(set(values)) == 3 and values.count(max(values, key=values.count)) == 2:
        return (7, max({x for x in values if x != min(values, key=values.count)}, key=lambda value: POSSIBLE_VALUES.index(value)))
    # One Pair (Two cards of the same value.)
    elif len(set(values)) == 4 and values.count(max(values, key=values.count)) == 2:
        return (8, max(values, key=values.count))
    # High Card (Highest value card.)
    else:
        return (9, maxValue)

def compareHighCard(hand1, hand2):
    for c1, c2 in reversed(zip(sorted(getValues(hand1), key=lambda value: POSSIBLE_VALUES.index(value)), sorted(getValues(hand2), key=lambda value: POSSIBLE_VALUES.index(value)))):
        if POSSIBLE_VALUES.index(c1) > POSSIBLE_VALUES.index(c2):
            return 1
        elif POSSIBLE_VALUES.index(c1) < POSSIBLE_VALUES.index(c2):
            return 2




with open('p054_poker.txt', 'r') as file:
    lines = [ [hands[:5], hands[5:]] for hands in [line.split() for line in file.readlines()] ]
    # Creates a list containing all the lines in the file where
    #   each line is a list containing hands where
    #       each hand is a list containing one two-character string for each card

    p1wins = 0
    for line in lines:
        h1, h2 = rankHand(line[0]), rankHand(line[1])
        print h1, h2
        if h1[0] > h2[0]:
            p1wins += 1
        elif h1[0] == h2[0] and POSSIBLE_VALUES.index(h1[1]) > POSSIBLE_VALUES.index(h2[1]):
            p1wins += 1
        elif h1 == h2 and compareHighCard(line[0], line[1]) == 1:
            p1wins += 1


    print p1wins
