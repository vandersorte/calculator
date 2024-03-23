import sys
from info import * # texto que aparece na calculadora
from style import * # estilo do tema do aplicativo
from display import * # display dos números digitados para calcular
from buttons import * # importação dos botões
from variables import * # variáveis usadas no aplicativo
from main_window import * # base de criação do aplicativo
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit

# cria o widget label para o layout
def label_layout(text):
    label_1 = QLabel(text) # cria um widget de texto para o layout, recebendo o texto
    label_1.setStyleSheet('font-size: 40px;') # estilo(tipo css)
    return label_1

if __name__ == '__main__':
    # o básico para iniciar um projeto
    app = QApplication(sys.argv)
    window = MainWindow()

    # App Style
    DarkTheme() # Esse é o tema do aplicativo

    # Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)

    # código pego nas respostas da aula para exibir o icone na TaskBar do Windows
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation')
        
    # Info
    info = Info('1 + 1 = 2')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display)
    window.vertical_layout.addLayout(buttonsGrid) # adicionando a grid de botões ao vertical_layout

    # # Button
    # buttonsGrid.addWidget(Buttons('1'), 0, 0) # adicionando o botão à widget da grid de botões 
    # # Também pode ser feito assim

    # Texto no layout           
    # window.addWidgetToVLayout(label_layout(info))

    # Executa tudo
    window.adjustFixedSize() # para a janela permanecer com tamanho fixo
    window.show()
    app.exec()