"""
Problem: Binary Removals
Source: https://codeforces.com/contest/1499/problem/B
@Author: Vishesh Sinha
"""

"""
1 < = a_1 < a_2 < ⋯ < a_k < = |s|
a_(i−1) + 1 < a_i

"""

    
def binaryR(_str):
    _len = len(_str)


if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        _str = input()

        print(binaryR(_str))