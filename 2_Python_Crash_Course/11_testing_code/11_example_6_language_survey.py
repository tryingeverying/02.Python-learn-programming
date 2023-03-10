from function_11_6_survey import AnonymousSurvey

# 定义一个问题，并且创建一个表示调查的AnonymousSurvey对象
question = '你的母语是什么'
my_survey = AnonymousSurvey(question)

# 显示问题并储存答案
my_survey.show_question()
print("任何时候输入'达咩'终止程序")
while True:
    response = input("语言:")
    if response == "达咩":
        break
    my_survey.store_respose(response)

# 显示调查结果
print("\n 感谢参与调研")
my_survey.show_results()








