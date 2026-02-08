'''Inheritance allows a class to inherit attributes from other classes.Helps with code reusability and
   extensibility'''
class Animal:
  def __init__(self,name):
    self.name = name
    self.is_alive = True
  def eat(self):
    print(f"{self.name} is eating")
  def sleep(self):
    print(f"{self.name} is sleeping")
class Dog(Animal):
  def speak(self):
    print("WOOf")
class Cat(Animal):
  pass
dog = Dog("Max")
cat = Cat("kitty")
print(dog.name)
print(cat.name)
dog.eat()
cat.sleep()
dog.speak()




