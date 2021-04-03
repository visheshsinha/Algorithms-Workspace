"""
Problem: Way Too Long Words
Source: https://codeforces.com/problemset/problem/71/A 
@Author: Vishesh Sinha
"""

def words(_str):
    _len = len(_str)

    if _len <= 10:
        print(_str)
    else:
        print(_str[0]+str(_len-2)+_str[-1])

if __name__ == '__main__':

    test_cases = int(input())

    for _ in range(test_cases):
        _str = input()
        words(_str)