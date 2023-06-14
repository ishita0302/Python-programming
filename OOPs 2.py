#types of constructor - parameterized (__init__(self,color,name)) & non-parameterized (__init__(self))
class car:
    wheel=4                                   #class variable can be called by both class & instance
    def __init__(self,color,driver):            #instance variable implicitely declared
        self.color = color
        self.driver = driver

print(car.wheel)
car1 = car("black","ishita")
car1.model = "LXI 2023"                 #instance variable can be declared outside(explicitely) class also for each object seperately
car2 = car("red","kritika")             #2 arguments are required
print(car1.color,car1.driver,car1.model,car1.wheel)
print(car2.color,car2.driver,car2.wheel)
del car1                                #to freeing the space of an instance and deleting it.

#non-static method - used by an instance
#static method - used by anyone to access class attributes