#!/usr/bin/python3
for n in range(0, 90):
    if n == 89:
        print("{:02d}".format(n))
    elif n % 10 > n / 10:
        print("{:02d}".format(n), end=", ")
