
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QSpacerItem, QSizePolicy, QHBoxLayout
from components.CustomWidget import CustomButton, CustomLineEdit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

time = 1
user = ''
senha = ''

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.user = ''
        self.senha = ''
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Interface com Inputs Centralizados")
        self.resize(400, 300)  # Pode ajustar para o tamanho desejado

        mainLayout = QVBoxLayout()

        mainLayout.addStretch()

        input1Layout = QHBoxLayout()
        input1Layout.addStretch()
        self.input1 = CustomLineEdit()
        input1Layout.addWidget(self.input1)
        input1Layout.addStretch()
        mainLayout.addLayout(input1Layout)

        input2Layout = QHBoxLayout()
        input2Layout.addStretch()
        self.input2 = CustomLineEdit()
        input2Layout.addWidget(self.input2)
        input2Layout.addStretch()
        mainLayout.addLayout(input2Layout)

        self.saveButton = CustomButton("Salvar Valores")
        self.saveButton.clicked.connect(self.saveValues)
        mainLayout.addWidget(self.saveButton)

        self.startButton = CustomButton("Iniciar PontoJob")
        self.startButton.clicked.connect(self.codigoRun)
        mainLayout.addWidget(self.startButton)

        mainLayout.addStretch()

        self.setLayout(mainLayout)

    def saveValues(self):
        global user, senha
        user = self.input1.text()
        senha = self.input2.text()

    def codigoRun(self):
        driver = webdriver.Chrome()

        driver.get("https://www.google.com")

        sleep(time)

        barraGoogle = driver.find_element(By.NAME, "q")
        barraGoogle.send_keys("PontoJob")
        barraGoogle.send_keys(Keys.RETURN)

        sleep(4)

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

        self.element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div[3]/button')
        clickBtnPonto = self.element
        clickBtnPonto.click()

        sleep(time)

        # clickBtnPontoConf = driver.find_element(By.XPATH, '//*[@id="react-confirm-alert"]/div/div/div/div/button[1]')
        # clickBtnPontoConf.click()

        sleep(time)

        driver.quit()