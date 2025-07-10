# wrapper just like toll gate through whic a func or an obj has to pass
# that takes another function as an argument and returns a new function with enhanced functionality.
# use - logging , timing, memorization, authentication
# can have muiltiple decorators too

import time 
import functools

def toll_gate_wrapper(func):
    def wrapper(*args, **kwargs):
        print(" checking for toll pass.....")
        result = func(*args, **kwargs)
        print(" Toll passed. proceeding")
        return result
    return wrapper


@toll_gate_wrapper
def drive_through(name):
    print(f"{name} is driving through the toll gate.")
    
    
    
drive_through("alice")
    
    

# method decorators 

def logged(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f'{fname} returned value {value}. \n')
            f.write(f"{fname} returned the value { value}")
        return value 
    return wrapper

@logged
def add(x,y):
    return x + y


print(add(10,30))


                       

def timed(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = func(*args, **kwargs)
        after = time.time()
        fname = func.__name__
        print(f'{fname} took {after-before:.100f} seconds to execute !!')
        return value
    return wrapper



@timed 
def myFunc(x):
    result = 1
    for i in range(1,x):
        result += 1
        
    return result

print(myFunc(10))


# class decorators

def fun(cls):
    cls.class_name = cls.__name__
    return cls 

@fun
class Person:
    pass 

print(Person.class_name)



#  BUILT-IN DECORATORS


# @classmethod define method that operates on class itself 
# can access and modify class state that applies across all instances of class 

class Employee:
    raise_amount = 1.05
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


Employee.set_raise_amount(1.10)
print(Employee.raise_amount)



# @staticmethod decorator used to define method that does not operate on instance of class
# they are called on class itself

class MathOperations:
    @staticmethod
    def add(x,y):
        return x + y


res = MathOperations.add(10,30)
print(res)



# The @property decorator is used to define a method as a property, 
# which allows you to access it like an attribute. This is useful for encapsulating the implementation of a method while still providing a simple interface.

class Circle:
    def __init__(self, radius):
        self._radius= radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        
        if value>=0:
            self._radius = value
        else:
            raise ValueError("Radius cant be -ve")
        
    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)


c = Circle(45)
print(c.radius)
print(c.area)



    
   
    

    

    
    
