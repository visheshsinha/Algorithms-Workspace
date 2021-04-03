"""
Problem: Primility check
@Author: Vishesh Sinha
"""

from divisors import divisors

if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        div = divisors(n)
        if len(div) == 2:
            print("PRIME")
        else:
            print("NOT PRIME")