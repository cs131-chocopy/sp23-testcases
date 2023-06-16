class A(object):
    def f(self:A, s:str):
        print(len(s))

x:str = "a string"
y:str = "another string"
l:[str] = None

l = l + [x]
l = l + [y]
A().f(l[1])