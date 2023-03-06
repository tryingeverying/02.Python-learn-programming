"""导入单个类"""
from function_9_1_car import ElectricCar

my_byd = ElectricCar("比亚迪","元","2021")
print(my_byd.get_descriptive_name())
my_byd.battery.describe_battery()
my_byd.battery.get_range()
my_byd.battery.upgrade_battery()
my_byd.battery.describe_battery()
my_byd.battery.get_range()

""""同时导入多个类"""
from function_9_1_car import Car,ElectricCar

old_car = Car('上汽',"金杯",2008)
print(old_car.get_descriptive_name())
old_car.update_odometer(7878)
old_car.read_odometer()
old_car.increment_odometer(10000)
old_car.read_odometer()
print("\n")

my_byd = ElectricCar("比亚迪","元","2021")
print(my_byd.get_descriptive_name())
my_byd.battery.describe_battery()
my_byd.battery.get_range()
my_byd.battery.upgrade_battery()
my_byd.battery.describe_battery()
my_byd.battery.get_range()

"""导入整个模块"""
import function_9_1_car

old_car = function_9_1_car.Car('上汽',"金杯",2008)
print(old_car.get_descriptive_name())

my_byd = function_9_1_car.ElectricCar("比亚迪","元","2021")
print(my_byd.get_descriptive_name())
