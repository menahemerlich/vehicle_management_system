from classes.car import Car
from classes.electric_mixin import ElectricMixin
from classes.luxury_mixin import LuxuryMixin

class ElectricCar(Car, ElectricMixin, LuxuryMixin):
    pass




