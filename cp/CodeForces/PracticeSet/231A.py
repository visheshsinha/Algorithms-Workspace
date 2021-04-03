"""
Problem: Team
Source: https://codeforces.com/problemset/problem/231/A 
@Author: Vishesh Sinha
"""

def team(_list):
    if sum(_list) >= 2:
        return True
    else:
        return False

if __name__ == '__main__':

    test_cases = int(input())

    count = 0

    for _ in range(test_cases):
        _list = (input().split(' '))
        for i in range(0, len(_list)): 
            _list[i] = int(_list[i])
        
        if team(_list):
            count += 1
    
    print(count)
