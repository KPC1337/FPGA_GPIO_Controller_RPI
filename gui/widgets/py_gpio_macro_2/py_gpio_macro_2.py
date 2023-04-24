# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
from gui.widgets import PyIconButton, PyLineEdit, PyDropDown
from gui.core.functions import Functions
import csv

class PyGpioMacro2(QWidget):
    addMacroClicked = Signal()
    deleteMacroClicked = Signal(QWidget)
    sendButtonClicked = Signal(list)
    saveMacroClicked = Signal(QWidget, list)
    dropDownClicked = Signal(list)
    def __init__(
            self, 
            app_parent,
            parent,
            name,
            dropdownval,
            width = 700,
            height = 60,
            radius = 10,
            colour = "#272c36",
            last_item = False
    ):
        super().__init__()

        self.button_states = []

        self.top_level = False

        self._parent = parent
        self._app_parent = app_parent

        self._name = name

        self._dropDownVal = dropdownval
        print(self._dropDownVal)

        self.customProfileType = 'Custom Profile (*.csv)'

        self._last_item = last_item



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
        self.contentLayout.setSpacing(10)
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
        if(last_item == False):
            self.on_add_macro_clicked(False)


    def on_add_macro_clicked(self, emitSignal = False):
        self.button_add_macro.setParent(None)

        # PY LINE EDIT
        self.macro_name = PyLineEdit(
            text = self._name,
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
        self.macro_name.setMaximumWidth(200)
        self.contentLayout.addWidget(self.macro_name)

        # com port selection dropdown
        self.dropdown = PyDropDown(
            bg_color = "#1B1D23",
            radius = 8,
            border_size = 2,
            border_color = "#21252B",
            hover_color = "#404758",
            item_text_color = "#dce1ec",
            item_background_color = "#21252B",
            selection_background_colour = "#272C36",
            border_right_color = "#568af2",
            width = 25
        )

        self.dropdown.setMaximumSize(300, 40)

        for item in self._dropDownVal.keys():
            self.dropdown.addItem(item)
        
        self.dropdown.activated.connect(self.onMacroDropClick)

        self.contentLayout.addWidget(self.dropdown)

        self.btn_load_macro = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_load.svg"),
            btn_id="load_macro",
            parent = self._parent,
            app_parent = self._app_parent,
            tooltip_text = "Load Macro",
            width = 40,
            height = 30,
            radius = 10,
            dark_one = "#1b1e23",
            icon_color = "#c3ccdf",
            icon_color_hover = "#dce1ec",
            icon_color_pressed = "#6c99f4",
            icon_color_active = "#f5f6f9",
            bg_color = "#1b1e23",
            bg_color_hover = "#21252d",
            bg_color_pressed =  "#568af2"
        )
        self.btn_load_macro.clicked.connect(self.onButtonClicked)
        self.contentLayout.addWidget(self.btn_load_macro)

        self.btn_save_macro = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_save.svg"),
            btn_id="save_macro",
            parent = self._parent,
            app_parent = self._app_parent,
            tooltip_text = "Save Macro",
            width = 40,
            height = 30,
            radius = 10,
            dark_one = "#1b1e23",
            icon_color = "#c3ccdf",
            icon_color_hover = "#dce1ec",
            icon_color_pressed = "#6c99f4",
            icon_color_active = "#f5f6f9",
            bg_color = "#1b1e23",
            bg_color_hover = "#21252d",
            bg_color_pressed =  "#568af2"
        )
        self.btn_save_macro.clicked.connect(self.onButtonClicked)
        self.contentLayout.addWidget(self.btn_save_macro)

        self.btn_change_macro = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_folder_open.svg"),
            parent = self._parent,
            app_parent = self._app_parent,
            tooltip_text = "Import User Macro",
            width = 40,
            height = 30,
            radius = 10,
            dark_one = "#1b1e23",
            icon_color = "#c3ccdf",
            icon_color_hover = "#dce1ec",
            icon_color_pressed = "#6c99f4",
            icon_color_active = "#f5f6f9",
            bg_color = "#1b1e23",
            bg_color_hover = "#21252d",
            bg_color_pressed =  "#568af2"
        )
        self.btn_change_macro.clicked.connect(self.openUserProfile)
        self.contentLayout.addWidget(self.btn_change_macro)

        self.btn_save_macro_csv = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_folder.svg"),
            parent = self._parent,
            app_parent = self._app_parent,
            tooltip_text = "Export User Macro",
            width = 40,
            height = 30,
            radius = 10,
            dark_one = "#1b1e23",
            icon_color = "#c3ccdf",
            icon_color_hover = "#dce1ec",
            icon_color_pressed = "#6c99f4",
            icon_color_active = "#f5f6f9",
            bg_color = "#1b1e23",
            bg_color_hover = "#21252d",
            bg_color_pressed =  "#568af2"
        )
        self.btn_save_macro_csv.clicked.connect(self.saveMacroCSV)
        self.contentLayout.addWidget(self.btn_save_macro_csv)

        self.btn_delete_macro = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_close.svg"),
            parent = self._parent,
            app_parent = self._app_parent,
            btn_id="delete_macro",
            tooltip_text = "Delete Macro",
            width = 40,
            height = 30,
            radius = 10,
            dark_one = "#1b1e23",
            icon_color = "#c3ccdf",
            icon_color_hover = "#dce1ec",
            icon_color_pressed = "#6c99f4",
            icon_color_active = "#f5f6f9",
            bg_color = "#1b1e23",
            bg_color_hover = "#21252d",
            bg_color_pressed =  "#568af2"
        )
        self.btn_delete_macro.clicked.connect(self.onButtonClicked)
        self.contentLayout.addWidget(self.btn_delete_macro)

        if(emitSignal):
            self.addMacroClicked.emit()
        

    def onMacroDropClick(self):
        print(self._dropDownVal)
        print(self._dropDownVal[self.dropdown.currentText()])
        self.dropDownClicked.emit(self._dropDownVal[self.dropdown.currentText()])

    def onButtonClicked(self):
        button = self.sender()
        if button.objectName() == "delete_macro":
            self.contentLayout.removeWidget(self.btn_save_macro_csv)
            self.contentLayout.removeWidget(self.btn_change_macro)
            self.contentLayout.removeWidget(self.btn_load_macro)
            self.contentLayout.removeWidget(self.btn_save_macro)
            self.contentLayout.removeWidget(self.dropdown)
            self.contentLayout.removeWidget(self.macro_name)
            self.contentLayout.removeWidget(self.btn_delete_macro)

            self.btn_save_macro_csv.setParent(None)
            self.btn_change_macro.setParent(None)
            self.btn_load_macro.setParent(None)
            self.btn_save_macro.setParent(None)
            self.dropdown.setParent(None)
            self.macro_name.setParent(None)
            self.btn_delete_macro.setParent(None)

            if(self.top_level): 
                self.contentLayout.addWidget(self.button_add_macro)
            else:
                self.button_add_macro.deleteLater()
                self.btn_save_macro_csv.deleteLater()
                self.btn_change_macro.deleteLater()
                self.btn_load_macro.deleteLater()
                self.btn_save_macro.deleteLater()
                self.dropdown.deleteLater()
                self.macro_name.deleteLater()
                self.btn_delete_macro.deleteLater()
            self.deleteMacroClicked.emit(self)
        elif button.objectName() == "load_macro":
            self.dropDownClicked.emit(self._dropDownVal[self.dropdown.currentText()])
        elif button.objectName() == "save_macro":
            print("hi")
            pinlist = []
            for value in self._dropDownVal[self.dropdown.currentText()]:
                pinlist.append(value[0])
            self.saveMacroClicked.emit(self, pinlist)

    def set_button_states(self, states):
        for index, state in enumerate(states):
            print(self._dropDownVal[self.dropdown.currentText()][index][1])
            self._dropDownVal[self.dropdown.currentText()][index][1] = state
        self.button_states = states

    def get_button_states(self):
        return self.button_states

    def set_top_level(self, state):
        self.top_level = state

    def get_top_level(self):
        return self.top_level
    
    def setDropDownVal(self, Dict):
        self._dropDownVal = Dict
        self.dropdown.clear()
        print("new dropdown")
        for item in self._dropDownVal.keys():
            self.dropdown.addItem(item)

    def getDropDownVal(self):
        return self._dropDownVal

    def saveMacroCSV(self):
        profile = QFileDialog.getSaveFileName(self, "Save User Config", "", self.customProfileType)
        if profile[0]:
            with open(profile[0], 'w', newline='')as file:
                firstRow = []
                # first element of the first row should be the name of the macro
                firstRow.append(self.macro_name.text())
                # the rest of the elements in the first row should be the pins
                for value in self._dropDownVal[self.dropdown.currentText()]:
                    firstRow.append(value[0])
                rows = []
                for macroname in self._dropDownVal.keys():
                    tempRow = []
                    tempRow.append(macroname)
                    for value in self._dropDownVal[macroname]:
                        tempRow.append(value[1])
                    rows.append(tempRow)

                # Create a CSV writer object
                writer = csv.writer(file)
                writer.writerow(firstRow)

                for row in rows:
                    writer.writerow(row)
            file.close()

    def deleteSelf(self):
        if(self._last_item):
            self.contentLayout.removeWidget(self.button_add_macro)
            self.button_add_macro.setParent(None)
        else:
            self.contentLayout.removeWidget(self.btn_save_macro_csv)
            self.contentLayout.removeWidget(self.btn_change_macro)
            self.contentLayout.removeWidget(self.btn_load_macro)
            self.contentLayout.removeWidget(self.btn_save_macro)
            self.contentLayout.removeWidget(self.dropdown)
            self.contentLayout.removeWidget(self.macro_name)
            self.contentLayout.removeWidget(self.btn_delete_macro)

            self.btn_save_macro_csv.setParent(None)
            self.btn_change_macro.setParent(None)
            self.btn_load_macro.setParent(None)
            self.btn_save_macro.setParent(None)
            self.dropdown.setParent(None)
            self.macro_name.setParent(None)
            self.btn_delete_macro.setParent(None)

        if(self._last_item): 
            self.button_add_macro.deleteLater()
        else:
            self.button_add_macro.deleteLater()
            self.btn_save_macro_csv.deleteLater()
            self.btn_change_macro.deleteLater()
            self.btn_load_macro.deleteLater()
            self.btn_save_macro.deleteLater()
            self.dropdown.deleteLater()
            self.macro_name.deleteLater()
            self.btn_delete_macro.deleteLater()
        self.deleteMacroClicked.emit(self)


    def openUserProfile(self):
        profile = QFileDialog.getOpenFileName(self, "Open User Config", "", self.customProfileType)
        newDict = {}
        if profile[0]:
            with open(profile[0], 'r', encoding='utf-8-sig') as file:
                rows = []
                csvreader = csv.reader(file)
                for row in csvreader:
                    rows.append(row)
                
                
                # get the Macro name
                self.macro_name.setText(rows[0][0])

                # get the pins
                pins = []
                for index in range(1, len(rows[0])):
                    print(rows[0][index])
                    pins.append(int(rows[0][index]))

                # Get the macro names
                macro_names = []
                for index in range(1, len(rows)):
                    print(rows[index][0])
                    macro_names.append(rows[index][0])

                
                # get the macrro values
                for rowindex in range(1, len(rows)):
                    valueList = []
                    for columnIndex in range(1, len(rows[0])):
                        valueList.append([pins[columnIndex-1],int(rows[rowindex][columnIndex])])
                    newDict[macro_names[rowindex-1]] = valueList
            print(newDict)    
            print("user macro set")
            self.setDropDownVal(newDict)         
            file.close()
                                             
    

