#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for s in range(1, len(sys.argv)):
        result += int(sys.argv[s])
    print("{}".format(result))
