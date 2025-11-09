from classes.vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, license_plate, year, max_load):
        super().__init__(license_plate, year)
        self.tax = None
        self.max_load = max_load

    def calculate_annual_tax(self):
        self.tax = 0
        if self.get_year() > 2000:
            self.tax += 1000
        else:
            self.tax += 500
        if self.max_load > 400:
            self.tax += 500
        else:
            self.tax += 250
        return self.tax




