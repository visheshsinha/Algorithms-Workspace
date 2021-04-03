"""
Problem: Trailing Zeros
Source: https://cses.fi/problemset/task/1618
@Author: Vishesh Sinha
"""

def trailingZeros(n):
    flag = 0
    while True:
        if n>=5:
            flag+=n//5
            n = n//5
        else:
            break
    print(flag)
         

if __name__ == '__main__':
    n = int(input())
    trailingZeros(n)