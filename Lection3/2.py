class Person(): #наследование
    classId = 24
    name = ""
    """docstring for Person"""
    
    def __init__(self, name):
        self.name = name;
        print("This is __init__")
    
a = Person('Denis')
print(a.name)



class Animal:
    def say(self):
        print('Hello world!')
    pass #пропустить дальше

class Cat(Animal):
    def say(self):
        print('Meow!')

class Dog(Animal):
    def say(self):
        print('Woaf!')
        
class CatDog(Cat, Dog):#сначала Cat, потом Dog
    def __init__(self):
        super().__init__() #вызов из суперкласса
    def __del__(self):
        #можно что-нибудь сделать
        pass
    pass
    #def say(self):
    #    print('WTF')

cd = CatDog()
cd.say()

print(dir(str))
#magic methods
#__doc__ - документация

class Pizza():
    @staticmethod
    def mix(x, y):
        return x+y
    @classmethod
    def methods(cls):
        pass
    
    def cook(self):
        return 123456789
    
Pizza(42).cook() == Pizza(24).cook() #false - разные объекты
Pizza.cook() #указатель на функцию