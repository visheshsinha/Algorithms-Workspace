"""
Problem: Coin Piles
Source: https://cses.fi/problemset/task/1754
@Author: Vishesh Sinha
"""

def coinPiles(a, b):
    if (min(a, b)*2 >= max(a, b)) and (a+b) % 3 == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        _list = (input().split(' '))
        for i in range(0, len(_list)): 
            _list[i] = int(_list[i]) 
        
        a, b = _list[0], _list[1]
        print(coinPiles(a, b))