#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

def show_winner():
    num = randint(1,52)
    number.setText(str(num))

#создание элементов интерфейса
app = QApplication([]) #приложение
window = QWidget() #окно

v_line = QVBoxLayout()

q = QLabel('Нажми, чтобы узнать победителя') #Текст
number = QLabel('?') #Цифра
button = QPushButton('Сгенерировать') #Кнопка
button.clicked.connect(show_winner)

v_line.addWidget(q)
v_line.addWidget(number)
v_line.addWidget(button)

window.setLayout(v_line)

window.show() #показать окно
app.exec() #открыть окно
