#!/usr/bin/python3
for j in range(9):
    for i in range(j + 1, 10):
        if j * 10 + i < 89:
            print("{:d}{:d}".format(j, i), end=", ")
print("{:d}".format(89))
