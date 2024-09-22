class A:
    def method_a(self):
        print("method of class A")

class B:
    def method_b(self):
        print("method of class B")

class C(A, B):
    def method_c(self):
        print('method of class C')

cobject = C()
cobject.method_a()  # Calls method of class A
cobject.method_b()  # Calls method of class B
cobject.method_c()  # Calls method of class C

