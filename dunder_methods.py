# dunder methods or magic methods 

# __ defined by built-in classes used for operator overloading
# __init__ initialization of obj is invoked when instance is created
# __repr__  defines how object is represented as string machine readeble representation type
# __str__ 
# __format__
# __hash__

class String:
    def __init__(self, string):
        self.string = string
        

    
class String2:
    
    def __init__(self, string):
        self.string = string
        
    def __repr__(self):
        return 'Object: {}'.format(self.string)
    
    def __add__ (self, other):
        return self.string + other    # if here other.string then only str + str allowed


class Vector:
    def __init__(self, x, y):
        self.x =x
        self.y =y
    
    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x , self.y - other.y)

    def __call__(self):
        print("Hello! I was called!!")



if __name__ == "__main__":
    
    # obj
    string_1 = String('Hello')
    print(string_1)
    string_2 = String2("Hello 2")
    print(string_2)
    
    
    # error obj + str not allowed
    print(string_2 + ' world') 
    
    # now allowed
    print(string_2 + 'is brutal')
    
    v1 = Vector(10, 20)
    v2 = Vector(30, 40)
    
    v3 = v1 + v2
    v4 = v1 - v2
    
    v3()
    print(v3.x, v3.y)