#pass in class if it is empty
#print(type(car))    type
#print(type(c1))    _main_car

class car:
    #print("successful") - it is an eg. and not dependent on object as not linked - it will print only 1 time
    var=input("enter car1 name: ")
    print(var)

c1 = car()
c2 = car()
print(c1.var,"car")
print(c2.var,"car")

#constructor - __init__ - as an initializer used for mapping. It can only be modified as constructor built as default.
class car:
    def __init__(self):         #self is not mandatory and constructor can have many attributes where self is object name.
        self.var=input("enter car name: ")

class driver:
    def __init__(self):
        self.var=input("enter driver name: ")

c1 = car()
d1 = driver()
c2 = car()
d2 = driver()
print(c1.var,"car",d1.var,"driver")
print(c2.var,"car",d2.var,"driver")

#2 magical methods - __init__() , __new__()
#__new__() - to create an object and it is first method to be called in a class.
class test:
    def __init__(self):
        print("a constructor")
    def __new__(cls):
        print("new method")
        return super(test,cls).__new__(cls)         #to tell it that constructor is modified then only __init__ will work.

t = test()