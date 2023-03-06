"""一个描述用户以及用户权限的类"""
class User():
    def __init__(self,first_name,last_name,age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name}{self.last_name}今年{self.age}岁了\n")

    def greet_user(self):
        print(f"靓仔，欢迎{self.first_name}{self.last_name}\n")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
    def __init__(self) -> None:
        self.privileges = ["can add post","can delete post","can ban user",]

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"尊贵的管理员有{privilege}的权限")
            
class Admin(User):
    def __init__(self, first_name, last_name, age) -> None:
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()