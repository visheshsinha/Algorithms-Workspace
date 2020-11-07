def mergesort(A):
    if len(A) == 1:
        return A
    elif len(A) == 2:
        if A[0] > A[1]:
            return [A[1], A[0]]
        else:
            return A
    
    l = len(A) // 2
    m1 = mergesort(A[l:])
    m2 = mergesort(A[:l])

    ans = []

    while True:
        if len(m1) > 0 and len(m2) > 0:
            if m1[0] <= m2[0]:
                ans.append(m1[0])
                m1 = m1[1:]
            else:
                ans.append(m2[0])
                m2 = m2[1:]
        elif len(m1) > 0:
            ans += m1
            m1 = []
        elif len(m2) > 0:
            ans += m2
            m2 = []
        else:
            break
    return ans

if __name__ == "__main__":
    A = [ 2 , 3 , 1 , 4 , 2 , 18 , 9 , 1 ]
    ans = mergesort(A)
    print("Array:", A, "\nSorted Array:", ans)
