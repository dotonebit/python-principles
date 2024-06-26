"""
Write a function named capital_indexes. The function takes a single parameter,
which is a string. Your function should return a list of all the indexes 
in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""

def capital_indexes(str):
    cap_index = []
    for i in range(len(str)):
        if str[i].isupper():
            cap_index.append(i)
    return cap_index