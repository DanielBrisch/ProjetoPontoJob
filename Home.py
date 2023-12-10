import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPainter, QPen
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QGraphicsDropShadowEffect, QApplication

from AppRun import AppRun
from components.CustomWidget import CustomLineEdit, CustomButton

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.user = ''
        self.senha = ''
        self.initUI()

    def initUI(self):
        self.setWindowTitle("AutoJob")
        self.resize(400, 300)

        layout = QVBoxLayout()

        self.InitialText = QLabel("Bem Vindo", self)
        self.InitialText.setAlignment(Qt.AlignCenter)
        self.InitialText.setFont(QFont('Comic Sans MS', 30))
        self.InitialText.setStyleSheet("color: #84b6f4;")

        layout.addWidget(self.InitialText)

        layout.addStretch()

        self.outPutUsuario = QLabel("Usuario", self)
        self.outPutUsuario.setAlignment(Qt.AlignCenter)
        self.outPutUsuario.setFont(QFont('Comic Sans MS', 15))

        layout.addWidget(self.outPutUsuario)

        input1Layout = QHBoxLayout()
        input1Layout.addStretch()
        self.input1 = CustomLineEdit()
        input1Layout.addWidget(self.input1)
        input1Layout.addStretch()
        layout.addLayout(input1Layout)

        self.outPutsenha = QLabel("senha", self)
        self.outPutsenha.setAlignment(Qt.AlignCenter)
        self.outPutsenha.setFont(QFont('Comic Sans MS', 15))

        layout.addWidget(self.outPutsenha)

        input2Layout = QHBoxLayout()
        input2Layout.addStretch()
        self.input2 = CustomLineEdit()
        input2Layout.addWidget(self.input2)
        input2Layout.addStretch()
        layout.addLayout(input2Layout)

        layout.addStretch()

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        self.saveButton = CustomButton("Salvar Valores")
        self.saveButton.clicked.connect(self.saveValues)
        buttonLayout.addWidget(self.saveButton)
        buttonLayout.addStretch()
        layout.addLayout(buttonLayout)

        layout.addStretch()

        self.setLayout(layout)

    def saveValues(self):
        self.user = self.input1.text()
        self.senha = self.input2.text()
        self.openAppRun(self.user, self.senha)  # Passamos user e senha como argumentos

    def openAppRun(self, user, senha):
        self.app_run = AppRun(user, senha)
        self.app_run.show()
        self.close()