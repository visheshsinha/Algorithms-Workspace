
A = [121, 432, 564, 23, 1, 45, 788]

def countingSort(place):
    
    global A

    k = 10

    B = list(range(len(A)))
    C = [0 for i in range(k)]
    


    for j in range(len(A)):
        index = A[j]//place
        C[index % 10] += 1


    for i in range(k):
        C[i] += C[i-1]

    i = len(A) - 1
    while i >= 0:
        index = A[i] //place
        B[C[index % 10] - 1] = A[i]
        C[index % 10] -= 1
        i -= 1

    for i in range(len(A)):
        A[i] = B[i]

def radixSort():

    global A

    m = max(A)
    place = 1

    while (m//place > 0):
        countingSort(place)
        place *= 10

def test():

    global A
    radixSort()
    print(A)

if __name__ == '__main__': test()