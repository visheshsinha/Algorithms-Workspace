"""
Problem: Repetions
Source: https://cses.fi/problemset/task/1069
@Author: Vishesh Sinha
"""

def repetions(seq):
    _l = len(seq)
    rep = 1
    counter = 1

    for _ in range(_l - 1):
        if seq[_+1] == seq[_]:
            counter += 1
        else:
            counter = 1
        
        if counter > rep:
            rep = counter

    print(rep)        

if __name__ == '__main__':
    seq = input()
    repetions(seq)