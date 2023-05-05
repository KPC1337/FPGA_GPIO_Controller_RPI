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

        self._start_pos = QPoint()
        self._is_dragging = False
        
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
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._start_pos = event.pos()
            self._is_dragging = True
            self.setCursor(Qt.ClosedHandCursor)
            event.accept()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._is_dragging:
            delta = self._start_pos - event.pos()
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() + delta.y())
            self._start_pos = event.pos()
            event.accept()
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self._is_dragging:
            self._is_dragging = False
            self.setCursor(Qt.ArrowCursor)
            event.accept()
        else:
            super().mouseReleaseEvent(event)
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
