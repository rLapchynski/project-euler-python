# https://projecteuler.net/problem=59

import operator

with open('p059_cipher.txt') as file:
    cipher = [int(i) for i in file.readline().split(',')]

    maxSpaces, maxSpacesClearText = 0, []
    for passNum in range(0, 26*26*26):
        #ASCII lowercase characters start at 97='a'
        password = chr(97+(passNum/(26*26))%26) + chr(97+(passNum/(26))%26) + chr(97+passNum%26)
        #Repeat password for the length of cipher
        key = [ord(password[i%3]) for i in range(0, len(cipher))]
        #Element-wise XOR of key and cipher
        cleartext = map(operator.xor, key, cipher)

        #I figured spaces should be much more common in correct english than in random characters and that turned out correct
        numSpaces = cleartext.count(32)
        if numSpaces > maxSpaces:
            maxSpaces, maxSpacesClearText = numSpaces, cleartext

    print(''.join(map(chr, maxSpacesClearText)))
    print(sum(maxSpacesClearText))
