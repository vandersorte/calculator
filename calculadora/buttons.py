from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import *
from style import *
from utils import *
from display import *
from info import *

class Buttons(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        
    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        font.setBold(True)
        self.setFont(font)
        # self.setCheckable(True)

class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display,info: Info, *args, **kwargs): # passando o acesso do display do aplicativo para a grid
        super().__init__(*args, **kwargs)

        self.gridMask = [
                ['C', '◀', '^', '/'],
                ['7', '8', '9', '*'],
                ['4', '5', '6', '-'],
                ['1', '2', '3', '+'],
                ['',  '0', '.', '='],
            ]
        self.display = display # passando o acesso do display do aplicativo para a grid
        self.info = info
        self.makeGrid()

    def makeGrid(self):
        for rowNumber, rowData in enumerate(self.gridMask):
            for colNumber, buttonText in enumerate(rowData):
                button = Buttons(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, rowNumber, colNumber)# adicionando botões, linhas e colunas à grid
                buttonSlot = self.makeButtonDisplaySlot(self.insertButtonTextToDisplay, button) 
                # essa viaravel(buttonSlot) acima está chamando o método makeButtonDisplaySLot
                
                button.clicked.connect(buttonSlot)
    
    def makeButtonDisplaySlot(self, func, *args, **kwargs):
        # esse método(makeButtonDisplaySlot) cria uma função(realSlot) 
        def realSlot(_): # essa função(realSlot) será o slot real dos botões
            func(*args, **kwargs) 
            # dentro de(realSlot) é executado a função(func) passando pra ela *args, **kwargs
        return realSlot

    def insertButtonTextToDisplay(self, button):
        buttonText = button.text()

        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)
        # print(button.text(), checked)
        