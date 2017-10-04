# https://projecteuler.net/problem=58

from utilities import isPrime

# Return the corners of layer n, indexed from 1 is the central 1
def corners(num):
    if(num == 1): return [1]
    return sorted([pow(num*2-1,2)-(num-1)*i*2 for i in range(0,4)])

numPrime, layer = 3, 2
while float(numPrime)/float(4*layer-3) > 0.1:
    layer += 1
    numPrime += sum([isPrime(i) for i in corners(layer)])

print((layer-1)*2+1)
