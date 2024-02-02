class Car:
    COLORS = {'Blue', 'Red', 'Black'}
    def __init__(self, make, model, year, color):
        self.make, self.model = make, model
        self.year = year
        self.color = color
    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, val):
        if val > 1900:
            self.year = val
        else:
            raise ValueError('Year must be greater than 1900.')
    
car1 = Car('Toyota', 'Corolla', 2022, 'Blue')
# car1.__year = 2020
# print(car1.__year)
# car1._Car__year = 2020
# print(car1.year)
car1.year = 2020
print(car1.year)