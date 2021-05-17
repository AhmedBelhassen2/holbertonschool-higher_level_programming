#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    rtat = 0
  for c in range(0, list_length):
        try:
            rtat = my_list_1[c] / my_list_2[c]
        except TypeError:
            print("wrong type")
            rtat = 0
        except ZeroDivisionError:
            print("division by 0")
            rtat = 0
        except IndexError:
            print("out of range")
            rtat = 0
        finally:
            new_list.append(rtat)
    return new_list
