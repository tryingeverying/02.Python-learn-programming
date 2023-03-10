import unittest
from function_11_6_survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self) -> None:
        """创建一个调查对象鹤一组答案，共使用的测试方法调用"""
        question = "你的母语是什么"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["汉语","英语","法语",]
    
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_respose(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_response(self):
        """测试三个答案都会被妥善的存储"""

        for response in self.responses:
            self.my_survey.store_respose(response)

        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()













