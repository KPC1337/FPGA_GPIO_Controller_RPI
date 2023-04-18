# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
from gui.widgets import PyIconButton, PyLineEdit, PyDropDown
from gui.core.functions import Functions
class PyGpioMacro(QWidget):
    addMacroClicked = Signal()
    deleteMacroClicked = Signal(QWidget)
    sendButtonClicked = Signal(list)
    saveMacroClicked = Signal(QWidget)
    def __init__(
            self, 
            app_parent,
            parent,
            width = 700,
            height = 60,
            radius = 10,
            colour = "#272c36"
    ):
        super().__init__()

        self.button_states = []

        self.top_level = False

        self._parent = parent
        self._app_parent = app_parent

        self.setMinimumSize(width, height)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet(f"background-color: {colour}; border-radius: {radius}")
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.backgroundWidget = QWidget()
        self.backgroundWidget.setMinimumSize(width, height)
        self.backgroundWidget.setStyleSheet(f"background-color: {colour}; border-radius: {radius}")
        
        self.backgroundWidget.setSizePolicy(sizePolicy)
        self.main_layout.addWidget(self.backgroundWidget)

        self.contentLayout  = QHBoxLayout(self.backgroundWidget)
        self.contentLayout.setContentsMargins(20,15,20,15)
        self.contentLayout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.contentLayout.setSpacing(15)
        self.button_add_macro = PyIconButton(
                        btn_id = "Add Macro",
                        icon_path = Functions.set_svg_icon("icon_plus.svg"),
                        parent = parent,
                        app_parent=app_parent,
                        tooltip_text = "Add Macro",
                        width = 500,
                        height = 40,
                        radius = 10,
                        dark_one = "#1b1e23",
                        icon_color = "#c3ccdf",
                        icon_color_hover = "#dce1ec",
                        icon_color_pressed = "#6c99f4",
                        icon_color_active = "#f5f6f9",
                        bg_color = "#1b1e23",
                        bg_color_hover = "#21252d",
                        bg_color_pressed = "#568af2",
                        context_color = "#272c36",
                    )
        self.contentLayout.addWidget(self.button_add_macro)
        self.button_add_macro.released.connect(lambda: self.on_add_macro_clicked(True))

        self.buttons = []

    def on_add_macro_clicked(self, emitSignal = False):
        self.button_add_macro.setParent(None)
        button = PyIconButton(
                        btn_id = "load_macro",
                        icon_path = Functions.set_svg_icon("icon_load.svg"),
                        parent = self._parent,
                        app_parent= self._app_parent,
                        tooltip_text = "Load Macro",
                        width = 60,
                        height = 40,
                        radius = 10,
                        dark_one = "#1b1e23",
                        icon_color = "#c3ccdf",
                        icon_color_hover = "#dce1ec",
                        icon_color_pressed = "#6c99f4",
                        icon_color_active = "#f5f6f9",
                        bg_color = "#1b1e23",
                        bg_color_hover = "#21252d",
                        bg_color_pressed = "#568af2",
                        context_color = "#272c36",
                    )
        self.buttons.append(button)

        button = PyIconButton(
                        btn_id = "save_macro",
                        icon_path = Functions.set_svg_icon("icon_save.svg"),
                        parent = self._parent,
                        app_parent= self._app_parent,
                        tooltip_text = "Save Macro",
                        width = 60,
                        height = 40,
                        radius = 10,
                        dark_one = "#1b1e23",
                        icon_color = "#c3ccdf",
                        icon_color_hover = "#dce1ec",
                        icon_color_pressed = "#6c99f4",
                        icon_color_active = "#f5f6f9",
                        bg_color = "#1b1e23",
                        bg_color_hover = "#21252d",
                        bg_color_pressed = "#568af2",
                        context_color = "#272c36",
                    )
        self.buttons.append(button)

        button = PyIconButton(
                        btn_id = "delete_macro",
                        icon_path = Functions.set_svg_icon("icon_close.svg"),
                        parent = self._parent,
                        app_parent= self._app_parent,
                        tooltip_text = "Delete Macro",
                        width = 60,
                        height = 40,
                        radius = 10,
                        dark_one = "#1b1e23",
                        icon_color = "#c3ccdf",
                        icon_color_hover = "#dce1ec",
                        icon_color_pressed = "#6c99f4",
                        icon_color_active = "#f5f6f9",
                        bg_color = "#1b1e23",
                        bg_color_hover = "#21252d",
                        bg_color_pressed = "#ff5555",
                        context_color = "#c3ccdf",
                    )
        self.buttons.append(button)     

        # PY LINE EDIT
        self.macro_name = PyLineEdit(
            text = "",
            place_holder_text = "Macro Name",
            radius = 8,
            border_size = 2,
            color = "#8a95aa",
            selection_color = "#f5f6f9",
            bg_color = "#1b1e23",
            bg_color_active = "#21252d",
            context_color = "#568af2"
        )
        self.macro_name.setMinimumHeight(30)
        self.macro_name.setMaximumWidth(300)
        self.contentLayout.addWidget(self.macro_name)

        # self.dropdown = PyDropDown
        if(emitSignal):
            self.addMacroClicked.emit()
        for button in self.buttons:
            button.clicked.connect(self.on_button_clicked)
            self.contentLayout.addWidget(button)
        

    
    def on_button_clicked(self):
        button = self.sender()
        if button.objectName() == "delete_macro":
            for button in self.buttons:
                self.contentLayout.removeWidget(button)
                button.setParent(None)
                self.contentLayout.removeWidget(self.macro_name)
                self.macro_name.setParent(None)
            self.buttons.clear()
            if(self.top_level): 
                self.contentLayout.addWidget(self.button_add_macro)
            else:
                self.button_add_macro.deleteLater()
            self.deleteMacroClicked.emit(self)
        elif button.objectName() == "load_macro":
            self.sendButtonClicked.emit(self.button_states)
            print("send button clicked")
        elif button.objectName() == "save_macro":
            self.saveMacroClicked.emit(self)

    def set_button_states(self, states):
        self.button_states = states

    def get_button_states(self):
        return self.button_states

    def set_top_level(self, state):
        self.top_level = state

    def get_top_level(self):
        return self.top_level
    

