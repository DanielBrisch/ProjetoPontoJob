import ctypes
from ctypes import wintypes
from datetime import datetime
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from trio._core._thread_cache import WorkerThread

from components.CustomWidget import CustomButton
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

time = 2

def is_workstation_locked():
    UOI_NAME = 2
    hDesktop = ctypes.windll.user32.OpenInputDesktop(0, False, 256)
    if hDesktop == 0:
        return True

    lengthNeeded = wintypes.DWORD()
    ctypes.windll.user32.GetUserObjectInformationW(hDesktop, UOI_NAME, None, 0, ctypes.byref(lengthNeeded))
    name = ctypes.create_unicode_buffer(lengthNeeded.value)
    ctypes.windll.user32.GetUserObjectInformationW(hDesktop, UOI_NAME, name, lengthNeeded.value, ctypes.byref(lengthNeeded))
    ctypes.windll.user32.CloseDesktop(hDesktop)

    return name.value != "Default"

class SchedulerThread(QThread):
    def __init__(self, action, hour, minute):
        super(SchedulerThread, self).__init__()
        self.action = action
        self.target_time = datetime.time(hour, minute)

    def run(self):
        while True:
            now = datetime.datetime.now().time()
            if now.hour == self.target_time.hour and now.minute == self.target_time.minute:
                if not is_workstation_locked():
                    self.action()  # Executa a ação
                    time.sleep(60)  # Pausa por um minuto para evitar múltiplas execuções
            time.sleep(10)

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

def main():
    if not is_workstation_locked():
        user = "seu_usuario"
        senha = "sua_senha"
        worker = WorkerThread(user, senha)
        worker.start()
        worker.wait()