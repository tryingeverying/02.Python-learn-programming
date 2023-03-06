"""关于car的类"""

class Car():

    def __init__(self,make,model,year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
        #默认属性，有点类似于函数中的默认参数，他这个不用在上面初始化的操作有点秀，
        # 但是看情况他给的是定值，如果这个值后期是可以修改的那应该还是要传入参数的

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print(f"这个车已经开了{self.odometer_reading}公里了")

    def update_odometer(self,mileage):
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        self.odometer_reading += miles

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












