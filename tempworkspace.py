#1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ” method (which prints “name” and “kind” in a sentence).

#2) Try turning describe()  from an instance method into a class and a static method. Change it back to an instance method thereafter.




class Food:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def describe(self):
        print (str(self.__dict__))

    def __repr__(self):
        return str(self.__dict__)




#3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.
class Meat(Food):
    def cook(self):
        print("cooking")

class Fruit(Food):
    def clean(self):
        print("cleaning")


#4) Overwrite a “dunder” method to be able to print your “Food” class.


eggs = Food("eggs", "fried")
eggs.describe()
print(eggs)

steak = Meat("steak", "rare")
steak.cook()
print(steak)

apple = Fruit("apple","fresh")
apple.clean()
print(apple)