# ! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random 

# 问题的内容
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 
'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 
'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
 'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 
 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 
 'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 
 'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville',
 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 
 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# 创建35个文件
for quizNum in range(2):
    # Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
    # Write out the header for the quiz. 
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    # Shuffle the order of the states.
    states = list(capitals.keys()) 
    random.shuffle(states) #random.shuffle(states)把states给随机打乱

    for questionNum in range(50):
        # Get right and wrong answers. 
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values()) 
        del wrongAnswers[wrongAnswers.index(correctAnswer)] #wrongAnswers.index(correctAnswer) 返回correctAnswer对应的索引值
        wrongAnswers = random.sample(wrongAnswers, 3) #random.sample(wrongAnswers, 3) 从wrongAnswers中取出一个长度为3的list，且不改变wrongAnswers
        answerOptions = wrongAnswers + [correctAnswer] 
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,states[questionNum])) 
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
        # Write the answer key to a file.  
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
quizFile.close()
answerKeyFile.close()































