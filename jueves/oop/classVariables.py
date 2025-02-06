class Bird:
    species = "Bird" # This is a class variable shared by all 
                        #instances.
    def __init__(self, name):
        self.name = name # This is an instance variable, unique to
                        #each instance.


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle): # Car inherits from Vehicle
    def __init__(self, brand, model):
        super().__init__(brand) # Initialize the parent class. VERY
                                #IMPORTANT
        self.model = model
    def print(self):
        print(self.brand, self.model )

if __name__=='__main__':
    c1=Car('Citroen','c3')
    c1.print()
