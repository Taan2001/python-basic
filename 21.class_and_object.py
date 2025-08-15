# # class 
# class Person:
#     # class attributes
#     count = 0 # be used by Person.count

#     # constructor
#     def __init__(self, name, age):
#         self.name = name # self.name is instance attribute  
#         self.age = age # self.age is instance attribute
#         Person.count += 1
    
#     # methods
#     def print_person(self):
#         print(f"Name: {self.name} - Age: {self.age}")
    
# # 1. Create object
# per_1 = Person("Taan", 25)
# per_2 = Person("An", 20)

# # 2. Get class attribute  
# print(f"The number of person is {Person.count}")
    
# # 3. Get instance attributes
# print(f"The name of person1 is {per_1.name}")
# print(f"The age of person2 is {per_2.age}")

# # 4. call method
# per_1.print_person()
# per_2.print_person()


# # Inheritance
# class Student:
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score

# # Create Object
# my_student = Student("Taan", 25, 10)
# print(f"Before changing object Student: {my_student.name}")

# my_student.name = "TAAN"
# print(f"After changing object Student: {my_student.name}")

# # Inheritance
# class Animal:
#     def __init__(self, name, age, weight):
#         self._name = name
#         self._age = age
#         self._weight = weight

# # Create Object
# my_animal = Animal("Dog", 25, 10)
# print(f"Before changing object Animal: {my_animal._name}")

# my_animal._name = "Cat"
# print(f"After changing object Animal: {my_animal._name}")

# # Inheritance
# class Tree:
#     def __init__(self, name, height):
#         self.__name = name
#         self.__height = height

# # Create Object
# my_tree = Tree("Rose", 10)
# # print(f"Before changing object Tree: {my_tree.__name}") # error

# my_tree.__height = 9.5
# print(f"After changing object Tree: {my_tree.__height}") # 9.5
# print(f"After changing object Tree: {my_tree.__dict__}") # 
# print(f"After changing object Tree: {my_tree._Tree__height}") # 10


# class Teacher(Person):
#     def __init__(self, name, age):
#         super().__init__(name + '-teacher', age)
#         # Person.__init__(self, name + '-teacher', age)
#         # self.name = name + '-teacher'
#         # self.age = age

# my_teacher = Teacher("Taan", 32)
# my_teacher.print_person()

# # Polymorphism 
# class Animal: 
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         return "some sound"

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def speak(self):
#         return "sound gauwgauw"

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def speak(self):
#         return "sound meowmeow"

# my_animal = Animal("a bird")
# my_dog = Dog("dog")
# my_cat = Cat("cat")

# print(f'my animal speak: {my_animal.speak()}')
# print(f'my dog speak: {my_dog.speak()}')
# print(f'my cat speak: {my_cat.speak()}')

# Abstraction
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    def not_abstract_method(self):
        return "no need overwrite"

class Dog(Animal):
    def speak(self):
        return "gawugawu~~"

class Cat(Animal):
    def speak(self):
        return "meow~meow~"

my_dog = Dog()
my_cat = Cat()
print(f"my dog speak: {my_dog.speak()}")
print(f"my cat speak: {my_cat.speak()}")
print(f"my dog call not_abstract_method: {my_dog.not_abstract_method()}")
print(f"my cat call not_abstract_method: {my_cat.not_abstract_method()}")