"""
Problem: Weird Algorithm
Source: https://cses.fi/problemset/task/1068
@Author: Vishesh Sinha
"""

def weirdAlgorithm(n):
    while True:
        print(n, end=' ')
        
        if (n == 1):
            break

        if (n%2 == 0):
            n = int(n/2)
        else:
            n = n*3 + 1
        

if __name__ == '__main__':
    n = int(input())
    weirdAlgorithm(n)