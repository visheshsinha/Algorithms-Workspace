"""
Problem: Bit Strings
Source: https://cses.fi/problemset/task/1617/
@Author: Vishesh Sinha
"""
def bitStrings(n):
    print((2<<(n-1))%int((1e9)+7))

if __name__ == '__main__':
    n = int(input())
    bitStrings(n)