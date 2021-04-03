"""
Problem: Watermelon
Source: https://codeforces.com/problemset/problem/4/A 
@Author: Vishesh Sinha
"""

def watermelon(n):
    if n%2 != 0 or n == 2 or n == 1 or n == 0:
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':

    n = int(input())
    watermelon(n)
        