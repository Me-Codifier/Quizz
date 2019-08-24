from urllib.request import urlopen
import random

r = urlopen("https://raw.githubusercontent.com/Me-Codifier/Quizz/master/quiz.txt")

Q_number = random.randint(1,7)
print(Q_number)

for line in r:
        line = line.decode("utf-8")
        question = line.split("/")
        if question[0] == str(Q_number):
                print(question[1])
                print('A) ' + question[2])
                print('B) ' + question[3])
                print('C) ' + question[4])
                answer = input('>>>>')
                # print(answer == question[5].strip('\r\n'))
                if answer == question[5].strip('\r\n'):
                        print('Right answer')
                else:
                        print('Wrong Answer')
        
