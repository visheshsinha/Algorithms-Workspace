def countingSort(A, k):
    B = list(range(len(A)))
    C = [0 for i in range(k)]
    
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1
    print(C)

    for i in range(k):
        C[i] = C[i] + C[i-1]

    for j in range(len(A)):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1

    return B    

if __name__ == '__main__':
    
    A = [3, 4, 5, 3, 5, 8, 6, 8, 0, 7, 0]
    B = countingSort(A, 10)
    print(B)