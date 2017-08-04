#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numarg = len(argv)
    prevnum = 0
    for i in range (1, numarg):
        num = int(argv[i])
        num += prevnum
        prevnum = num
    print("{}".format(num))
