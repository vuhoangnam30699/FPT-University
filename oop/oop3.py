"""

Viết chương trình quản lý động vật, có các thuộc tính name().
Với class Dog(), Cat() sẽ có thêm thuộc tính khác như speak()

"""


class Animal:
    def __init__(self, name: str):
        self._name = name
        
    def speak(self):
        raise NotImplementedError("Subclass implements this method")
        
class Dog(Animal):     
    def speak(self):
        return f"{self._name} says Woof!"
    
    
class Cat(Animal):
        
    def speak(self):
        return f"{self._name} says Meow!"
    
class Bird(Animal):
    def __init__(self, name, can_fly: bool):
        super().__init__(name)
        self.can_fly = can_fly
    
    def speak(self):
        return f"{self._name} can Tweet"
        
        
dog = Dog('Dog')
print(dog.speak())

cat = Cat('Cat')
print(cat.speak())
    
bird = Bird('Bird', True)
print(bird.speak())

print("Can bird fly?")
print(bird.can_fly)
    



        
        
    