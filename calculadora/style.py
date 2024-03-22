import qdarktheme # estilo tema do aplicativo
from variables import *

qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {MINIMUM_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {MEDIUM_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {MAXIMUM_PRIMARY_COLOR};
    }}"""

def DarkTheme():
        qdarktheme.setup_theme(
                theme= 'dark',
                custom_colors={"[dark]": {"primary": f'{MINIMUM_PRIMARY_COLOR}',
                    }, '[light]': {'primary': f'{MINIMUM_PRIMARY_COLOR}',
                },
            },
            additional_qss = qss  
        )  # aplicação do tema