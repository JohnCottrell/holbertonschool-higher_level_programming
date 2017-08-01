#!/usr/bin/python3
for one in range(97, 123):
    if one == 101 or one == 113:
        continue
    print("{:c}".format(one), end="")
