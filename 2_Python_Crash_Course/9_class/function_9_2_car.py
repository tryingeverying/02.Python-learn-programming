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