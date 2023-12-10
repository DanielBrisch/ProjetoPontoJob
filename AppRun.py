from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QSpacerItem, QSizePolicy, QHBoxLayout, QCalendarWidget
from trio._core._thread_cache import WorkerThread

from components.CustomWidget import CustomButton, CustomLineEdit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

time = 2

class AppRun(QWidget):
    def __init__(self, user, senha):
        super(AppRun, self).__init__()
        self.user = user
        self.senha = senha
        self.initUI()

    def initUI(self):
        self.setWindowTitle("AutoJob")
        self.resize(400, 300)

        mainLayout = QVBoxLayout()

        mainLayout.addStretch()

        self.calendar = QCalendarWidget(self)
        mainLayout.addStretch()
        self.calendar.setGridVisible(True)
        mainLayout.addWidget(self.calendar)

        mainLayout.addStretch()

        self.startButton = CustomButton("Iniciar PontoJob")
        self.startButton.clicked.connect(self.codigoRun)
        mainLayout.addWidget(self.startButton)

        mainLayout.addStretch()

        self.setLayout(mainLayout)

    def codigoRun(self):
        self.worker_thread = WorkerThread(self.user, self.senha)
        self.worker_thread.start()

class WorkerThread(QThread):
    def __init__(self, user, senha):
        super(WorkerThread, self).__init__()
        self.user = user
        self.senha = senha

    def run(self):
        driver = webdriver.Chrome()

        driver.get("http://talentrh.com.br:3000/")

        sleep(time)

        userPontoJob = driver.find_element(By.XPATH,
                                           '//*[@id="root"]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/input')
        userPontoJob.send_keys(self.user)

        senhaPontoJob = driver.find_element(By.XPATH,
                                            '//*[@id="root"]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/input')
        senhaPontoJob.send_keys(self.senha)

        clickAcessar = driver.find_element(By.XPATH,
                                           '//*[@id="root"]/div[1]/div/div/div/div/div/div/div/div/div[3]/button')
        clickAcessar.click()

        sleep(time)

        self.element = driver.find_element(By.XPATH,
                                           '//*[@id="root"]/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/div[3]/button')
        clickBtnPonto = self.element
        clickBtnPonto.click()

        sleep(time)

        # clickBtnPontoConf = driver.find_element(By.XPATH, '//*[@id="react-confirm-alert"]/div/div/div/div/button[1]')
        # clickBtnPontoConf.click()
