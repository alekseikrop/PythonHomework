def foo(lst):
    res = []
    elem = 1
    for i in lst:
        for j in lst:
            if i == j:
                continue
            elem *= j
        res.append(elem)
        elem = 1
    return res

if __name__ == '__main__':
    print(foo([1, 2, 3, 4, 5]))
    print(foo([3, 2, 1]))
