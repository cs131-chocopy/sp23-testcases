
def f()->int:
    def g():
        nonlocal e
        print(e)
    e:int = 5
    g()
    return 4

print(f())
