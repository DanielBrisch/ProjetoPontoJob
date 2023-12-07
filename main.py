from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, \
    QHBoxLayout

time = 1
user = ''
senha = ''

def codigoRun():
    driver = webdriver.Chrome()

    driver.get("https://www.google.com")

    sleep(time)

    barraGoogle = driver.find_element(By.NAME, "q")
    barraGoogle.send_keys("PontoJob")
    barraGoogle.send_keys(Keys.RETURN)

    sleep(2)

    first_result = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/div/span/a')
    first_result.click()

    sleep(time)

    userPontoJob = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/input')
    userPontoJob.send_keys(user)
    userPontoJob.send_keys(Keys.RETURN)

    senhaPontoJob = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/input')
    senhaPontoJob.send_keys(senha)

    clickAcessar = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div/div/div/div/div/div[3]/button')
    clickAcessar.click()

    sleep(time)

    clickBtnPonto = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div[3]/button')
    clickBtnPonto.click()

    sleep(time)

    # clickBtnPontoConf = driver.find_element(By.XPATH, '//*[@id="react-confirm-alert"]/div/div/div/div/button[1]')
    # clickBtnPontoConf.click()

    sleep(time)

    driver.quit()


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Interface com Inputs Centralizados")
        self.resize(300, 200)

        mainLayout = QVBoxLayout()

        # Configurando o layout do primeiro input
        input1Layout = QHBoxLayout()
        input1Layout.addStretch()
        self.input1 = QLineEdit(self)
        input1Layout.addWidget(self.input1)
        input1Layout.addStretch()
        mainLayout.addLayout(input1Layout)

        # Configurando o layout do segundo input
        input2Layout = QHBoxLayout()
        input2Layout.addStretch()
        self.input2 = QLineEdit(self)
        input2Layout.addWidget(self.input2)
        input2Layout.addStretch()
        mainLayout.addLayout(input2Layout)

        # Configurando o layout do botão salvar
        saveButtonLayout = QHBoxLayout()
        saveButtonLayout.addStretch()
        self.saveButton = QPushButton("Salvar Valores", self)
        self.saveButton.clicked.connect(self.saveValues)
        self.configurarEstiloBotao(self.saveButton)
        saveButtonLayout.addWidget(self.saveButton)
        saveButtonLayout.addStretch()
        mainLayout.addLayout(saveButtonLayout)

        # Configurando o layout do botão iniciar
        startButtonLayout = QHBoxLayout()
        startButtonLayout.addStretch()
        self.startButton = QPushButton("Iniciar PontoJob")
        self.startButton.clicked.connect(codigoRun)
        self.configurarEstiloBotao(self.startButton)
        startButtonLayout.addWidget(self.startButton)
        startButtonLayout.addStretch()
        mainLayout.addLayout(startButtonLayout)

        self.setLayout(mainLayout)

    def configurarEstiloBotao(self, botao):
        botao.setFixedSize(150, 50)
        botao.setStyleSheet(
            "QPushButton {"
            "background-color: #84b6f4;"
            "color: white;"
            "font-size: 16px;"
            "border-radius: 10px;"
            "}"
        )

    def saveValues(self):
        global user, senha
        user = self.input1.text()
        senha = self.input2.text()
        print("Usuário:", user)
        print("Senha:", senha)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())
