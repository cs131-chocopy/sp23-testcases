class A(object):
    x: int = 10


x: [[A]] = None
y: [A] = None
z: [[int]] = None
x = [[None]]  # bad
y = z = [None]  # bad
y[0] = A()
print(z[0][0])
