class CountClasses(type):
    _count = {}

    def __new__(cls, name, bases, dct):
        #print("Я родился", cls,  name, bases, dct, sep="\n", end="\n...\n")
        dct["_count"] = cls._count
        return super().__new__(cls,  name, bases, dct)


    def __call__(cls, *args, **kwargs):
        result = super().__call__(*args, **kwargs)
        classname = cls.__name__
        cls._count[classname] = cls._count.get(classname, 0) + 1
        return result


class MyClass1(metaclass=CountClasses):
    pass

obj1 = MyClass1()
obj2 = MyClass1()
print(obj2._count)

class MyClass2(metaclass=CountClasses):
    pass

obj11 = MyClass2()
obj12 = MyClass2()
print(obj2._count)

print("Task 3".center(40, "="))
class Register(type):
    _register = set()

    def __new__(cls, name, bases, dct):
        #print("Я родился", cls,  name, bases, dct, sep="\n", end="\n...\n")
        dct["register"] = cls._register
        return super().__new__(cls,  name, bases, dct)


    def __call__(cls, *args, **kwargs):
        result = super().__call__(*args, **kwargs)
        if cls.__name__ not in cls._register:
            cls._register.add(cls.__name__)
        return result


class MyClass3(metaclass=Register):
    pass

ob1 = MyClass3()
ob2 = MyClass3()
print(*ob2.register)

class MyClass4(metaclass=Register):
    pass

ob3 = MyClass4()
ob4 = MyClass4()
print(*ob2.register)