"""
Problem: Interesting XOR
Source: https://www.codechef.com/MARCH21B/problems/IRSTXOR
@Author: Vishesh Sinha
"""

import math

def interestingXOR(C):
    A = pow(2, (C.bit_length() - 1)) -1
    B = C^A
    print(A*B)

if __name__ == '__main__':
    for _ in range(int(input())):
        C = int(input())
        interestingXOR(C)