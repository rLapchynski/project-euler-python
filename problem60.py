# https://projecteuler.net/problem=60

from math import *


def points_on_layer(layer, dim):

    if dim == 1:
        return [[layer]]
    else:
        points = []
        for z in range(0, layer+1):
            for point in points_on_layer(layer-z, dim-1):
                points.append([z] + point)
        return points

        # return [(([z]+point) for point in points_on_layer(layer-z, dim-1)) for z in range(0, layer+1)]


















