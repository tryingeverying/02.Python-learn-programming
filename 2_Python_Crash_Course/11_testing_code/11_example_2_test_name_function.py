"""原始函数不能通过的测试"""
import unittest
from function_11_2_name_fuction import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试function_11_2_name_fuction.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,"Janis Joplin")
        # assertEqual 断言函数输出结果和期望值一致

unittest.main()