"""
Problem: LCM & GCD
@Author: Vishesh Sinha
"""
def GCD(n, m):
    if n == 0:
        return m
    return GCD(m % n, n)

def LCM(n, m):
    return (n*m // GCD(n, m))


if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        n, m = map(int, input().split())

        print(f"GCD: {GCD(n, m)}, LCM: {LCM(n, m)}")