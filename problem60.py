# https://projecteuler.net/problem=60

from math import *

digit = lambda num,n: (num//10**n)%10

def pointsOnLayer(layer, subLayer, dim):
    points = []


def spread(num, dim):
    if (num, dim) == (3, 2):
        return [(1,2),(2,1)]

    assert num >= dim


def all3dig():
    return [ tuple([digit(i,n) for n in range(0,3)]) for i in range(0, 999)]

#pointsOnLayer(4,0,4)

points = all3dig()
points = [a for a in points if sum(a)==5]

for i in points:
    print(i)

#for j in range(0,dim):
#    points.append( tuple([point[(j+k)%dim] for k in range(0, dim)]) )
