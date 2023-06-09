import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QComboBox, QGridLayout, QLabel, QLineEdit, QPushButton, QWidget
from database import add_data

class School(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Добавление ученика")
        self.setFixedSize(640, 480)
    
        self.number_class = QComboBox()
        self.number_class.addItem("1")
        self.number_class.addItem("2")
        self.number_class.addItem("3")
        self.number_class.addItem("4")
        self.number_class.addItem("5")
        self.number_class.addItem("6")
        self.number_class.addItem("7")
        self.number_class.addItem("8")
        self.number_class.addItem("9")
        self.number_class.addItem("10")
        self.number_class.addItem("11")
        
        self.index_class = QComboBox()
        self.index_class.addItem("А")
        self.index_class.addItem("Б")
        self.index_class.addItem("В")
        self.index_class.addItem("Г")
        self.index_class.addItem("Д")
    
        
        layout = QGridLayout()
        self.lbl = QLabel("Добавить ученика")
        self.lbl_1 = QLabel("ФИО")
        self.full_name = QLineEdit()
        self.lbl_3 = QLabel("Класс")
        self.lbl_4 = QLabel("Индекс класса")
        self.btn_add = QPushButton("Добавить")
        self.btn_exit = QPushButton("Выход")
        self.btn_add_index = QPushButton("Добавить индекс")
    
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        layout.addWidget(self.lbl_1, 0,0)
        layout.addWidget(self.lbl_3, 1,0)
        layout.addWidget(self.lbl_4, 2,0)
        layout.addWidget(self.full_name, 0,2)
        layout.addWidget(self.number_class, 1,2)
        layout.addWidget(self.index_class, 2,2)
        layout.addWidget(self.btn_add,3,3)
        layout.addWidget(self.btn_add_index, 3,2)
        layout.addWidget(self.btn_exit, 3,0)
        
        self.btn_add.clicked.connect(self.btn_add_click)
        self.btn_exit.clicked.connect(self.btn_exit_click)
        self.btn_add_index.clicked.connect(self.btn_add_index_click)
        
    def btn_add_index_click(self):
        pass
        
    def btn_add_click(self):
        full_name = self.full_name.text()
        number_class = self.number_class.currentText()
        index_class = self.index_class.currentText()
        add_data(full_name, number_class, index_class)
        
        
    def btn_exit_click(self):
        app.exit()
       
app = QApplication(sys.argv)
ex = School()
ex.show()
app.exec()
