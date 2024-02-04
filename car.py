#Class definitions
class Vehicle:
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    def get_year(self):
        return self.year
    
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def get_doors(self):
        return self.doors
    
    def get_roof(self):
        return self.roof
    
#User input:
user_year = input('What is the year of the car? ')
user_make = input('What is the make of the car? ')
user_model = input('What is the model of the car? ')
user_doors = input('How many doors does the car have? ')
user_roof = input('What kind of roof does the car have? ')

#Instance creation
user_vehicle = Automobile('car', user_year, user_make, user_model, user_doors, user_roof)

#Readable output
print("\nVehicle type: "+Automobile.get_type(user_vehicle)+"\nYear: "+Automobile.get_year(user_vehicle)+"\nMake: "+Automobile.get_make(user_vehicle)+"\nModel: "+Automobile.get_model(user_vehicle)+"\nNumber of Doors: "+Automobile.get_doors(user_vehicle)+"\nRoof Type: "+Automobile.get_roof(user_vehicle)+"\n")