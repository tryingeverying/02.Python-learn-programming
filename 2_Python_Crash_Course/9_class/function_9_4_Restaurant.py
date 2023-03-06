"""一个描述餐馆的类"""
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name}大饭店，主营{self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name}大饭店开门了 ")

    def set_number_served(self,number):
        self.number_served = number
        
    def increment_number_served(self,add_number):
        self.number_served += add_number