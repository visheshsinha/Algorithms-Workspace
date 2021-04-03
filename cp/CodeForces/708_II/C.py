"""
Problem: k-LCM
Source: https://m1.codeforces.com/contest/1497/problem/C1
@Author: Vishesh Sinha
"""

from math import gcd

def LCM(_list):
    lcm = 1
    for i in _list[1:]:
        lcm = lcm*i//gcd(lcm, i)
    return lcm


def k_LCM(n): 
  
    count = 0
    for i in range(1, n-1): 
        for j in range(1, n-1): 
            for k in range(1, n-1): 
                if(i + j + k == n): 
                    if LCM([i, j, k]) <= n/2:
                        print(i, j, k)
                        return 0

"""
def solve(n):
    a1, a2 = 1, 1

    if n % 3 == 0:
        a1, a2 = int(n / 3), int(n / 3)
        print(a1, a2, a1)
        return 0
    a1 = int(n / 3)
    a2 = int(n - 2 * a1)

    if (a1 == 0):
        a1 = a1 + 1
    if (a2 == 0):
        a2 = a2 + 1

    if (((a1 * a2) / gcd(a1, a2)) > n / 2):
        a1 = n - 2 * a2
        print(a1, a2, a2)
    else:
        print(a1, a1, a2)
"""


if __name__ == '__main__':

    test_cases = int(input())
    
    for _ in range(test_cases):

        _list = (input().split(' '))
        for i in range(0, len(_list)): 
            _list[i] = int(_list[i])

        k_LCM(_list[0])
        