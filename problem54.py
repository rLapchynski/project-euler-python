# https://projecteuler.net/problem=54

V, S = 0, 1     # Define V and S to the indicies of Value and Suit in the card strings, so each can be accessed as card[S] and card[V]
POSSIBLE_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
POSSIBLE_SUITS = ['H', 'C', 'D', 'S']

getValues = lambda cards: [card[V] for card in cards]
getSuits = lambda cards: [card[S] for card in cards]

def rankHand(hand):

    values = getValues(hand)
    suits = getSuits(hand)
    rank = -1

    # Royal Flush (Ten, Jack, Queen, King, Ace, in same suit.)
    if len(set(suits)) == 1 and sorted(values) == ['A', 'J', 'K', 'Q', 'T']:
        rank = 0
    # Straight Fulsh (All cards are consecutive values of same suit.)
    elif len(set(suits)) == 1 and sorted(values) in [sorted(POSSIBLE_VALUES[x:x+5]) for x in range(0, len(POSSIBLE_VALUES)-4)]:
        rank = 1
    # Four of a Kind (Four cards of the same value.)
    elif values.count(max(values, key=values.count)) == 4:
        rank = 2
    # Full House (Three of a kind and a pair.)
    elif len(set(values)) == 2 and values.count(max(values, key=values.count)) == 3:
        rank = 3
    # Flush (All cards of the same suit.)
    elif len(set(suits)) == 1:
        rank = 4
    # Straight (All cards are consecutive values.)
    elif sorted(values) in [sorted(POSSIBLE_VALUES[x:x+5]) for x in range(0, len(POSSIBLE_VALUES)-4)]:
        rank = 5
    # Three of a Kind (Three cards of the same value.)
    elif len(set(values)) == 3 and values.count(max(values, key=values.count)) == 3:
        rank = 6
    # Two Pairs (Two different pairs.)
    elif len(set(values)) == 3 and values.count(max(values, key=values.count)) == 2:
        rank = 7
    # One Pair (Two cards of the same value.)
    elif len(set(values)) == 4 and values.count(max(values, key=values.count)) == 2:
        rank = 8
    # High Card (Highest value card.)
    else:
        rank = 9

    return (rank, [value for value in sorted(values, key=lambda value: POSSIBLE_VALUES.index(value))][4] )



with open('p054_poker.txt', 'r') as file:
    lines = [ [hands[:5], hands[5:]] for hands in [line.split() for line in file.readlines()] ]
    # Creates a list containing all the lines in the file where
    #   each line is a list containing hands where
    #       each hand is a list containing one two-character string for each card

    test = ['TC', 'TD', 'JC', 'QC', 'KC']
    print(rankHand(test))
