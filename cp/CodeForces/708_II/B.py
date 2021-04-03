"""
Problem: M-arrays
Source: https://codeforces.com/contest/1497/problem/B
@Author: Vishesh Sinha
"""

def m_Arrays(n , m, _list):

    dp = [[0 for i in range(500)] 
			for i in range(500)]
    
    


if __name__ == '__main__':

    test_cases = int(input())
    
    for _ in range(test_cases):

        _list = (input().split(' '))
        for i in range(0, len(_list)): 
            _list[i] = int(_list[i]) 
        
        n, m = _list[0], _list[1]

        _list = (input().split(' '))
        for i in range(0, len(_list)): 
            _list[i] = int(_list[i])

        m_Arrays(n, m, _list)
        