# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets

# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QGridLayout, QMainWindow

class MyWindow(QMainWindow): 
    def __init__(self, parent=None):
        super().__init__(parent)
# quando trabalhamos com herança( QMainWindow ), é indicado chamar o init da super( super().__init__() )
        
        self.central_widget = QWidget() # é umn widget que serve como local para outros widgets(mas ele não consegue receber outros widgets)
        
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Meu Primeiro Software')


        self.botao1 = self.make_button('Botão 1')
        self.botao1.clicked.connect(self.exibe_frase)

        self.botao2 = self.make_button('Botão 2')
        self.botao2.clicked.connect(self.exibe_nome_usuario)

        self.botao3 = self.make_button('Botão 3')
        self.botao3.clicked.connect(self.exibe_print)

        self.grid_layout = QGridLayout()
        # então foi criado um layout que recebe outros widgets
        self.central_widget.setLayout(self.grid_layout)
        # e o layout do central_widget será esse mesmo layout que pode recebe outros widgets

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1) # pode ser adicionado quantos botões desejar
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)

        # statusBar
        self.status_bar = self.statusBar() # adiciona uma barra inferior de status
        self.status_bar.showMessage(f'Mensagem de barra inferior de status') # exibe a mensagem da barra infeiror de status

        # menuBar
        self.Menu = self.menuBar()

        self.primeiroMenu = self.Menu.addMenu('Testando Menu 1')

        self.acao1menu1 = self.primeiroMenu.addAction('ação 1, Menu 1')
        self.acao2menu1 = self.primeiroMenu.addAction('ação 2, Menu 1').triggered.connect(self.exibe_print)
        self.acao3menu1 = self.primeiroMenu.addAction('ação 3, Menu 1')
        ...
        self.segundoMenu = self.Menu.addMenu('Testando Menu 1')

        self.acao1menu2 = self.segundoMenu.addAction('ação 1, Menu 2').triggered.connect(self.exibe_nome_usuario)

        self.acao2menu2 = self.segundoMenu.addAction('ação 2, Menu 2')
        self.acao2menu2.setCheckable(True)
        self.acao2menu2.toggled.connect(self.exibe_checked)

        self.terceiroMenu = self.Menu.addMenu('Testando Menu 1')

        self.acao1menu3 = self.terceiroMenu.addAction('ação 1, Menu 3').triggered.connect(self.exibe_frase)



    # funçao primeiroMenu - ação 2, Menu 1
    @Slot()
    def exibe_print(self):
        num = 1,2,3,4,5,6,7,8,9,10
        for x in num:
            print(x)
        print(':)')

    #função segundoMenu - ação 1, Menu2
    @Slot()
    def exibe_nome_usuario(self):
        print('Teste')

    #função segundomenu - ação 2, Menu 2
    @Slot()
    def exibe_checked(checked):
        print('Está marcado?', checked)

    #função terceiroMenu - ação 1, Menu3
    @Slot()
    def exibe_frase(self):
        print('Funcionou!')

    # função cria botão
    def make_button(self, text):
        btn = QPushButton(text) # (QPushbutton) esse é o botão
        btn.setStyleSheet('font-size: 30px; font-weight: bold; color: blue')
        return btn



        
if __name__ == '__main__':
    app = QApplication(sys.argv) # (QApplication) esse é o próprio app em si, com argumentos(sys.argv)
    window = MyWindow() # inicia a janela
    window.show() # exibe a janela
    app.exec() # executa o loop da aplicação