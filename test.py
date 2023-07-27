import os
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import *

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create a QVBoxLayout
        layout = QVBoxLayout()

        # Create a QWidget to hold the layout
        widget = QWidget()
        widget.setLayout(layout)

        # Create a QScrollArea
        scroll_area = QScrollArea()

        # Create a QVBoxLayout for the scroll area
        scroll_layout = QVBoxLayout()

        # Create a QWidget to hold the scroll layout
        scroll_widget = QWidget()
        scroll_widget.setLayout(scroll_layout)

        # Create a QGraphicsScene
        scene = QGraphicsScene()

        # Create a QGraphicsView and set the scene
        view = QGraphicsView()
        view.setScene(scene)
        view.setDragMode(QGraphicsView.NoDrag)

        # Create a QGraphicsPixmapItem to display the image
        image_item = QGraphicsPixmapItem()

        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/images"
        filename = "cyclone_2.png"
        image_path = os.path.join(app_path, folder, filename)

        # Load the image
        image = QPixmap(image_path)
        image_item.setPixmap(image)

        # Add the image item to the scene
        scene.addItem(image_item)

        # Create a QPushButton
        button = QPushButton("Button")

        # Create a QGraphicsProxyWidget for the button
        button_proxy = QGraphicsProxyWidget()
        button_proxy.setWidget(button)
        
        # Calculate the position for the button
        button_pos_x = image.width() / 2 - button.width() / 2
        button_pos_y = image.height() / 2 - button.height() / 2
        button_proxy.setPos(button_pos_x, button_pos_y)

        # Add the button proxy to the scene
        scene.addItem(button_proxy)

        scroll_layout.addWidget(view)

        # Add some labels to the scroll layout
        for i in range(10):
            label = QLabel(f"Label {i+1}")
            scroll_layout.addWidget(label)

        # Set the scroll widget as the widget for the scroll area
        scroll_area.setWidget(scroll_widget)

        # Add the QScrollArea to the layout
        layout.addWidget(scroll_area)

        # Set the QWidget as the central widget of the main window
        self.setCentralWidget(widget)

        self.show()

if __name__ == '__main__':
    app = QApplication([])
    window = MyMainWindow()
    app.exec()
