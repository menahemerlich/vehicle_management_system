from classes.vehicle import Vehicle
from classes.engine import Engine

class Car(Vehicle):
    def __init__(self, license_plate, year, engine: Engine):
        super().__init__(license_plate, year)
        self.tax = None
        self.engine = engine

    def calculate_annual_tax(self):
        self.tax = 0
        if self.get_year() > 2000:
            self.tax += 1000
        else:
            self.tax += 500
        if self.engine.horsepower > 100:
            self.tax += 500
        else:
            self.tax += 250
        return self.tax





