"""编写一个测试用例，其中包含两个测试方法：
test_give_default_raise() 和test_give_custom_raise() 。
使用方法setUp() ，以免在每个测试方法中都创建新的雇员实例。
运行这个测试用例，确认两个测试都通过了。"""

import unittest
from function_11_7_employee import Employee

class TestEmployee(unittest.TestCase):
    """针对Employee类的测试用例"""

    def setUp(self) -> None:
        """初始化实例"""
        self.employee = Employee("狗子","大","50000")

    def test_give_default_raise(self):
        '''测试默认方法是否会出bug'''
        new_salary = self.employee.give_raise()
        self.assertEqual("大狗子的最新薪资待遇为55000",new_salary)

    def test_give_custom_raise(self):
        '''测试自定义方法是否会出bug'''
        new_salary = self.employee.give_raise(3000)
        self.assertEqual("大狗子的最新薪资待遇为53000",new_salary)
unittest.main()















