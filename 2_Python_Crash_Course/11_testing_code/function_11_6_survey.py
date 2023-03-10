class AnonymousSurvey():
    """收集匿名调查问卷的答案"""

    def __init__(self,question):
        """存储一个问题，并未存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_respose(self, new_response):
        """存储单份调查问卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷"""
        print("调查结果如下:")
        for response in self.responses:
            print(f"- {response}")









