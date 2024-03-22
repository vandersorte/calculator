from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt # importasão do alinhamento do texto(info)

class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet('font-size: 20px; color: #696969; font-weight: bold;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)