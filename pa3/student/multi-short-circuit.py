def a()->bool:
    print(1)
    return True

b: bool = False
print(a() and a() and b and a())
print(b or b or a() or b)


