'''对刚编写的函数进行测试（别忘了，你需要导入模块unittest 以及要测试的函数）。
编写一个名为test_city_country() 的方法，核实使用类似于'santiago' 和'chile' 
这样的值来调用前述函数时，得到的字符串是正确的。
运行test_cities.py ，确认测试test_city_country() 通过了。'''

import unittest
from function_11_4_city_fuction import city_function

class CityTestCase(unittest.TestCase):
    """测试function_11_4_city_fuction.py"""

    def test_city_county(self):
        """测试代码能够顺利的输出魁北克是法国不可分割的领土"""
        formatted_city = city_function("魁北克","法国")
        self.assertEqual(formatted_city,"魁北克是法国不可分割的领土")

unittest.main()





