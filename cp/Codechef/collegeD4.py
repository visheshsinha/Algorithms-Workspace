"""
Problem : College Life 4
Source : https://www.codechef.com/problems/COLGLF4
@Author : Vishesh Sinha
"""

def calculate(_list):
    N, E, H, A, B, C = _list
    temp_E = E
    temp_H = H
    
    if min(A, B, C) == C:
        if E==H:
            if E >= N:
                print(C*N)
            else:
                print("-1")
        elif E>H:
            temp = E-H
            if H >= N:
                print(C*N)
            elif (H + int(temp/2)) >= N:
                print(H*C +(N-H)*A)
            else:
                print("-1")
        else:
            temp=H-E
            if E >= N:
                print(C*N)
            elif (E + int(temp/3)) >= N:
                print(E*C +(N-E)*B)
            else:
                print("-1")
    elif min(A, B, C) == B:
        if int(H/3) >= N:
            print(B*N)
        else:
            if min(A,C) == C:
                if int(H%3) != 0 and E != 0 and E >= H%3:
                    if int(H/3) + int(H%3) >= N:
                        print(B*int(H/3) + int(H%3)*C)
                    else:
                        temp = E - H%3
                        if int(H/3) + int(H%3) + int(temp/2) >= N:
                            print((B*int(H/3))+(int(H%3)*C) + (int(temp/2)*A))
                        else:
                            print("-1")
                else:
                    if int(H%3) != 0 and E != 0 and E < H%3:
                        if int(H/3) + int(E) >= N:
                            print(B*int(H/3) + int(E)*C)
                        else:
                            temp = H%3 - E
                            if int(H/3) + int(E) + int(temp/3) >= N:
                                print((B*int(H/3)) + (int(E)*C) + (int(temp/3)*B))
                            else:
                                print("-1")
                    else:
                        print("-1")
            else:
                if int(H/3) + int(E/2) >= N:
                    print(int(H/3)*B + int(E/2)*A)
                elif (E%2) != 0 and (H%3) != 0:
                    temp = abs((E%2) - (H%3))
                    if int(H/3) + int(E/2) + temp >= N:
                        print(int(H/3)*B + int(E/2)*A + temp*C)
                    else:
                        print("-1")

    else: # min(A, B, C) == A
        if int(E/2) == N:
            print(N * A)
        else:
            if min(B, C) == B:
                if int(H/3) + int(E/2) >= N:
                    print(int(H/3)*B + int(E/2)*A)
                elif (E%2) != 0 and (H%3) != 0:
                    temp = abs((E%2) - (H%3))
                    if int(H/3) + int(E/2) + temp >= N:
                        print(int(H/3)*B + int(E/2)*A + temp*C)
                    else:
                        print("-1")
            else:
                if int(E%2) != 0 and H != 0 and H >= E%2:
                    if int(E/2) + int(E%2) >= N:
                        print(int(E/2)*A + int(E%2)*C)
                    else:
                        temp = H - E%2
                        if int(E/2) + int(E%2) + int(temp/3) >= N:
                            print(int(E/2)*A + int(E%2)*C + int(temp/3)*B)
                        else:
                            print("-1")
                else:
                    if int(E%2) != 0 and H != 0 and H < E%2:
                        if int(E/2) + int(E%2) >= N:
                            print(int(E/2)*A + int(E%2)*C)
                        else:
                            temp = E%2 - H
                            if int(E/2) + int(H) + int(temp/2) >= N:
                                print(int(E/2)*A + int(E%2)*C + int(temp/2)*A)
                            else:
                                print("-1")
                    else:
                        print("-1")


if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        _list = (input().split(' '))
        for i in range(0, len(_list)): 
            _list[i] = int(_list[i])

        calculate(_list)
