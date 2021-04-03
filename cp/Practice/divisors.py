"""
Problem: Divisors
@Author: Vishesh Sinha
"""

from math import *

def divisors(n):
    
    div = []
    for _ in range(1, int(sqrt(n)) + 1):
        if n % _ == 0:
            div.append(_)
            div.append(n // _)
    div.sort()
    return div

if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        print("Divisors:", *divisors(n))