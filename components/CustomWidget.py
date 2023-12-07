from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton, QLineEdit, QGraphicsDropShadowEffect

def aplicarSombra(widget):
    sombra = QGraphicsDropShadowEffect()
    sombra.setBlurRadius(10)
    sombra.setXOffset(0)
    sombra.setYOffset(0)
    sombra.setColor(QColor(0, 0, 0, 60))
    widget.setGraphicsEffect(sombra)

class CustomButton(QPushButton):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.configurarEstiloBotao()
        aplicarSombra(self)  # Agora está correto

    def configurarEstiloBotao(self):
        self.setFixedSize(150, 40)
        self.setStyleSheet(
            "QPushButton {"
            "background-color: #84b6f4;"
            "color: white;"
            "font-size: 16px;"
            "border-radius: 10px;"
            "}"
        )

class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.configurarEstiloInput()
        aplicarSombra(self)  # Agora está correto

    def configurarEstiloInput(self):
        self.setFixedSize(200, 30)
        self.setStyleSheet(
            "QLineEdit {"
            "border-radius: 10px;"
            "}"
        )
