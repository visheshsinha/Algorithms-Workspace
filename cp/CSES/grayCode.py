"""
Problem: Gray Code
Source: https://cses.fi/problemset/task/2205
@Author: Vishesh Sinha
"""
def grayCode(n):

    N = int(pow(2, n) + 1)
    for _ in range(N):
        out = bin(_).replace("0b", "")
        out = convert_gray(out)
        out = str(out)
        _len = len(out)

        if _len < n:
            out = "0" * (n - _len) + out
            print(out)
        elif _len > n:
            out = out[_len:]
        else:
            print(out)

def convert_gray(binary):
    binary = int(binary, 2)
    binary ^= (binary >> 1)
    return bin(binary)[2:]



if __name__ == '__main__':
    n = int(input())
    grayCode(n)