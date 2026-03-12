# Create child class Car that overrides start().

class Vehical:
    def start(self):
        print('Vehical is here')

class Car(Vehical):
    def start(self):
        print("Car is here")

obj=Car()
obj.start()