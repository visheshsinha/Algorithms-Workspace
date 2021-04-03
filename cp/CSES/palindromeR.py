"""
Problem: Palindrome Reorder
Source: https://cses.fi/problemset/task/1754
@Author: Vishesh Sinha
"""
from collections import Counter, OrderedDict

def palindromeReorder(_str):
    freq = dict(Counter(_str))
    _str = ""

    freq = dict(sorted(freq.items(), key=lambda item: item[1]))
    freq = OrderedDict(reversed(list(freq.items())))

    flag = 0

    for _, (ch, f) in enumerate(freq.items()):
        f = int(f)
        if f % 2 == 0:
            _str += ch*int(f/2)

    for _, (ch, f) in enumerate(freq.items()):
        f = int(f)
        if f % 2 != 0:
            flag += 1
            _str += ch*f
    
    
    freq = OrderedDict(reversed(list(freq.items())))
    
    for _, (ch, f) in enumerate(freq.items()):
        f = int(f)
        if f % 2 == 0:
            _str += ch*int(f/2)
        
    if flag > 1:
        print("NO SOLUTION")
    else:
        print(_str)

if __name__ == '__main__':
    _str = input()
    palindromeReorder(_str)