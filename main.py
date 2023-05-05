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

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os

from configparser import ConfigParser
import csv
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# IMPORT SERIAL MODULES
import serial.tools.list_ports
import time
import threading

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)
        self.btn_send.setEnabled(False)

        self.macros = []

        self.currentProfile = False
        self.profileTypes = 'Profiles (*.ini)'
        self.customProfileType = 'Custom Profile (*.csv)'
        
        # self.add_macro_widget.addMacroClicked.connect(lambda: self.handleAddMacro(self.add_macro_widget, self.test_widget.button_states))
        # self.add_macro_widget.sendButtonClicked.connect(self.handleSendMacro)
        # self.add_macro_widget.deleteMacroClicked.connect(self.handleDeleteMacro)
        # self.add_macro_widget.saveMacroClicked.connect(self.handleSaveMacro)
        # self.macros.append(self.add_macro_widget)

        self.add_macro_widget_2.dropDownClicked.connect(self.handleMacroDropClick)
        self.add_macro_widget_3.dropDownClicked.connect(self.handleMacroDropClick)
        self.add_macro_widget_4.dropDownClicked.connect(self.handleMacroDropClick)
        self.add_macro_widget_5.dropDownClicked.connect(self.handleMacroDropClick)
        self.add_macro_widget_6.dropDownClicked.connect(self.handleMacroDropClick)
        self.add_macro_widget_7.dropDownClicked.connect(self.handleMacroDropClick)
        self.add_macro_widget_8.dropDownClicked.connect(self.handleMacroDropClick)
        self.add_macro_widget_9.dropDownClicked.connect(self.handleMacroDropClick)
        self.add_macro_widget_10.dropDownClicked.connect(self.handleMacroDropClick)

        self.add_macro_widget_2.saveMacroClicked.connect(self.handleSaveMacro)
        self.add_macro_widget_3.saveMacroClicked.connect(self.handleSaveMacro)
        self.add_macro_widget_4.saveMacroClicked.connect(self.handleSaveMacro)
        self.add_macro_widget_5.saveMacroClicked.connect(self.handleSaveMacro)
        self.add_macro_widget_6.saveMacroClicked.connect(self.handleSaveMacro)
        self.add_macro_widget_7.saveMacroClicked.connect(self.handleSaveMacro)
        self.add_macro_widget_8.saveMacroClicked.connect(self.handleSaveMacro)
        self.add_macro_widget_9.saveMacroClicked.connect(self.handleSaveMacro)
        self.add_macro_widget_10.saveMacroClicked.connect(self.handleSaveMacro)

        self.add_macro_widget_2.addMacroClicked.connect(self.handleAddMacro)
        self.add_macro_widget_3.addMacroClicked.connect(self.handleAddMacro)
        self.add_macro_widget_4.addMacroClicked.connect(self.handleAddMacro)
        self.add_macro_widget_5.addMacroClicked.connect(self.handleAddMacro)
        self.add_macro_widget_6.addMacroClicked.connect(self.handleAddMacro)
        self.add_macro_widget_7.addMacroClicked.connect(self.handleAddMacro)
        self.add_macro_widget_8.addMacroClicked.connect(self.handleAddMacro)
        self.add_macro_widget_9.addMacroClicked.connect(self.handleAddMacro)
        self.add_macro_widget_10.addMacroClicked.connect(self.handleAddMacro)

        self.add_macro_widget_2.deleteMacroClicked.connect(self.handleDeleteMacro)
        self.add_macro_widget_3.deleteMacroClicked.connect(self.handleDeleteMacro)
        self.add_macro_widget_4.deleteMacroClicked.connect(self.handleDeleteMacro)
        self.add_macro_widget_5.deleteMacroClicked.connect(self.handleDeleteMacro)
        self.add_macro_widget_6.deleteMacroClicked.connect(self.handleDeleteMacro)
        self.add_macro_widget_7.deleteMacroClicked.connect(self.handleDeleteMacro)
        self.add_macro_widget_8.deleteMacroClicked.connect(self.handleDeleteMacro)
        self.add_macro_widget_9.deleteMacroClicked.connect(self.handleDeleteMacro)
        self.add_macro_widget_10.deleteMacroClicked.connect(self.handleDeleteMacro)

        self.macros.append(self.add_macro_widget_10)
        self.macros.append(self.add_macro_widget_2)
        self.macros.append(self.add_macro_widget_3)
        self.macros.append(self.add_macro_widget_4)
        self.macros.append(self.add_macro_widget_5)
        self.macros.append(self.add_macro_widget_6)
        self.macros.append(self.add_macro_widget_7)
        self.macros.append(self.add_macro_widget_8)
        self.macros.append(self.add_macro_widget_9)



        self.ui.statusBar.set_right_text_color(self.themes["app_color"]["red"])
        self.ui.statusBar.set_left_text_color(self.themes["app_color"]["text_active"])
        print(self.test_widget.getSerialData(self.ui.statusBar))
        self.serial_connect()
        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    def update_button_position(self):
        # Get the current size of the window
        window_size = self.size()

        # Get the size of the button
        button_size = self.btn_send.sizeHint()



        # Calculate the position of the button
        button_x = window_size.width() - button_size.width() - 15
        button_y = window_size.height() - button_size.height() - 15

        print(button_x)
        print(button_y)

        # Set the button position
        self.btn_send.setGeometry(button_x, button_y, button_size.width(), button_size.height())

    def handleMacroDropClick(self, values):
        for item in values:
            # item[0] is the index and item[1] is the state
            self.test_widget.setButtonState(index = item[0], state = item[1])

    def handleAddMacro(self):
            macro_widget = PyGpioMacro2(
                parent = self,
                app_parent = self.ui.central_widget,
                name = "",
                dropdownval={},
                width = 600,
                colour = self.themes["app_color"]["dark_three"],
                last_item=True
            )
            self.ui.load_pages.verticalLayout_2.addWidget(macro_widget)
            macro_widget.addMacroClicked.connect(self.handleAddMacro)
            macro_widget.dropDownClicked.connect(self.handleMacroDropClick)
            macro_widget.deleteMacroClicked.connect(self.handleDeleteMacro)
            macro_widget.saveMacroClicked.connect(self.handleSaveMacro)
            self.macros.append(macro_widget)

    def handleSendMacro(self, states):
            self.test_widget.setButtonStates(states)
            self.test_widget.getSerialData(self.ui.statusBar)
            # self.serial_send()

    def handleSaveMacro(self, widget, pinList):
            print("wow")
            stateList = []
            for pin in pinList:
                stateList.append(self.test_widget.button_states[pin])
            print(pinList)
            print(stateList)
            widget.set_button_states(stateList)

    def handleDeleteMacro(self, widget):
        print("ddelete macro clicked")
        self.macros.remove(widget)
        self.ui.load_pages.verticalLayout_2.removeWidget(widget)
        widget.deleteLater()


    # Main functions for serial controls 
    # ///////////////////////////////////////////////////////////////
    # def update_coms(self):
    #     ports = serial.tools.list_ports.comports()
    #     coms = [com[0] for com in ports]
    #     coms.insert(0, "-")
    #     print(coms)
    #     portDropDown = self.dropdown_com_sel
    #     portDropDown.clear()
    #     for ports in coms:
    #         portDropDown.addItem(ports)

    def serial_connect(self):
        port = "/dev/ttyS0"
        print(port)
        if port != '-':
            try:
                self.ser = serial.Serial(port, 115200, timeout=0)
                self.ui.statusBar.set_right_text("Connected")
                self.beginReadSerial = True
                t1 = threading.Thread(target=self.read_serial)
                t1.deamon = True
                t1.start()
                self.btn_send.setEnabled(True)
                self.ui.statusBar.set_right_text_color(self.themes["app_color"]["green"])
            except:
                print("Couldn't connect")


    # Function (Thread 2) to Manage Reading the UART data from MCU
    def read_serial(self):
        self.serialData = ""
        print("thread start")
        
        # while self.beginReadSerial:
        #     try:
        #         #data = self.ser.readline().decode('utf8')
        #         data = self.ser.read()
                
        #         # if(counter > 600):
        #         #     counter = 0
                    
        #         #     # update the serial monitor or Monitoring widgets
        #         #     for index in range(1,14):
        #         #         if(self.monitorValues[0]==221):
        #         #             labels[index-1].set_text(str(self.monitorValues[index]*0.016),self.themes["app_color"]["context_color"])
        #         #             labels[index-1].set_indication_color(self.themes["app_color"]["context_color"])

        #         # else:
        #         #     counter = counter + 1
                
        #         # if len(data) > 0:
        #         #     value = int.from_bytes(data, "big")
        #         #     if value == 170: # header
        #         #         print(self.monitorValues)
        #         #         self.monitorValuesIndex = 0
        #         #         if(self.monitorValues[0] == 204): # detect identification bit to identify that it is a feedback tx value
        #         #             self.feedbackValue = ""
        #         #             for index in range(1,20):
        #         #                 if(index <= 17):
        #         #                     self.feedbackValue = self.feedbackValue + bin(self.monitorValues[index] - 128)[2:] + " "
        #         #                 else:
        #         #                     self.feedbackValue = self.feedbackValue + bin(self.monitorValues[index])[2:] + " "
        #         #         elif(self.monitorValues[0] == 221):
        #         #             self.serialData = ""
        #         #             for index in range(1,16):
        #         #                 self.serialData = self.serialData + str(self.monitorValues[index]) + " "
        #         #         self.serialMonitor.setText("Sensor data: " + '\n' + self.serialData + '\n' + "Feedback data:" + '\n' + self.feedbackValue)
        #         #     elif(value != 85):     
        #         #         self.monitorValues[self.monitorValuesIndex] = value
        #         #         self.monitorValuesIndex = self.monitorValuesIndex + 1
        #         # else:
        #         time.sleep(0.25)
        #     except serial.serialutil.SerialException as error:
        #         # Disconnect of USB -> UART occurred
        #         print(error)
        #         self.update_coms()
        #         self.ser.close()
        #         self.ui.statusBar.set_right_text("Disconnected")
        #         self.ui.statusBar.set_right_text_color(self.themes["app_color"]["red"])
        #         self.btn_connect.set_tooltip_text("Connect Serial device")
        #         self.btn_connect.setChecked(0) 
        #         self.beginReadSerial = False

    def serial_send(self):
        writeVal = self.test_widget.getSerialData(self.ui.statusBar)
        for value in writeVal:
            print(bin(value)[2:], end = " ")
        print()
        try:
            self.ser.write(writeVal)
        except serial.serialutil.SerialException as e:
            print(e)

    def clear_serial(self):
        self.serialData = ""

    def stop_thread(self):
        self.beginReadSerial = False

    # def openUserProfile(self):
    #     profile = QFileDialog.getOpenFileName(self, "Open User Config", "", self.customProfileType)
    #     if profile[0]:
    #         with open(profile[0], 'r') as file:
    #             rows = []
    #             csvreader = csv.reader(file)
    #             for row in csvreader:
    #                 rows.append(row)
                
    #             # get the GPIO pins
    #             for index in range(1, len(rows[0])):
    #                 print(rows[0][index])
                
    #             # Get the macro names
    #             for index in range(1, len(rows)):
    #                 print(rows[index][0])
                
    #             # get the macrro values
    #             for rowindex in range(1, len(rows)):
    #                 for columnIndex in range(1, len(rows[0])):
    #                     print(rows[rowindex][columnIndex])

                                             
    #         file.close()
    def loadUserConfig(self):
        profile = QFileDialog.getOpenFileName(self, "Open User Config", "profiles/Full_Configs/", self.customProfileType)
        if profile[0]:
            while(len(self.macros) > 0):
                print("deleteing macro %s" %self.macros[-1]._name)
                self.macros[-1].deleteSelf()
            with open(profile[0], 'r') as file:
                rows = []
                csvreader = csv.reader(file)
                for row in csvreader:
                    rows.append(row)
                pinMap = {}
                pinNames = []

                index = 0
                for pin in rows[1]:
                    if(pin == ""):
                        break
                    pinMap[pin] = index
                    pinNames.append(pin)
                    index = index+1

                for pin in rows[2]:
                    if(pin == ""):
                        break
                    pinMap[pin] = index
                    pinNames.append(pin)
                    index = index+1

                for pin in rows[4]:
                    if(pin == ""):
                        break
                    pinMap[pin] = index
                    pinNames.append(pin)
                    index = index+1

                for pin in rows[5]:
                    if(pin == ""):
                        break
                    pinMap[pin] = index
                    pinNames.append(pin)
                    index = index+1
                    
                current_dict = {}
                name = ""
                firstRowFlag = 1
                pins = []

                for index,row in enumerate(rows):
                    # / will be used as the seperator between the macro definitions
                    if row[0] == "/":

                        macro_widget = PyGpioMacro2(
                            parent = self,
                            app_parent = self.ui.central_widget,
                            name = name,
                            dropdownval=current_dict,
                            width = 600,
                            colour = self.themes["app_color"]["dark_three"]
                        )
                        macro_widget.dropDownClicked.connect(self.handleMacroDropClick)
                        macro_widget.deleteMacroClicked.connect(self.handleDeleteMacro)
                        macro_widget.saveMacroClicked.connect(self.handleSaveMacro)
                        self.ui.load_pages.verticalLayout_2.addWidget(macro_widget)
                        self.macros.append(macro_widget)
                        current_dict = {}
                        firstRowFlag = 1
                        pins.clear()


                    # # will be used to indicate the end of hte macros
                    elif row[0] == "#":

                        macro_widget = PyGpioMacro2(
                            parent = self,
                            app_parent = self.ui.central_widget,
                            name = name,
                            dropdownval=current_dict,
                            width = 600,
                            colour = self.themes["app_color"]["dark_three"]
                        )
                        macro_widget.dropDownClicked.connect(self.handleMacroDropClick)
                        macro_widget.deleteMacroClicked.connect(self.handleDeleteMacro)
                        macro_widget.saveMacroClicked.connect(self.handleSaveMacro)
                        self.ui.load_pages.verticalLayout_2.addWidget(macro_widget)
                        self.macros.append(macro_widget)

                        macro_widget = PyGpioMacro2(
                            parent = self,
                            app_parent = self.ui.central_widget,
                            name = "",
                            dropdownval={},
                            width = 600,
                            colour = self.themes["app_color"]["dark_three"],
                            last_item=True
                        )
                        self.ui.load_pages.verticalLayout_2.addWidget(macro_widget)
                        macro_widget.addMacroClicked.connect(self.handleAddMacro)
                        macro_widget.dropDownClicked.connect(self.handleMacroDropClick)
                        macro_widget.deleteMacroClicked.connect(self.handleDeleteMacro)
                        macro_widget.saveMacroClicked.connect(self.handleSaveMacro)
                        self.macros.append(macro_widget)
                        current_dict = {}
                        pins.clear()

                        break
                    elif(index>5):
                        if(firstRowFlag):
                            for i in range(1, len(row)):
                                if(row[i] == ''):
                                    break
                                pins.append((row[i]))
                            name = row[0]
                            firstRowFlag = 0
                        else:
                            values = []
                            for i in range(1, len(row)):
                                if(row[i]==''):
                                    break
                                values.append([(int(pinMap[pins[i-1]])), int(row[i])])
                            current_dict[row[0]] = values      

                for index, name in enumerate(pinNames):
                    item = QTableWidgetItem()
                    item.setText(str(name))
                    self.gpio_edit_table.setItem(index, 0, item)
                    self.test_widget.buttons[index].set_tooltip_text(name)

            file.close()
            

    def saveUserConfig(self):
        profile = QFileDialog.getSaveFileName(self, "Save User Config", "profiles/Full_Configs/", self.customProfileType)
        if profile[0]:
            with open(profile[0], 'w', newline='')as file:
                rows = []               
                row = []

                row.append("Top_Pins")
                rows.append(row)
                row = []

                pinNameMap = {}

                for index in range(self.gpio_edit_table.rowCount()):
                    if(index == 19):
                        row.append(self.gpio_edit_table.item(index, 0).text())
                        rows.append(row)
                        pinNameMap[index] = self.gpio_edit_table.item(index, 0).text()
                        row = []
                    elif(index == 39):
                        row.append(self.gpio_edit_table.item(index, 0).text())
                        rows.append(row)
                        pinNameMap[index] = self.gpio_edit_table.item(index, 0).text()
                        row = []
                        row.append("Bottom_Pins")
                        rows.append(row)
                        row = []
                    elif(index == 59):
                        row.append(self.gpio_edit_table.item(index, 0).text())
                        rows.append(row)
                        pinNameMap[index] = self.gpio_edit_table.item(index, 0).text()
                        row = []
                    elif(index == 79):
                        row.append(self.gpio_edit_table.item(index, 0).text())
                        rows.append(row)
                        pinNameMap[index] = self.gpio_edit_table.item(index, 0).text()
                        row = []
                    else:
                        row.append(self.gpio_edit_table.item(index, 0).text())
                        pinNameMap[index] = self.gpio_edit_table.item(index, 0).text()

                for index, macro in enumerate(self.macros):
                    row = []
                    if(index == 0):
                        # first element of the first row is the name of the macro
                        row.append(macro._name)
                        # Rest of the elements in the row is the pin names
                        for values in macro._dropDownVal[macro.dropdown.currentText()]:
                            row.append(pinNameMap[values[0]])
                        rows.append(row)

                        for macroname in macro._dropDownVal.keys():
                            row = []
                            row.append(macroname)
                            for value in macro._dropDownVal[macroname]:
                                row.append(value[1])
                            rows.append(row)
                    elif(index == len(self.macros)-2):
                        row.append("/")
                        rows.append(row)

                        # first element of the first row is the name of the macro
                        row = []
                        row.append(macro._name)

                        # Rest of the elements in the row is the pin names
                        for values in macro._dropDownVal[macro.dropdown.currentText()]:
                            row.append(pinNameMap[values[0]])
                        rows.append(row)


                        for macroname in macro._dropDownVal.keys():
                            row=[]
                            row.append(macroname)
                            for value in macro._dropDownVal[macroname]:
                                row.append(value[1])
                            rows.append(row)

                        row = []
                        row.append("#")
                        rows.append(row)
                    elif(index < len(self.macros)-1):
                        row.append("/")
                        rows.append(row)

                        # first element of the first row is the name of the macro
                        row = []
                        row.append(macro._name)

                        # Rest of the elements in the row is the pin names
                        for values in macro._dropDownVal[macro.dropdown.currentText()]:
                            row.append(pinNameMap[values[0]])
                        rows.append(row)

                        for macroname in macro._dropDownVal.keys():
                            row = []
                            row.append(macroname)
                            for value in macro._dropDownVal[macroname]:
                                row.append(value[1])
                            rows.append(row)
                
                # Create a CSV writer object
                writer = csv.writer(file)
                for row in rows:
                    writer.writerow(row)
                rows.clear()
            file.close()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # Remove Selection If Clicked By "btn_close_left_column"
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()

        # Get Title Bar Btn And Reset Active         
        top_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        top_settings.set_active(False)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////
        
        # HOME BTN
        if btn.objectName() == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        # WIDGETS BTN
        if btn.objectName() == "btn_open_file":
            # Select Menu
            # self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            # MainFunctions.set_page(self, self.ui.load_pages.page_2)

            # self.saveFile()
            self.loadUserConfig()
            
        # LOAD USER PAGE
        if btn.objectName() == "btn_save":
            # Select Menu
            # self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 3 
            # MainFunctions.set_page(self, self.ui.load_pages.page_3)
            self.saveUserConfig()

        # BOTTOM INFORMATION
        if btn.objectName() == "btn_info":
            # CHECK IF LEFT COLUMN IS VISIBLE
            print(len(QApplication.allWidgets()))
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btn.objectName())

                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self, 
                    menu = self.ui.left_column.menus.menu_2,
                    title = "Info tab",
                    icon_path = Functions.set_svg_icon("icon_info.svg")
                )

        # SETTINGS LEFT
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self, 
                    menu = self.ui.left_column.menus.menu_1,
                    title = "Settings Left Column",
                    icon_path = Functions.set_svg_icon("icon_settings.svg")
                )

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////
        
        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn            
            top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            top_settings.set_active_tab(False)            

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    def parserSetValues(self):
            parser = ConfigParser()
            parser.read(self.currentProfile[0])

            # Save the current values that are assigned to the GPIOs
            if not parser.has_section("current_GPIO_state"):
                parser.add_section("current_GPIO_state")
                for index, state in enumerate(self.test_widget.button_states):
                    parser.set("current_GPIO_state", str(index), str(state)) 
            # Save the macros created
            if(len(self.macros) > 1):
                for macroIndex, macros in enumerate(self.macros):
                    if macroIndex != len(self.macros)-1:
                        if not parser.has_section("Macro_" + str(macroIndex)):
                            parser.add_section("Macro_" + str(macroIndex))
                            #parser.set("Macro_"+ str(macroIndex), "Name", self. )
                            for stateIndex, states in enumerate(macros.get_button_states()):
                                parser.set("Macro_" + str(macroIndex), str(stateIndex), str(states))
            # Save the names of the GPIOs
            if not parser.has_section("GPIO_names"):
                parser.add_section("GPIO_names")
                for row_number in range(self.gpio_edit_table.rowCount()):
                    parser.set("GPIO_names", str(row_number), str(self.gpio_edit_table.item(row_number, 0)))
            with open(self.currentProfile[0], 'w') as configfile:
                parser.write(configfile) 
            configfile.close()

    def parserGetValues(self):
        try:
            parser = ConfigParser()
            parser.read(self.currentProfile[0])
            # load the GPIO configs
            states = []
            for index in range(len(self.test_widget.button_states)):
                states.append(eval(parser.get("current_GPIO_state", str(index))))
            self.test_widget.setButtonStates(states)
            # load the macros
            while((len(self.macros)-1) >= 1):
                print("deleting macros")
                self.handleDeleteMacro(self.macros[-2]) 
            states = []
            for section in parser.sections():
                if(section[:5] == "Macro"):
                    for index in range(len(self.test_widget.button_states)):
                        states.append(eval(parser.get(section, str(index))))
                    self.macros[-1].on_add_macro_clicked()
                    self.handleAddMacro(self.macros[-1], states) 
                    states = []
                    print("adding macros")
        except TypeError as e:
            print("type error: %s"%e)
        except Exception as e:
            print(e)
    
    def saveFile(self):
        if self.currentProfile:
            print(self.currentProfile[0])
            self.parserSetValues()
        else:
            self.saveAs()

    def saveAs(self):
        profile = QFileDialog.getSaveFileName(self, "Save Config as", "/profiles/untitled.ini", self.profileTypes)
        if profile[0]:
            self.currentProfile = profile    
            print(self.currentProfile[0])
            self.parserSetValues()
    
    def openFile(self):
        profile = QFileDialog.getOpenFileName(self, "Open Config", "", self.profileTypes)
        if profile[0]:
            self.currentProfile = profile
            self.parserGetValues()

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec_())