x = [1, 2, 3]


# print(*x)

def xx(*a, **k):
    print(k['Yasser'])
    print(a)


xx(1, 2, 3, Yasser=39)
