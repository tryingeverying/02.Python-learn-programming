"""一个描述管理员以及其权限的类"""

from function_9_6_User import User

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

