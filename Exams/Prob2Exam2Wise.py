class House:
    def __init__(self, rooms, year, city, house_type = 'S'):
        self.num_rooms = rooms
        self.year_built = year
        self.city = city
        self.type = house_type

    @property
    def year_built(self):
        return self._year_built
    @year_built.setter
    def year_built(self, val):
        if(0 <= val <= 2023):
            self._year_built = val
        else:
            raise ValueError('Year is not between 0 and 2023')
    @property
    def age(self):
        return 2023 - self.year_built
    
    def __str__(self):
        if self.type == 'S':
            to_return = 'Single'
        else:
            to_return = 'Multi'
        return f"{to_return}-Family house with {self.num_rooms} rooms located in {self.city} was built in {self._year_built}"
    
    def __gt__(self, other):
        if isinstance(other, int):
            return self.year_built > other
        elif isinstance(other, str):
            return self.city > other
        elif isinstance(other, House):
            return self.num_rooms > other.num_rooms

class Duplex(House):
    def __init__(self, num_rooms, year, city):
        super().__init__(num_rooms, year, city, 'M')
        self.num_units = 2
    
    def __add__(self, other):
        if isinstance(other, Duplex):
            return Duplex(self.num_rooms + other.num_rooms, max(self.year_built, other.year_built), self.city)
        
    def __iadd__(self, other):
        if isinstance(other, Duplex):
            self.num_rooms += other.num_rooms
            self.year_built = max(self.year_built, other.year_built)
    
            
house1 = House(4, 1990, 'Boston', 'M')
house2 = House(19, 2000, 'Seattle', 'S')
house3 = Duplex(6, 2022, 'Chelsea')
house4 = Duplex(2, 2021, 'San Francisco')
print(house1)
print(house2)
print(house3)
print(house4)

        


