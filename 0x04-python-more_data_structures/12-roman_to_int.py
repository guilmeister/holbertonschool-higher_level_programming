#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    total = 0
    cmp_last = 0
    for x in roman_string[::-1]:
        total = total - roman[x] if roman[x] < cmp_last else total + roman[x]
        cmp_last = roman[x]
    return total
