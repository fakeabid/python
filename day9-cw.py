class Vehicle:
    def __init__(self, id, rate):
        self._vehicle_id = id
        self._base_rate = rate

    def display_details(self):
        return f'{self._vehicle_id}- rate:{self._base_rate}'
    
    def rental_charge(self):
        return 0.0
    

class Car(Vehicle):
    def __init__(self, id, rate, num_seats):
        super().__init__(id, rate)
        self._num_seats = num_seats

    def rental_charge(self):
        return self._base_rate * self._num_seats
    
class Bike(Vehicle):
    def __init__(self, id, rate, bike_type):
        super().__init__(id, rate)
        self._bike_type = bike_type

    def rental_charge(self):
        return self._base_rate * 0.5
    
def calculate_rental(vehicle):
    return vehicle.rental_charge()

volvo = Car('1sd34', 500, 5)
print(calculate_rental(volvo))