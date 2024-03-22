from PySide6.QtWidgets import QLineEdit # importação para criar o display da calculadora
from PySide6.QtCore import Qt # importasão do alinhamento do texto(display)
from variables import *

class Display(QLineEdit):
    def __init__(self):
        super().__init__()
        self.confingStyle() # as funções devem ser chamadas dentro da classe 

    def confingStyle(self): # função para estilo do display 
        self.setStyleSheet(
    'font-size: 20px; font-weight: bold;')
        self.setMinimumHeight(MINIMUN_HEIGHT * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight) # alinhar o textodo display à direita
        self.setPlaceholderText('Digite aqui ')
        
        
        margin = [TEXT_MARGIN for _ in range(4)]# Exemplo: TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN
        self.setTextMargins(*margin) # usa o esterisco para desempacotar os valores