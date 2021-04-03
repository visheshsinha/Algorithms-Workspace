"""
Problem: Suffix Array
Source: https://codeforces.com/edu/course/2/lesson/2
@Author: Vishesh Sinha
"""
def suffixArray(_str):
    _len = len(_str)
    _p , _c = [], []
    _a = []

    for i in range(_len):
        _a.append([_str[i], i])
    _a.sort()

    for i in range(_len):
        _p.append(_a[i][1])
        _c.append(int())

    _c[_p[0]] = 0
    for i in range(1, _len):
        if _a[i][0] == _a[i-1][0]:
            _c[_p[i]] = _c[_p[i-1]]
        else:
            _c[_p[i]] = _c[_p[i-1]] + 1


    k = 0

    while True:

        _a = []
        for i in range(_len):
            _a.append([_c[i], _c[(i + (1<<k)) % _len], i])
        
        _a.sort()

        for i in range(_len):
            _p[i] = _a[i][2]


        _c[_p[0]] = 0
        for i in range(1, _len):
            if _a[i][0] == _a[i-1][0] and _a[i][1] == _a[i-1][1]:
                _c[_p[i]] = _c[_p[i-1]]
            else:
                _c[_p[i]] = _c[_p[i-1]] + 1

        k += 1

        if (1 << k) >= _len:
            break
    
    print(*_p)

if __name__ == '__main__':
    _str = input()
    _str += "$"
    suffixArray(_str)
    