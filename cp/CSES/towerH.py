"""
Problem: Tower of Hanoi
Source: https://cses.fi/problemset/task/2165
@Author: Vishesh Sinha
"""

"""
Reference : https://www.hackerearth.com/blog/developers/tower-hanoi-recursion-game-algorithm-explained/
"""


def towerOfHanoi(n, _from, _aux, _to):
    if n == 1:
        print(_from, _to)
    else:
        towerOfHanoi(n-1, _from, _to, _aux)
        print(_from, _to)
        towerOfHanoi(n-1, _aux, _from, _to)


if __name__ == '__main__':
    n = int(input())
    moves = int(pow(2, n) - 1)
    print(moves)
    towerOfHanoi(n, "1", "2", "3")