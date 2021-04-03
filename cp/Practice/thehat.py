"""
-- The Hat (CF - Round 503 Div. I)

- n students (n is even)
- i and i+1 are adjacent in a circle 

- if Both student i and student i + n/2 have same number given to them , terminate the program printing i
    - else -1

"""
import  sys, numpy as np

a = np.zeros((100001), dtype=int)

def main(n):
    
    if n % 4 != 0:
        print("! -1")
        sys.stdout.flush()
        return
    
    print("?", n//2)
    sys.stdout.flush()
    a[n//2] = int(input())

    print("?", n)
    sys.stdout.flush()
    a[n] = int(input())

    if a[n]==a[n//2]: 
        print("!", n//2)
        sys.stdout.flush()
        return

    a[0] = a[n]
    work(0,n//2)


def work(l, r):
    if (l>r) :
        print("! -1")
        sys.stdout.flush()
        return

    mid = (l+r)>>1

    if l == mid:
        print("! -1")
        sys.stdout.flush()
        return

    print("?",mid)
    sys.stdout.flush()
    a[mid] = input()

    print("?",mid+n/2)
    sys.stdout.flush()
    a[mid+n//2] = input()

    if a[mid]==a[mid+n//2]: 
        print("!",mid)
        sys.stdout.flush()
        return
    if (a[l]<a[l+n//2] and a[mid]>a[mid+n//2] or a[l]>a[l+n//2] and a[mid+n//2]>a[mid]):
        work(l,mid)
    else:
        work(mid,r)

if __name__ == "__main__":
    n = int(input())
    main(n)
