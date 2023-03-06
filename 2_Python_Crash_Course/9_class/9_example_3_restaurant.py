"""9-10 导入Restaurant 类 ：将最新的Restaurant 类存储在一个模块中。在另一个文件中，导入Restaurant 类，建一个
Restaurant 实例，并调用Restaurant 的一个方法，以确认import 语句正确无误"""

from function_9_4_Restaurant import Restaurant

so_big_restaurant = Restaurant("黄焖鸡米饭","鲁菜")
print(so_big_restaurant.number_served)
so_big_restaurant.set_number_served(50)
print(so_big_restaurant.number_served)

so_big_restaurant.increment_number_served(50)
print(so_big_restaurant.number_served)
print(so_big_restaurant.describe_restaurant())