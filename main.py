from classes.electric_car import ElectricCar
from classes.car import Car
from classes.truck import Truck
from classes.engine import Engine

car1 = Car(1504726, 1998, Engine(170, "MINI"))
e_car1 = ElectricCar(20284703, 2015, Engine(150, "BMW"))
truck1 = Truck(40156201, 2005, 350)
vehicles = [car1, e_car1, truck1]
for vehicle in vehicles:
    print(vehicle.calculate_annual_tax())

e_car1.set_year(2021)
print(e_car1.get_year())
e_car1.charge()
l = ["elctric", "blake"]
print(e_car1.get_luxury_features(l))



