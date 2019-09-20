#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = 0
    if not a_dictionary:
        return None
    else:
        for x in a_dictionary.keys():
            if max_score < a_dictionary[x]:
                max_score = a_dictionary[x]
        for y in a_dictionary:
            if a_dictionary[y] == max_score:
                return y
