def BintoInt(src:str)->int:
    ans:int = 0
    x:str = ""
    for x in src:
        if x == "0":
            ans = ans * 2
        elif x == "1":
            ans = ans * 2
            ans = ans + 1
    return ans

print(BintoInt("11100101"))
