
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QSpacerItem, QSizePolicy, QHBoxLayout
from components.CustomWidget import CustomButton, CustomLineEdit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

time = 1


class AppRun(QWidget):
    def __init__(self):
        super().__init__(self, self.user, self.senha)
        global user, senha
        self.user = user
        self.senha = senha
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Interface com Inputs Centralizados")
        self.resize(400, 300)

        mainLayout = QVBoxLayout()

        mainLayout.addStretch()

        self.startButton = CustomButton("Iniciar PontoJob")
        self.startButton.clicked.connect(self.codigoRun)
        mainLayout.addWidget(self.startButton)

        mainLayout.addStretch()

        self.setLayout(mainLayout)
    def codigoRun(self):
        driver = webdriver.Chrome()

        driver.get("http://talentrh.com.br:3000/")

        sleep(time)

        userPontoJob = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/input')
        userPontoJob.send_keys(user)

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