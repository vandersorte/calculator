from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)

        self.central_widget = QWidget()
        self.vertical_layout = QVBoxLayout()
        self.central_widget.setLayout(self.vertical_layout)
        self.setCentralWidget(self.central_widget)

        # Título da janela
        self.setWindowTitle('Calculadora')

    # Função para Ajuste de tamanho da janela  
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # função que adiciona um widget ao layout
    def addWidgetToVLayout(self, widget: QWidget):
        self.vertical_layout.addWidget(widget) # adiciona um widget ao layout
        