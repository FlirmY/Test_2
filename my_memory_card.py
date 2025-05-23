from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
     QApplication, QWidget, QRadioButton , QLabel , QVBoxLayout , QHBoxLayout, QMessageBox , QPushButton , QGroupBox, QButtonGroup   
)
from random import shuffle, choice


class Question():
     def __init__(self, quest , r_answer , w_a1 , w_a2 , w_a3):
          self.question = quest
          self.right_answer = r_answer 
          self.wrong_answer1 = w_a1
          self.wrong_answer2 = w_a2
          self.wrong_answer3 = w_a3  



def next_question():
     random_question = choice(questions)
     ask(random_question)



def show_results():
     Group.hide()
     Group2.show()
     button.setText('Следующий вопрос')
     
def show_question():
     Group2.hide()
     Group.show()
     button.setText('Ответить')
     RadioGroup.setExclusive(False)
     r1_btn.setChecked(False)
     r2_btn.setChecked(False)
     r3_btn.setChecked(False)
     r4_btn.setChecked(False)
     RadioGroup.setExclusive(True)

def start_test():
     if button.text() == ('Ответить'):
          check_answer()
     elif button.text() == ('Следующий вопрос'):
          next_question()




def ask (quest: Question):
     shuffle(buttons)
     buttons[0].setText(quest.right_answer)
     buttons[1].setText(quest.wrong_answer1)
     buttons[2].setText(quest.wrong_answer2)
     buttons[3].setText(quest.wrong_answer3)
     text.setText(quest.question)
     right_answer.setText(quest.right_answer)
     show_question()
     window.total_question += 1

def check_answer ():
     if buttons[0].isChecked():
          answer.setText('Правильно')
          show_results()
          window.correct_answers += 1
          raiting = ((window.correct_answers)/(window.total_question))*100
          print('Статистика')
          print('-Всего вопросов:', window.total_question)
          print('-Правильных ответов:', window.correct_answers)
          print('Рейтинг:', raiting)

     elif  buttons[1].isChecked() or buttons[2].isChecked() or buttons[3].isChecked():
          answer.setText('Неправильно')
          show_results()
          raiting = ((window.correct_answers)/(window.total_question))*100
          print('Статистика')
          print('-Всего вопросов:', window.total_question)
          print('-Правильных ответов:', window.correct_answers)
          print('Рейтинг:', raiting,('%'))

app = QApplication([])
window = QWidget()
window.correct_answers = 0
window.total_question= 0
window.setWindowTitle('Мемори')
window.resize(600,300)


v1_line = QVBoxLayout()#зоздание линий главного окна 
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()
h3_line = QHBoxLayout() 

v1_line.addLayout(h1_line)
v1_line.addLayout(h2_line)
v1_line.addLayout(h3_line)



text = QLabel('Вопрос')#создание виджетов главного окна
button = QPushButton('Ответить')
Group = QGroupBox('Варианты')
Group2 = QGroupBox('Результаты теста')
Group2.hide()

h1_line.addWidget(text) #подключение виджетов к линиям в главном окне
h2_line.addWidget(Group)
h2_line.addWidget(Group2)
h3_line.addStretch(1)
h3_line.addWidget(button, stretch=2)
h3_line.addStretch(1)

r1_btn = QRadioButton('А')#создание виджетов ответов
r2_btn = QRadioButton('Б')
r3_btn = QRadioButton('В')
r4_btn = QRadioButton('Г')

buttons = [r1_btn,r2_btn,r3_btn,r4_btn]
shuffle(buttons)


RadioGroup = QButtonGroup()
RadioGroup.addButton(r1_btn)
RadioGroup.addButton(r2_btn)
RadioGroup.addButton(r3_btn)
RadioGroup.addButton(r4_btn)

gr_v1_line = QVBoxLayout()#создание линий в группе
gr_v2_line = QVBoxLayout()
gr_h1_line = QHBoxLayout()



right_answer = QLabel('Правильный ответ')
answer = QLabel('Правильно/Неправильно')


gr2_v1_line = QVBoxLayout()
gr2_v1_line.addWidget(right_answer)
gr2_v1_line.addWidget(answer, alignment = Qt.AlignCenter)



gr_v1_line.addWidget(r1_btn)
gr_v1_line.addWidget(r2_btn)
gr_v2_line.addWidget(r3_btn)
gr_v2_line.addWidget(r4_btn)

gr_h1_line.addLayout(gr_v1_line)
gr_h1_line.addLayout(gr_v2_line)


button.clicked.connect(start_test)

Group.setLayout(gr_h1_line)
Group2.setLayout(gr2_v1_line)
window.setLayout(v1_line)



questions = []
questions.append(Question('Сколько зубов у человека',
                         '32',
                         '75',
                         '60',
                         '53'))
questions.append(Question('Какое животное лучший друг человека',
                         'собака',
                         'голубь',
                         'синий кит',
                         'корова'))
questions.append(Question('Самая высокая гора в мире',
                         'Эверест',
                         'Эльбрус',
                         'Лхоцзе',
                         'Канченджанга'))
questions.append(Question('Кто открыл Амереку',
                         'Христофор Калумб',
                         'Марко Поло',
                         'Петр 1',
                         'Гамо Васко да'))
questions.append(Question('в каком году распался СССР',
                         '1991',
                         '1945',
                         '1989',
                         '2000'))
questions.append(Question('температура кипячения воды',
                         '100 градусов C',
                         '1000 градусов C',
                         '50 градусов C',
                         '65 градусов C'))
questions.append(Question('сколько бит в 1 байте',
                         '8',
                         '16',
                         '32',
                         '64'))
                         
next_question()


window.show()
app.exec()