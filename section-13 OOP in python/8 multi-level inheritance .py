class A:
    def method_a(self):
        print("Method of class A")

class B(A):  # Class B inherits from class A
    def method_b(self):
        print("Method of class B")

class C(B):  # Class C inherits from class B
    def method_c(self):
        print("Method of class C")

# Create an object of class C
c_object = C()

# Now we can call methods from class A, class B, and class C
c_object.method_a()  # Inherited from class A
c_object.method_b()  # Inherited from class B
c_object.method_c()  # Defined in class C
