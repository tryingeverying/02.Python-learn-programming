from function_9_2_car import Car

class Battery():
    def __init__(self,battery_size = 70) -> None:
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"这个破车的电池容量是{self.battery_size}千瓦时")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = f"这个破车在满电的情况下能跑{range}公里"
        print(message)

class ElectricCar(Car):

    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
        self.battery = Battery()