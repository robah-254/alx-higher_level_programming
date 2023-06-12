#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in my_list[0:]:
        if i % 2 == 0:
            return my_list[i].append(True)
        else:
            return my_list[i].append(False)
