class A(object):
    x: int = 23333
    y: str = "12312123"

    def foo(self: A) -> int:
        x: int = 123
        if True:
            return 2 if True else 4 if True else 3
        return x

    def f(self: A, x: int, y: A):
        def f(x: int, y: A):
            def f(x: int, y: A):
                def f(x: int, y: A):
                    def f(x: int, y: A):
                        z: int = 100000
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
