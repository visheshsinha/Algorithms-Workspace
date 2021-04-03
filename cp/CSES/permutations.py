"""
Problem: Permutations 
Source: https://cses.fi/problemset/task/1094
@Author: Vishesh Sinha
"""

def permutations(n):

    if n == 1:
        print("1")
    elif(n < 4):
        print("NO SOLUTION")
    elif(n == 4):
        print("2 4 1 3\n")
    else:
        i = 2
        for _ in range(n):
            if(i > n):
                break       
            print(i)
            i += 2

        i = 1
        for _ in range(n):
            if(i > n):
                break
            print(i)
            i += 2

            
if __name__ == '__main__':
    n = int(input())
    permutations(n)