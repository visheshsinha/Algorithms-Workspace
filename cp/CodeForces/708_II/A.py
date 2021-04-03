"""
Problem: Meximization
Source: https://codeforces.com/contest/1497/problem/0
@Author: Vishesh Sinha
"""

def meximization(n, _list):
    _list.sort()


    seen = set()
    l = 0
    r = 0
    while True:
        # advance `r` to the next not-yet-seen number
        while r < len(_list) and _list[r] in seen:
            r += 1
        if r == len(_list): break
        # add the number to the set
        seen.add(_list[r])
        # swap arr[l] with arr[r]
        _list[l], _list[r] = _list[r], _list[l]
        # advance `l`
        l += 1
    
    for i in range(len(_list)):
        print(_list[i], end=" ")
    
    print()


if __name__ == '__main__':

    test_cases = int(input())
    
    for _ in range(test_cases):

        n = int(input())

        _list = (input().split(' '))
        for i in range(0, len(_list)): 
            _list[i] = int(_list[i])

        meximization(n, _list)
        