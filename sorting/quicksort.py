def partition(A, l, h):
    i = l - 1
    pivot = A[h]
    
    for j in range(l, h):
        print('i = ', i, 'j =', j)
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i+1], A[h] = A[h], A[i+1]
    return i+1

def quicksort(A, l, h):
    print(A)
    if l < h:
        j = partition(A, l, h)
        quicksort(A, l, j-1)
        quicksort(A, j+1, h)


if __name__ == '__main__':
    A = [4, 5, 2, 3, 56, 18, 29, 44]
    n = len(A)
    quicksort(A, 0, n-1)