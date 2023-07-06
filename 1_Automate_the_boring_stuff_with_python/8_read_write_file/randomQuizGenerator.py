#! python3
# randomQuizGenerator.py 生成35份随机排列的美国各州首府的选择题以及对应的答案

import random
'''
创建35份不同的测验试卷。
为每份试卷创建50个多重选择题，次序随机。
为每个问题提供一个正确答案和3个随机的错误答案，次序随机。
将测验试卷写到35个文本文件中。
将答案写到35个文本文件中。
'''

# 包含美国各州及首府的字典
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

basePath = r"F:\Programming\02.Python-learn-programming\1_Automate_the_boring_stuff_with_python\8_read_write_file\test_file\capitals"

# 生成35份问题文件和答案文件
for quitNum in range(35):
    quitFile = open((basePath + r"\quit_%s.txt")%(quitNum+1),'w')
    answerFile = open((basePath + r"\answer_%s.txt")%(quitNum+1),'w')
    
    # 在问题文件中写入姓名，日期之类的固定格式内容
    quitFile.write("name:\n\ndate:\n\nperiod\n\n")
    quitFile.write('-'*20 + f"quit_{quitNum +1}" + '-'*20)
    quitFile.write('\n\n')
    answerFile.write(f"the answer of quit{quitNum+1}\n")

    # 生成一个随机排列的各州州名list，以便实现后面的问题是随机的
    stats = list(capitals.keys())
    random.shuffle(stats)

    for questionNum in range(50):
        # 写入题目
        quitFile.write(f"{questionNum+1}.what is the capitals of {stats[questionNum]}\n")
        
        # 生成答案选项
        correctAnswer = capitals[stats[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        # wrongAnswer.index(correctAnswer)
        # 返回correctAnswer在wrongAnswer中的索引值

        wrongAnswer = random.sample(wrongAnswer,3)
        # random.sample(wrongAnswer,3)
        # 从wrongAnswer中随机选出三个

        # 生成四个随机排列的答案选项,并写入问题文件
        answerOptions = wrongAnswer + [correctAnswer]
        random.shuffle(answerOptions)
        for i in range(4):
            quitFile.write(f"{'ABCD'[i]}.{answerOptions[i]}\n")
        quitFile.write("\n")

        # 将正确答案写入答案文件
        answerFile.write(f"{questionNum+1}.{'ABCD'[answerOptions.index(correctAnswer)]}\n")


    quitFile.close()
    answerFile.close()

