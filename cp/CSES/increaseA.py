"""
Problem: Increasing Array 
Source: https://cses.fi/problemset/task/1094
@Author: Vishesh Sinha
"""

def increaseA(n):
    _list = (input().split(' '))
    for i in range(0, len(_list)): 
        _list[i] = int(_list[i])
    
    total = 0
    m = _list[0]

    for i in range(len(_list)):
        total += max({0, (m - _list[i])})
        m = max(m, _list[i])

    print(total)        
    
         

if __name__ == '__main__':
    n = int(input())
    increaseA(n)