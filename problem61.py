
from utilities import *


# The indices on which each type 4 digits long, inclusive.
# Triangular:   44 to 139
# Square:       31 to 98
# Pentagonal:   25 to 80
# Hexagonal:    22 to 69
# Heptagonal:   20 to 62
# Octagonal:    18 to 57

def remove_not_begins_with(num, excluded):
    # Removes all numbers in polys that don't begin with the last two digits of num and removes all excluded lists
    polys = [[polygonal_num(3, i) for i in range(44, 140)],
              [polygonal_num(4, i) for i in range(31, 99)],
              [polygonal_num(5, i) for i in range(25, 81)],
              [polygonal_num(6, i) for i in range(22, 70)],
              [polygonal_num(7, i) for i in range(20, 63)],
              [polygonal_num(8, i) for i in range(18, 58)]]
    for i in [a for a in range(0, 6) if a not in excluded]:
        for comp_num in list(polys[i]):
            if not comp_num//100 == num%100:
                polys[i].remove(comp_num)
    for i in excluded:
        for a in list(polys[i]):
            polys[i].remove(a)

    return polys


def chain(poss_next, excluded, curr_chain):
    if len(curr_chain) == 6 and curr_chain[5]%100 == curr_chain[0]//100:
        print(sum(curr_chain))
        exit()
    for next_dim in [a for a in range(0, 6) if a not in excluded]:
        for next_num in poss_next[next_dim]:
            chain(remove_not_begins_with(next_num, excluded + [next_dim]), excluded + [next_dim], curr_chain + [next_num])


for i in [polygonal_num(8, i) for i in range(18, 58)]:
    possNext = remove_not_begins_with(i, [5])
    chain(possNext, [5], [i])
