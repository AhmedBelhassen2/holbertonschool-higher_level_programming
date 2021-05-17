def safe_print_list(my_list=[], x=0):
    countx = 0
    try:
        for cx in range(0, x):
            print("{}".format(my_list[cx]), end="")
            countx += 1
        print()
    except:
        print()
        return countx
    return countx
