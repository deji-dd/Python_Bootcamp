class Dog:
    # Class object attribute: They are the same for any instance of a class
    species = 'Mammal'
    def __init__(self, breed, name):
        # For attributes, we take in the argument and assign it using self.attribute_name
        self.breed = breed
        self.name = name
    # Methods -> Actions/Operations
    def bark(self, number):
        print(f"Woof! My name is {self.name} and I'm {number} years old")


class Circle:
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius
    def circumference(self):
        return f"The circumference is {2 * Circle.pi * self.radius}"
    def area(self):
        return f"The area is {Circle.pi * self.radius ** 2}"


class Animal:
    def __init__(self):
        print("Animal created!")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")


my_dog = Dog('Lab', 'Sammy')
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)
my_dog.bark(7)
print('\n')
my_circle = Circle(7)
print(my_circle.area())
print(my_circle.circumference())


class Dog(Animal):  # Inheritance
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def who_am_i(self):
        print("I am a dog")


print('\n')
my_dog = Dog()
my_dog.who_am_i()
my_dog.eat()
print('\n')


class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} says woof!"


class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} says meow!"


niko = Dog("Niko")
felix = Cat("Felix")
print(niko.speak())
print(felix.speak())
print('\n')

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())

print('\n')

def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)


class Animal():
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")  # Used to return an error


myanimal = Animal('Fred')
# myanimal.speak() -> returns an error
print('\n')


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}."
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book object has been deleted!")


b = Book('Python Bootcamp Rocks', 'Jose', 200)
print(b)
del b  # deletes a variable
