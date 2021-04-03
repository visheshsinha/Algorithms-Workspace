"""
Problem: Numeral Spiral
Source: https://cses.fi/problemset/task/1071
@Author: Vishesh Sinha
"""

def numeralSpiral(y, x):
    M=max(y, x)
    return ((y - x) * ((-1)**M) + (M*M - M + 1))
        
if __name__ == '__main__':
    
    test_cases = int(input())

    for _ in range(test_cases):
        _list = (input().split(' '))
        for i in range(0, len(_list)): 
            _list[i] = int(_list[i]) 
        
        y, x = _list[0], _list[1]
        print(numeralSpiral(y, x))
