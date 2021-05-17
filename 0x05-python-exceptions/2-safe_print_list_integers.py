def safe_print_list_integers(my_list=[], x=0):
    countx = 0
    for cx in range(0, x):
        try:
            print("{:d}".format(my_list[cx]), end="")
            countx += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
