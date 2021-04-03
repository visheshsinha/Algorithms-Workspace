"""
Problem: Minimum Grid Path
Source: https://codeforces.com/contest/1499/problem/B
@Author: Vishesh Sinha
"""

def gridPath(n, _list):

    odd_i = [] 
    even_i = [] 
    for i in range(0, len(_list)): 
        if i % 2: 
            even_i.append(_list[i]) 
        else : 
            odd_i.append(_list[i])

    _index_odd = odd_i.index(min(odd_i))
    _index_even = even_i.index(min(even_i))

    cost = 0
    count = 0

    for i in odd_i:
        _index = odd_i.index(i)

        cost += 1*int(i)
        count += 1

        if _index >= max(_index_even, _index_odd):
            break
    
    cost += (n - count) * odd_i[_index_odd]
    count = 0

    for i in even_i:
        
        cost += 1*int(i)
        count += 1

        _index = even_i.index(i)

        if _index >= max(_index_even, _index_odd):
            break

    cost += (n - count) * even_i[_index_even]
    return cost

if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):

        n = int(input())

        _list = (input().split(' '))
        for i in range(0, len(_list)): 
            _list[i] = int(_list[i])

        print(gridPath(n, _list))