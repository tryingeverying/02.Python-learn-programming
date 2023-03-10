"""编写一个名为Employee 的类，其方法__init__()接受名、姓和年薪，
并将它们都存储在属性中。编写一个名为give_raise() 的方法，
它默认将年薪增加5000美元，但也能够接受其他的年薪增加量。"""

class Employee():
    def __init__(self,last_name,first_name,salary) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.salary = salary

    def give_raise(self,add_salary = 5000):
        new_salary = int(self.salary) + int(add_salary)
        return f"{self.first_name}{self.last_name}的最新薪资待遇为{new_salary}"
    








