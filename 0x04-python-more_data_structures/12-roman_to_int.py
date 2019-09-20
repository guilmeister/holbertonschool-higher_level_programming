#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    dic = {'I': 1,
           'V': 5,
           'X': 10,
           'L': 50,
           'C': 100,
           'D': 500,
           'M': 1000}
    total = 0
    for x in range(len(roman_string)):
        s1 = dic[roman_string[x]]
        if (x + 1 < len(roman_string)):
            s2 = dic[roman_string[x + 1]]
            if (s1 >= s2):
                total = total + s1
            else:
                total = total + (s2 - s1)
        else:
            total = total + s1
    return total
