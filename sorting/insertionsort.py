def insertionsort(A):
    for i in range(len(A)):
        key = A[i]
        j = i - 1
        while j > -1 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A


if __name__ == "__main__":
    A = [ 2 , 3 , 1 , 4 , 2 , 18 , 9 , 1 ]
    print(insertionsort(A))