# Demonstrate single inheritance using Animal → Dog.

class Animal:
    def ani_sound(self):
        print('The Animal sound')
class Dog(Animal):
    def dog_sound(self):
        self.ani_sound()
        print("The dog barks")

obj=Dog()
obj.dog_sound()