class A:
    def __init__(self):
        self.x=20
    def f(self):
        self.x=self.x+1
        print(self.x)
s=A()
print(s.x)
print(A().x)
print(A().f)
s.f()
print(s.x)