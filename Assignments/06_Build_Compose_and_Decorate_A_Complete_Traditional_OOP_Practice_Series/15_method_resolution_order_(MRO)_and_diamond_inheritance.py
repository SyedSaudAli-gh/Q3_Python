class A:
    def show(self):
        print("show method from 'A'")
        
class B(A):
    def show(self):
        print("Show Method from B")
        
class C(A):
    def show(self):
        print("Show Method from C")
        
class D(B, C):
    pass
        
d1 = D()
d1.show()