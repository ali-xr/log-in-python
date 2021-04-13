import sys
from PyQt5 import QtWidgets, QtGui
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Calculator(QMainWindow): 
  
    def __init__(self): 
        super().__init__() 
  
        # setting title 
        self.setWindowTitle("Python ") 
  
        # setting geometry 
        self.setGeometry(800, 150, 360, 350) 
  
        # calling method 
        self.UiComponents() 
  
        # showing all the widgets 
        self.show() 
  
        # method for widgets 
    def UiComponents(self): 
  
        # creating a label 
        self.label = QLabel(self) 
  
        # BU CONSELGA YOZADIGAN JOYI 5 - bu  chapdan 5 milimetr tashlaydi ||| 6 - bu tepadan 6 milimetr || 350 bu shirina  || 70 esa bu dlina 
        self.label.setGeometry(5, 6, 350, 70) 
  
        # creating label multi line 
        self.label.setWordWrap(True) 
  
        # setting style sheet to the label 
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 5px solid black;"
                                 "background : white ;"
                                 "}") 
  
        # setting alignment to the label 
        self.label.setAlignment(Qt.AlignRight) 
  
        # setting font 
        self.label.setFont(QFont('Arial', 15)) 
  
  
        # adding number button to the screen 
        # creating a push button 
        push1 = QPushButton("1", self) 
  
        # setting geometry 
        push1.setGeometry(5, 150, 80, 40) 
  
        # creating a push button 
        push2 = QPushButton("2", self) 
  
        # setting geometry 
        push2.setGeometry(95, 150, 80, 40) 
  
        # creating a push button 
        push3 = QPushButton("3", self) 
  
        # setting geometry 
        push3.setGeometry(185, 150, 80, 40) 
  
        # creating a push button 
        push4 = QPushButton("4", self) 
  
        # setting geometry 
        push4.setGeometry(5, 200, 80, 40) 
  
        # creating a push button 
        push5 = QPushButton("5", self) 
  
        # setting geometry 
        push5.setGeometry(95, 200, 80, 40) 
  
        # creating a push button 
        push6 = QPushButton("5", self) 
  
        # setting geometry 
        push6.setGeometry(185, 200, 80, 40) 
  
        # creating a push button 
        push7 = QPushButton("7", self) 
  
        # setting geometry 
        push7.setGeometry(5, 250, 80, 40) 
  
        # creating a push button 
        push8 = QPushButton("8", self) 
  
        # setting geometry 
        push8.setGeometry(95, 250, 80, 40) 
  
        # creating a push button 
        push9 = QPushButton("9", self) 
  
        # setting geometry 
        push9.setGeometry(185, 250, 80, 40) 
  
        # creating a push button 
        push0 = QPushButton("0", self) 
  
        # setting geometry 
        push0.setGeometry(5, 300, 80, 40) 
  
        # adding operator push button 
        # creating push button 
        push_equal = QPushButton("=", self) 
  
        # setting geometry 
        push_equal.setGeometry(275, 300, 80, 40) 
  
        # adding equal button a color effect 
        c_effect = QGraphicsColorizeEffect() 
        c_effect.setColor(Qt.blue) 
        push_equal.setGraphicsEffect(c_effect) 
  
        # creating push button 
        push_plus = QPushButton("+", self) 
  
        # setting geometry 
        push_plus.setGeometry(275, 250, 80, 40) 
  
        # creating push button 
        push_minus = QPushButton("-", self) 
  
        # setting geometry 
        push_minus.setGeometry(275, 200, 80, 40) 
  
        # creating push button 
        push_mul = QPushButton("*", self) 
  
        # setting geometry 
        push_mul.setGeometry(275, 150, 80, 40) 
  
        # creating push button 
        push_div = QPushButton("/", self) 
  
        # setting geometry 
        push_div.setGeometry(185, 300, 80, 40) 
  
        # creating push button 
        push_point = QPushButton(".", self) 
  
        # setting geometry 
        push_point.setGeometry(95, 300, 80, 40) 
  
  
        # clear button 
        push_clear = QPushButton("Tozalash", self) 
        push_clear.setGeometry(5, 100, 200, 40) 
    
        # del one character button 
        push_del = QPushButton("O'chirish", self) 
        push_del.setGeometry(210, 100, 145, 40) 
    
        # adding action to each of the button 
        push_minus.clicked.connect(self.action_minus) 
        push_equal.clicked.connect(self.action_equal) 
        push0.clicked.connect(self.son0) 
        push1.clicked.connect(self.son1) 
        push2.clicked.connect(self.son2) 
        push3.clicked.connect(self.son3) 
        push4.clicked.connect(self.son4) 
        push5.clicked.connect(self.son5) 
        push6.clicked.connect(self.son6) 
        push7.clicked.connect(self.son7) 
        push8.clicked.connect(self.son8) 
        push9.clicked.connect(self.son9) 
        push_div.clicked.connect(self.action_div) 
        push_mul.clicked.connect(self.action_mul) 
        push_plus.clicked.connect(self.action_plus) 
        push_point.clicked.connect(self.action_point) 
        push_clear.clicked.connect(self.action_clear) 
        push_del.clicked.connect(self.action_del) 
    
    def action_equal(self): 
    
        # get the label text 
        equation = self.label.text() 
    
        try: 
            # getting the ans 
            ans = eval(equation) 
    
            # setting text to the label 
            self.label.setText(str(ans)) 
    
        except: 
            # setting text to the label 
            self.label.setText("Amalni To'gri tanlang") 
    
    def action_plus(self): 
        # appending label text 
        text = self.label.text() 
        self.label.setText(text + " + ") 
    
    def action_minus(self): 
        # appending label text 
        text = self.label.text() 
        self.label.setText(text + " - ") 
    
    def action_div(self): 
        # appending label text 
        text = self.label.text() 
        self.label.setText(text + " / ") 
    
    def action_mul(self): 
        # appending label text 
        text = self.label.text() 
        self.label.setText(text + " * ") 
    
    def action_point(self): 
        # appending label text 
        text = self.label.text() 
        self.label.setText(text + ".") 
    
    def son0(self): 
        # appending label text 
        text = self.label.text() 
        self.label.setText(text + "0") 
    
    def son1(self): 
        # appending label text 
        text = self.label.text() 
        self.label.setText(text + "1") 
    
    def son2(self): 
        # appending label text 
        text = self.label.text() 
        self.label.setText(text + "2") 
    
    def son3(self): 
        # appending label text 
        text = self.label.text() 
        self.label.setText(text + "3") 
    
    def son4(self): 
        # appending label text 
        text = self.label.text() 
        self.label.setText(text + "4") 
    
    def son5(self): 
        # appending label text 
        text = self.label.text() 
        self.label.setText(text + "5") 
    
    def son6(self): 
        # appending label text 
        text = self.label.text() 
        self.label.setText(text + "6") 
    
    def son7(self): 
        # appending label text 
        text = self.label.text() 
        self.label.setText(text + "7") 
    
    def son8(self): 
        # appending label text 
        text = self.label.text() 
        self.label.setText(text + "8") 
    
    def son9(self): 
        # appending label text 
        text = self.label.text() 
        self.label.setText(text + "9") 
    
    def action_clear(self): 
        # clearing the label text 
        self.label.setText("") 
    
    def action_del(self): 
        # clearing a single digit 
        text = self.label.text() 
        print(text[:len(text)-1]) 
        self.label.setText(text[:len(text)-1]) 
        
class Boshqa_oyna(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.oyna()
        self.boglanish()
    def boglanish(self):
        
        self.bog = sqlite3.connect("LOGINSAYT.db")
        self.kursor = self.bog.cursor()
        sqlSorov = "CREATE TABLE IF NOT EXISTS userlar (login TEXT,ism TEXT, parol TEXT, tasdiq TEXT email TEXT)"
        self.kursor.execute(sqlSorov)
        self.bog.commit()    
        
    def oyna(self):
        self.setWindowTitle("Sign up")
        self.setFixedSize(400,300)
        
        self.panj = None
        
        self.fon = QtWidgets.QLabel()
        self.fon.setPixmap(QtGui.QPixmap("C:\\HELLO.jpg"))
    
        
        self.loginText = QtWidgets.QLabel("Login: ")
        self.ismText = QtWidgets.QLabel("Ism: ")
        self.parolText = QtWidgets.QLabel("Parol: ")
        self.tasdiqText = QtWidgets.QLabel("Parolni tasdiqlang: ")
        self.emailText = QtWidgets.QLabel("Email: ")
        
        
        self.login1 = QtWidgets.QLineEdit()
        self.ism1 = QtWidgets.QLineEdit()
        self.parol1 = QtWidgets.QLineEdit()
        self.tasdiqparol2 = QtWidgets.QLineEdit()
        self.tasdiqparol2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.email1 = QtWidgets.QLineEdit("")
        
        
        self.button1 = QtWidgets.QPushButton("Ro'yxatdan o'tish")
        self.button2 = QtWidgets.QPushButton("KIrish joyiga qaytish")
        self.checkbox1 = QtWidgets.QCheckBox("Shartlarga Roziman")
        
        v_box = QtWidgets.QVBoxLayout()
        f_box = QtWidgets.QHBoxLayout()
        login_box = QtWidgets.QHBoxLayout()
        ism_box = QtWidgets.QHBoxLayout()
        parol_box = QtWidgets.QHBoxLayout()
        tasdiq_box = QtWidgets.QHBoxLayout()
        email_box = QtWidgets.QHBoxLayout()
        d_box = QtWidgets.QHBoxLayout()
        
        f_box.addWidget(self.fon)
        login_box.addWidget(self.loginText)
        login_box.addWidget(self.login1)
        ism_box.addWidget(self.ismText)
        ism_box.addWidget(self.ism1)
        parol_box.addWidget(self.parolText)
        parol_box.addWidget(self.parol1)
        tasdiq_box.addWidget(self.tasdiqText)
        tasdiq_box.addWidget(self.tasdiqparol2)
        email_box.addWidget(self.emailText)
        email_box.addWidget(self.email1)
        
        d_box.addWidget(self.button1)
        d_box.addWidget(self.button2)
        d_box.addWidget(self.checkbox1)
        
        v_box.addLayout(f_box)
        v_box.addLayout(login_box)
        v_box.addLayout(ism_box)
        v_box.addLayout(parol_box)
        v_box.addLayout(tasdiq_box)
        v_box.addLayout(email_box)
        v_box.addLayout(d_box)
        
        self.setLayout(v_box)
        
        self.button1.clicked.connect(self.kir)
        self.button2.clicked.connect(self.ortga)
        
        self.show()
    def ortga(self):
        if self.panj == None:
            self.panj = Panjara()
            self.hide()
    def kir(self):
        login = self.login1.text()
        ism = self.ism1.text()
        parol = self.parol1.text()
        email = self.email1.text()

        sqlSorov = "INSERT INTO userlar VALUES (?, ?, ?, ?)"
        self.kursor.execute(sqlSorov, ( login, ism, parol, email))
        self.bog.commit()         

        data = self.kursor.fetchall()
        if self.checkbox1.isChecked() == True:
            if len(data) == 0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Muvafiqiyatli ")
                msg.setInformativeText("Tizimga ma'lumotlar qo'shildi ")
                msg.setWindowTitle("DIQQAT !!!")
                x = msg.exec_()
            else: 
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("XATOOO")
                msg.setInformativeText("Tizimga kirmadi ")
                msg.setWindowTitle("DIQQAT !!!")
                x = msg.exec_()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Muvaffaqiyatsiz !!!")
            msg.setInformativeText("Shartlarni qabul qilin")
            msg.setWindowTitle("Diqqat !!")
            x = msg.exec_()

class Panjara(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.boglanish()
        self.init_ui()
        
    def boglanish(self):
        self.bog = sqlite3.connect("LOGINSAYT.db")
        self.kursor = self.bog.cursor()
        sqlSorov = "CREATE TABLE IF NOT EXISTS userlar (login TEXT,ism TEXT, parol TEXT, email TEXT)"
        self.kursor.execute(sqlSorov)
        self.bog.commit()
        
    def init_ui(self):
        self.setWindowTitle("Sign in / @akhmadovnazarbek")
        self.setFixedSize(400, 300)
        
        self.fon = QtWidgets.QLabel()
        self.fon.setPixmap(QtGui.QPixmap("C:\\WELCOME.jpg"))
        
        self.oyna = None
        self.calc = None
        
        self.loginText = QtWidgets.QLabel("Login: ")
        self.parolText = QtWidgets.QLabel("Parol: ")
        
        self.login1 = QtWidgets.QLineEdit()
        self.parol1 = QtWidgets.QLineEdit()
        self.parol1.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.label = QtWidgets.QLabel("Boshqa oyna")
 
        
        self.button1 = QtWidgets.QPushButton("Kirish")
        self.button2 = QtWidgets.QPushButton("Ro'yxatdan o't")

        v_box = QtWidgets.QVBoxLayout()
        h_box = QtWidgets.QHBoxLayout()
        t_box = QtWidgets.QHBoxLayout()
        y_box = QtWidgets.QHBoxLayout()
        
        
        v_box.addWidget(self.fon)
        h_box.addWidget(self.loginText)
        h_box.addWidget(self.login1)
        t_box.addWidget(self.parolText)
        t_box.addWidget(self.parol1)        
        y_box.addWidget(self.button1)
        y_box.addWidget(self.button2)

        
        v_box.addLayout(h_box)
        v_box.addLayout(t_box)
        v_box.addLayout(y_box)
    
    
        self.setLayout(v_box)
        
        self.button1.clicked.connect(self.tizimgaKir)
        self.button2.clicked.connect(self.royxatdan_ot)
        
        
        self.show()

    def tizimgaKir(self):
        ism = self.login1.text()
        parol = self.parol1.text()
        
        sqlSorov = "SELECT * FROM userlar WHERE login = ? and parol = ?"
        self.kursor.execute(sqlSorov, (ism, parol))
        
        data = self.kursor.fetchall()
        
        if len(data) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("XATO !!!")
            msg.setInformativeText("Login yoki parol xato")
            msg.setWindowTitle("Diqqat!!!")
            msg.setDetailedText("Xato:\nLogin yoki parol topilmadi")
            x = msg.exec_()
        else:
            self.calc = None
            self.calc = Calculator()
            self.hide()
    def royxatdan_ot(self):
        if self.oyna == None:
            self.oyna = Boshqa_oyna()
            self.hide()
            #self.show()
        

app = QtWidgets.QApplication(sys.argv)

panjara = Panjara()

sys.exit(app.exec_())
