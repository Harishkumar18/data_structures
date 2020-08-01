"""
singleton pattern

Design patterns are divided into a few broad categories, though mainly Creational patterns, Structural patterns, and Behavioral patterns.
This pattern restricts the instantiation of a class to one object. It is a type of creational pattern and involves only one class to create methods and specified objects.
It provides a global point of access to the instance created.
Motivation:
This pattern is commonly implemented in features that require control over access to a shared resource such as a database connection or a file. By ensuring that a class can only be used to create a single instance and providing a single global access point, access to the shared resource can be restricted and integrity can be maintained.
A good analogy of a singleton pattern is that a country can have a single government that controls access and operations within the country. Any attempts to create another government are forbidden.

Pros and Cons
Pros
The Singleton pattern offers the guarantee that only one instance of our class exists and reduces the risk of unexpected behavior in our program.
Since the creation of the class is controlled by a single class, this offers flexibility since changes only need to be made to one class and object.
Cons
A class created using the singleton pattern violates the Single Responsibility Principle since the class may have to handle more than one responsibility at a given time.
Life cycle management can pose problems in other areas such as testing since the singleton class is kept alive during the lifespan of the application and different test cases might require new versions of the class.


"""


class Singleton:
    _instance = None

    def __init__(self):
        if not Singleton._instance:
            Singleton._instance = self
        else:
            raise Exception("This class is a singleton!")

    @staticmethod
    def get_instance():
        if not Singleton._instance:
            Singleton()
        return Singleton._instance


class not_singleton:
    _instance = None

    def __init__(self):
        not_singleton._instance = self

    @staticmethod
    def get_instance():
        return not_singleton._instance


ns = not_singleton()
print(ns)

new = not_singleton.get_instance()
print(new)

new_ns = not_singleton()
print(new_ns)


s = Singleton()
print(s)

new = Singleton.get_instance()
print(new)

new2= Singleton.get_instance()
print(new2)

new_s = Singleton()
print(new_s)