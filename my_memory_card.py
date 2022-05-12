#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QRadioButton,QButtonGroup, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton)
from random import shuffle,randint
class Question():
    def __init__(self,question,right_answer, wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
q = Question('2+2=?' ,'4' ,'1', '2', '3') 
question_list = []
question_list.append(q)
q1 = Question('Государственный язык Аргентины','Испанский','Английский', 'Португальский', 'Итальянский')
question_list.append(q1)
q2 = Question('Государственный язык Бразилии','Португальский','Английский', 'Испанский', 'Итальянский')
question_list.append(q2)
q3 = Question('Государственный язык Уругвая', 'Испанский','Английский', 'Португальский', 'Итальянский')
question_list.append(q3)
q4 = Question('Государственный язык России', 'Русский','Английский', 'Португальский', 'Итальянский')
question_list.append(q4)
q5 = Question('Государственный язык Сенегала', 'Французкий','Английский', 'Португальский', 'Итальянский')
question_list.append(q5)
q6 = Question('Где находится Египет', 'В Африке','В Юж.Америке', 'В Азии', 'В Европе')
question_list.append(q6)








app= QApplication([])
main_win =QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(600,400)

RadioGroupBox = QGroupBox('Варианты ответов')
question = QLabel('Какой национальности не существует?')
btn_answer1 = QRadioButton('Энцы')
btn_answer2 = QRadioButton('Чулымцы')
btn_answer3 = QRadioButton('Смурфы')
btn_answer4 = QRadioButton('Алеуты')

hl1= QHBoxLayout()
hl2= QHBoxLayout()
hl1.addWidget(btn_answer1)
hl1.addWidget(btn_answer2)
hl2.addWidget(btn_answer3)
hl2.addWidget(btn_answer4)

RadioGroup = QButtonGroup() 
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)
vl= QVBoxLayout()

vl.addLayout(hl1)
vl.addLayout(hl2)

RadioGroupBox.setLayout(vl)


ans_GroupBox = QGroupBox('Результат теста')
ans1 = QLabel('Правильно/Неправильно')
ans2 = QLabel('Правильный ответ')


vl2 = QVBoxLayout()
vl2.addWidget(ans1)
vl2.addWidget(ans2)
ans_GroupBox.setLayout(vl2)
ans_GroupBox.hide()
l1 = QLabel
l2 = QLabel
btn = QPushButton('Ответить')

layout_main = QVBoxLayout()
layout_main.addWidget(question)
layout_main.addWidget(RadioGroupBox)
layout_main.addWidget(ans_GroupBox)


layout_main.addWidget(btn)

main_win.setLayout(layout_main)


def show_quetion():
    btn.setText('Ответить')
    ans_GroupBox.hide()
    RadioGroupBox.show()
    RadioGroup.setExclusive(False)    
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)
def show_results():
    btn.setText('Следующий вопрос')
    ans_GroupBox.show()
    RadioGroupBox.hide()
    


answers = [ btn_answer1,btn_answer2,btn_answer3,btn_answer4]
RadioGroup.setExclusive(True)
def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    ans2.setText(q.right_answer)
    show_quetion()

def show_correct(res):
    ans1.setText(res)
    show_results()
def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно")
        main_win.score += 1
        print('Статистика', '\n Всего вопросов:'+str(main_win.total), '\n Всего правильных ответов:',str(main_win.score))
        print ('Рейтинг', main_win.score/main_win.total*100, '%')

    else:
        show_correct("Неправильно")
        print('Неверно')
        print ('Рейтинг', main_win.score/main_win.total*100, '%')
    
       
def next_question():
    
    main_win.total += 1
    print('Статистика', '\n Всего вопросов:'+str(main_win.total), '\n Всего правильных ответов:',str(main_win.score))
    cur_question = randint(0, len(question_list) -1)
    q = question_list[cur_question]

    ask(q)

def click_OK():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()

btn.clicked.connect(click_OK)

main_win.score = 0 
main_win.total = 0 
next_question()
main_win.show()
app.exec_()





