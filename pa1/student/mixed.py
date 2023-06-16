class A(object):
    x: int = 23333
    y: str = "12312123"

    def foo(self: A) -> int:
        x: int = 123
        if True:
            return 2 if 3 else 3 and 4 if 3 else 3 or 3
        elif False:
            return 2 if 3 else 3 and 4 if 3 else 3 or 3 if 3 else 3 and 4 if 3 else 3 or 3
        else:
            return 2 if 3 else 3 and 4 if 3 else 3 or 32 if 3 else 3 and 4 if 3 else 3 or 32 if 3 else 3 and 4 if 3 else 3 or 3

    def f(x: int, y: A):
        x: int = 123

        def f(x: int, y: A):
            def f(x: int, y: A):
                def f(x: int, y: A):
                    x: int = 123

                    def f(x: int, y: A):
                        pass
                    pass
                pass
            pass
        pass


def f(x: int, y: A):
    def f(x: int, y: A):
        def f(x: int, y: A):
            def f(x: int, y: A):
                def f(x: int, y: A):
                    z: int = 123
                    pass
                pass
            pass
        pass
    pass
