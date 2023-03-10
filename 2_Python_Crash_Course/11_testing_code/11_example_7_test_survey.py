"""编写一个测试，对AnonymousSurvey 类的行为的一个方面进行验证：
如果用户面对调查问题时只提供了一个答案，这个答案也能被妥善地存储。"""

import unittest
from function_11_6_survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "你的母语是什么"
        my_survey = AnonymousSurvey(question)
        my_survey.store_respose('汉语')

        self.assertIn("汉语",my_survey.responses)

    def test_store_three_response(self):
        """测试三个答案都会被妥善的存储"""
        question = "你的母语是什么"
        my_survey = AnonymousSurvey(question)
        responses = ["汉语","英语","法语",]
        for response in responses:
            my_survey.store_respose(response)

        for response in responses:
            self.assertIn(response,my_survey.responses)

unittest.main()










