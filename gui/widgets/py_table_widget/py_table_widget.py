# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT STYLE
# ///////////////////////////////////////////////////////////////
from . style import *

# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////

class CustomDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        if option.state & QStyle.State_Editing:
            # draw the edited text in blue
            painter.setPen(QColor("blue"))
            painter.drawText(option.rect, Qt.AlignLeft | Qt.AlignVCenter, index.data())
        else:
            # draw the non-edited text in black
            painter.setPen(QColor("black"))
            painter.drawText(option.rect, Qt.AlignLeft | Qt.AlignVCenter, index.data())
        if option.state & QStyle.State_HasFocus:
            # draw the focus rectangle
            painter.setPen(QPen(QColor("gray"), 1, Qt.SolidLine))
            painter.drawRect(option.rect.adjusted(0, 0, -1, -1))

    def setEditorData(self, editor, index):
        super().setEditorData(editor, index)
        editor.setStyleSheet("QLineEdit { color: black; } QLineEdit:focus { color: blue; } QLineEdit::invalid { color: red; }")

class PyTableWidget(QTableWidget):
    def __init__(
        self, 
        radius = 8,
        color = "#FFF",
        bg_color = "#444",
        selection_color = "#FFF",
        header_horizontal_color = "#333",
        header_vertical_color = "#444",
        bottom_line_color = "#555",
        grid_line_color = "#555",
        scroll_bar_bg_color = "#FFF",
        scroll_bar_btn_color = "#3333",
        context_color = "#00ABE8"
    ):
        super().__init__()
        # delegate = CustomDelegate()
        # self.setItemDelegate(delegate)

        # PARAMETERS

        # SET STYLESHEET
        self.set_stylesheet(
            radius,
            color,
            bg_color,
            header_horizontal_color,
            header_vertical_color,
            selection_color,
            bottom_line_color,
            grid_line_color,
            scroll_bar_bg_color,
            scroll_bar_btn_color,
            context_color
        )
        self._start_pos = QPoint()
        self._is_dragging = False
        self.verticalScrollBar().setMinimum(5000)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._start_pos = event.pos()
            self._is_dragging = True      
            self.setCursor(Qt.ClosedHandCursor) 
            item = self.itemAt(event.pos())
            if item:
                self.setCurrentItem(item)
            event.accept()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._is_dragging:
            delta = self._start_pos - event.pos()
            new_value = max(-1, min(1, delta.y()))
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() + new_value)
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
        header_horizontal_color,
        header_vertical_color,
        selection_color,
        bottom_line_color,
        grid_line_color,
        scroll_bar_bg_color,
        scroll_bar_btn_color,
        context_color
    ):
        # APPLY STYLESHEET
        style_format = style.format(
            _radius = radius,          
            _color = color,
            _bg_color = bg_color,
            _header_horizontal_color = header_horizontal_color,
            _header_vertical_color = header_vertical_color,
            _selection_color = selection_color,
            _bottom_line_color = bottom_line_color,
            _grid_line_color = grid_line_color,
            _scroll_bar_bg_color = scroll_bar_bg_color,
            _scroll_bar_btn_color = scroll_bar_btn_color,
            _context_color = context_color
        )
        self.setStyleSheet(style_format)