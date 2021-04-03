"""
Problem: Strange Table
Source: https://codeforces.com/contest/1506/problem/A
@Author: Vishesh Sinha
"""

def strangeTable(_list):
    n, m, x = _list[0], _list[1], _list[2]
    
    if n*m == x:
        return x
    
    _temp_1 = x // n
    _temp_2 = x % n

    return (((_temp_2-1)*m) + _temp_1 + 1)
    

if __name__ == '__main__':

    test_cases = int(input())
    
    for _ in range(test_cases):

        _list = (input().split(' '))
        for i in range(0, len(_list)): 
            _list[i] = int(_list[i])

        print(strangeTable(_list))