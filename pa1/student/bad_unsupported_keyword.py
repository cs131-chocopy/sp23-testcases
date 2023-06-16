async def range(n: int) -> None:
    i: int = 0
    while i < n:
        yield i
        i = i + 1
