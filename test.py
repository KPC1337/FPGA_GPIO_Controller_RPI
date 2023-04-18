import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

from qt_core import *

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QPushButton {{
	border: none;
    padding-left: 10px;
    padding-right: 5px;
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
}}
QPushButton:hover {{
	background-color: {_bg_color_hover};
}}
QPushButton:pressed {{	
	background-color: {_bg_color_pressed};
}}
'''

# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class CustomButton(QPushButton):
    def __init__(
        self, 
        text,
        radius,
        color,
        bg_color,
        bg_color_hover,
        bg_color_pressed,
        parent = None,
    ):
        super().__init__(parent)

        # SET PARAMETRES
        self.setText(text)
        if parent != None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        # SET STYLESHEET
        custom_style = style.format(
            _color = color,
            _radius = radius,
            _bg_color = bg_color,
            _bg_color_hover = bg_color_hover,
            _bg_color_pressed = bg_color_pressed
        )
        self.setStyleSheet(custom_style)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Example")
        self.setGeometry(100, 100, 400, 300)

        # Create the custom button
        self.button = CustomButton(
            text = "Button Without Icon",
            radius  =8,
            color =  "#2c313c",
            bg_color =  "#2c313c",
            bg_color_hover ="#2c313c",
            bg_color_pressed = "#2c313c",
            parent = self
        )
        self.button.setText("Click Me")

        # Set the button position
        self.update_button_position()

    def update_button_position(self):
        # Get the current size of the window
        window_size = self.size()

        # Get the size of the button
        button_size = self.button.sizeHint()

        # Calculate the position of the button
        button_x = window_size.width() - button_size.width() - 10
        button_y = window_size.height() - button_size.height() - 10

        print(button_x)
        print(button_y)
        print(button_size.width())
        print(button_size.height())

        # Set the button position
        self.button.setGeometry(button_x, button_y, button_size.width(), button_size.height())

    def resizeEvent(self, event):
        # Call the base class resizeEvent handler
        super().resizeEvent(event)

        # Update the position of the button
        self.update_button_position()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
