#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numarg = len(argv)
    print("{}".format(numarg - 1), end="")
    if numarg == 1:
        print(" argument.")
    elif numarg == 2:
        print(" argument:")
    else:
        print(" arguments:")
    for i in range(1, numarg):
        print("{}: {}".format(i, argv[i]))
