class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self._velocity = value
        else:
            self._velocity = 0

    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        if 0 <= value <= 100:
            self._fuelRate = value
        else:
            self._fuelRate = 0

    def run(self, distance, velocity):
        self.velocity = velocity
        fuel_needed = distance * 0.1  # 10% per 10 km
        if self.fuelRate >= fuel_needed:
            self.fuelRate -= fuel_needed
            self.stop(0)
        else:
            distance_left = distance - (self.fuelRate / 0.1)
            self.fuelRate = 0
            self.stop(distance_left)

    def stop(self, remain_distance):
        self.velocity = 0
        if remain_distance > 0:
            print(f"Car stopped! {remain_distance:.2f} km left due to no fuel.")
        else:
            print("Arrived at destination!")
