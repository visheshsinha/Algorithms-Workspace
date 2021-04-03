"""
Problem: Missing Number 
Source: https://cses.fi/problemset/task/1083
@Author: Vishesh Sinha
"""

def missingNumber(n):
    counter = [0] * n
    
    _list = (input().split(' '))

    for i in range(0, len(_list)): 
        _list[i] = int(_list[i]) 
    
    for _ in range(n-1):
        temp = _list[_]
        counter[temp-1] += 1
    
    missing = counter.index(min(counter)) + 1
    print(missing)
        

if __name__ == '__main__':
    n = int(input())
    missingNumber(n)