"""
Problem: Two Knights 
Source: https://cses.fi/problemset/task/1072
@Author: Vishesh Sinha
"""

def twoKnights(n):
    for _i in range(n):
        safe = int((_i + 1)*(_i + 1) * ((_i + 1)*(_i + 1) - 1) / 2) - (4 * ((_i + 1) - 1) * ((_i + 1) - 2))
        print(safe)

if __name__ == '__main__':
    n = int(input())
    twoKnights(n)