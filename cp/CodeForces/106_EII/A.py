"""
Problem: Domino on Windowsill
Source: https://codeforces.com/contest/1499/problem/0
@Author: Vishesh Sinha
"""

def dominoW(_list, w, b):

    if w == 0 and b == 0:
        return "YES"
    
    n , k1, k2 = _list[0], _list[1], _list[2]

    _min = min(k1, k2)
    _max = max(k1, k2)
    _abs = abs(k1 - k2)

    w = w - _min
    b = b - (n - _max)

    if w == 0 and b == 0:
        return "YES"
    
    _ho = int(_abs // 2)

    if w <= _ho:
        w = 0
    if b <= _ho:
        b = 0
    
    if w == 0 and b == 0:
        return "YES"
    
    return "NO"

if __name__ == '__main__':
    test_cases = int(input())
    
    for _ in range(test_cases):

        _list = (input().split(' '))
        for i in range(0, len(_list)): 
            _list[i] = int(_list[i])

        _list_copy = _list
        
        _list = (input().split(' '))
        for i in range(0, len(_list)): 
            _list[i] = int(_list[i]) 
        
        w, b = _list[0], _list[1]

        print(dominoW(_list_copy, w, b))