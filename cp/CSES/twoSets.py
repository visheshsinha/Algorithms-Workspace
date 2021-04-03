"""
Problem: Two Sets 
Source: https://cses.fi/problemset/task/1092
@Author: Vishesh Sinha
"""

def bitMultiply(n, m):
    count, ans = 0, 0
    while True:
        if m % 2 == 1:
            ans += n << count
        count += 1
        m = m >> 1
        if m == 0:
            break 
    return ans


def twoSets(n):  
    sum = bitMultiply(n, n+1) >> 1
    if sum % 2 != 0:
        print('NO')
    else:
        print('YES')
        sum = sum >> 1
        set1 = []
        set2 = []

        while True:
            if (sum - n >= 0):
                set1.append(n)
                sum -= n
            else:
                set2.append(n)
            n -= 1
            if (n==0):
                break
        print(len(set1))
        for _ in range(len(set1)):
            print(int(set1[_]), end=" ")
        print()
        print(len(set2))
        for _ in range(len(set2)):
            print(int(set2[_]), end=" ")

if __name__ == '__main__':
    n = int(input())
    twoSets(n)