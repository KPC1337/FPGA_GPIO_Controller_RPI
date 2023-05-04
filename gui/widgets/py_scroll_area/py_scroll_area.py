# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT STYLE
# ///////////////////////////////////////////////////////////////
from . style import *

# class for scrollable label
class PyScrollArea(QScrollArea):
    contentArea = QVBoxLayout()
    def __init__(
        self, 
        parent = None,
        radius = 8,
        color = "#FFF",
        bg_color = "#444",
        border_size = 2,
        border_color = "#21252B",
        scroll_bar_bg_color = "#FFF",
        scroll_bar_btn_color = "#333333",
        context_color = "#00ABE8", 
        spacing = 1
    ):
        super().__init__(parent)

        self.setWidgetResizable(True)

        # making qwidget object
        content = QWidget(self)
        content.setStyleSheet(("background-color: {_bg_color}").format(_bg_color = bg_color))
        self.setWidget(content)
        
        # PARAMETERS

        # SET STYLESHEET
        self.set_stylesheet(
            radius,
            color,
            bg_color,
            border_size,
            border_color,
            scroll_bar_bg_color,
            scroll_bar_btn_color,
            context_color
        )

        # vertical box layout
        contentArea = QVBoxLayout(content)
        contentArea.setSpacing(spacing)

        self.contentArea = contentArea

    # the add_widget method
    def add_widget(self, widget, alignment = Qt.AlignHCenter):
        # adding widget to the label
        self.contentArea.addWidget(widget, 0, alignment)

    # SET STYLESHEET
    def set_stylesheet(
        self,
        radius,
        color,
        bg_color,
        border_size,
        border_color,
        scroll_bar_bg_color,
        scroll_bar_btn_color,
        context_color
    ):
        # APPLY STYLESHEET
        style_format = style.format(
            _radius = radius,          
            _color = color,
            _bg_color = bg_color,
            _border_size = border_size,
            _border_color = border_color,
            _scroll_bar_bg_color = scroll_bar_bg_color,
            _scroll_bar_btn_color = scroll_bar_btn_color,
            _context_color = context_color
        )
        self.setStyleSheet(style_format)
