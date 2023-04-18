# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
from gui.widgets import PyIconButton
from gui.core.functions import Functions
from gui.core.json_themes import Themes
import time
import os
class PyGpioSelector(QWidget):
    buttonClicked = Signal(int)
    buttonStatesChanged = Signal(list)
    
    def __init__(
            self, 
            app_parent,
            parent,   
            board = "DE10 nano",
            pictureWidth = 1280,
            pictureHeight = 720,
            width = 200, 
            height = 100, 
            radius = 10,
            color = "#272c36", 
            rows = 2, 
            columns = 15, 
            sideBorders = 5, 
            topBorders = 5, 
            bottomBorders = 5, 
            buttonHeight = 20,
            buttonWidth = 20,
            buttonRadius = 10,
            buttonColour = "#c3ccdf",
            buttonColourPressed = "#edf0f5",
            buttonColourHover = "#dce1ec",
            buttonColourActive = "#568af2",
            buttonSpacing=10, 
            vSpacing = 10
        ):
        super().__init__()

        self.button_states = []
        self.buttons = []

        # Set the size of the widget
        self.setMinimumSize(pictureWidth+10, pictureHeight+10)

        
        if(board == "DE10 nano"):
            self.FPGA_IMAGE = QLabel()
            app_path = os.path.abspath(os.getcwd())
            folder = "gui/images/images/de10_nano_blue_crop.png"
            path = os.path.join(app_path, folder)
            # pixmap = QPixmap("C:/Code/qt creator projects/FPGA_GPIO_Controller/gui/images/images/de10_nano_blue_crop.png")
            pixmap = QPixmap(path)
            self.FPGA_IMAGE.setPixmap(pixmap)
            self.FPGA_IMAGE.setScaledContents(True)
            self.FPGA_IMAGE.setFixedSize(QSize(pictureWidth, pictureHeight))
            #self.FPGA_IMAGE.setMask(pixmap.mask())
            self.backgroundWidgetTop = QWidget()
            self.backgroundWidgetTop.setStyleSheet(f"background-color: {color}; border-radius: {radius}")
            self.backgroundWidgetTop.setFixedSize(width, height)
            self.backgroundWidgetTop.setContentsMargins(sideBorders, topBorders, sideBorders, bottomBorders)
            
            self.spacer = QWidget()
            self.spacer.setFixedSize(width, 170)
            
            self.backgroundWidgetBottom = QWidget()
            self.backgroundWidgetBottom.setStyleSheet(f"background-color: {color}; border-radius: {radius}")
            self.backgroundWidgetBottom.setFixedSize(width, height)
            self.backgroundWidgetBottom.setContentsMargins(sideBorders, topBorders, sideBorders, bottomBorders)


        # Set the background color of the widget
        # self.setStyleSheet(f"background-image: url(C:/Code/qt creator projects/FPGA_GPIO_Controller/gui/images/images/de10_nano_no_pins-removebg.png);")
        #self.setStyleSheet(f"background-color: {color};")

        # Set the content margins of the widget
        

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setAlignment(Qt.AlignVCenter)
        main_layout.addWidget(self.FPGA_IMAGE)


        main_layout_2 = QGridLayout(self.FPGA_IMAGE)
        main_layout_2.setContentsMargins(69,0,0,0)
        main_layout_2.addWidget(self.backgroundWidgetTop,0,0)
        main_layout_2.addWidget(self.spacer,1,0)
        main_layout_2.addWidget(self.backgroundWidgetBottom,2,0) 
        main_layout_2.setRowStretch(0, 1)
        main_layout_2.setRowStretch(1, 1)
        main_layout_2.setColumnStretch(0, 1)
        main_layout_2.setColumnStretch(1, 1)
        

        spacer_layout = QHBoxLayout(self.spacer)
        spacer_layout.setContentsMargins(0,0,0,0)
        spacer_layout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        spacer_layout.setSpacing(300)
        
        # Create a grid layout to hold the buttons
        grid_layout_top = QGridLayout(self.backgroundWidgetTop)
        grid_layout_top.setSpacing(vSpacing)
        grid_layout_top.setHorizontalSpacing(buttonSpacing)
        grid_layout_top.setVerticalSpacing(vSpacing)

        # Create a grid layout to hold the buttons
        grid_layout_bottom = QGridLayout(self.backgroundWidgetBottom)
        grid_layout_bottom.setSpacing(vSpacing)
        grid_layout_bottom.setHorizontalSpacing(buttonSpacing)
        grid_layout_bottom.setVerticalSpacing(vSpacing)

        # Create a for loop to generate the buttons
        for i in range(rows):
            for j in range(columns):
                # Create a QPushButton widget and add it to the grid layout
                # 25 is 5v 
                # 5 is ground
                # 34 is 3.3v
                # 14 is ground 
                if (i * columns + j) == 5 or (i * columns + j) == 14:
                    button = PyIconButton(
                        btn_id = f"ButtonTop {i * columns + j + 1}",
                        icon_path = Functions.set_svg_icon("icon_minimize.svg"),
                        parent = parent,
                        app_parent=app_parent,
                        tooltip_text = "GND",
                        width = buttonWidth,
                        height = buttonHeight,
                        radius = buttonRadius,
                        dark_one = "#1b1e23",
                        icon_color = "#c3ccdf",
                        icon_color_hover = "#c3ccdf",
                        icon_color_pressed = "#c3ccdf",
                        icon_color_active = "#c3ccdf",
                        bg_color = "#272c36",
                        bg_color_hover = "#272c36",
                        bg_color_pressed = "#272c36",
                        context_color = "#272c36",
                    )
                elif(i * columns + j) == 25:
                    button = PyIconButton(
                        btn_id = f"ButtonTop {i * columns + j + 1}",
                        icon_path = Functions.set_svg_icon("icon_plus.svg"),
                        parent = parent,
                        app_parent=app_parent,
                        tooltip_text = "5V",
                        width = buttonWidth,
                        height = buttonHeight,
                        radius = buttonRadius,
                        dark_one = "#1b1e23",
                        icon_color = "#c3ccdf",
                        icon_color_hover = "#c3ccdf",
                        icon_color_pressed = "#c3ccdf",
                        icon_color_active = "#c3ccdf",
                        bg_color = "#ff5555",
                        bg_color_hover = "#ff5555",
                        bg_color_pressed = "#ff5555",
                        context_color = "#ff5555",
                        tooltip_bottom=True
                    )
                elif(i * columns + j) == 34:
                    button = PyIconButton(
                        btn_id = f"ButtonTop {i * columns + j + 1}",
                        icon_path = Functions.set_svg_icon("icon_plus.svg"),
                        parent = parent,
                        app_parent=app_parent,
                        tooltip_text = "3.3V",
                        width = buttonWidth,
                        height = buttonHeight,
                        radius = buttonRadius,
                        dark_one = "#1b1e23",
                        icon_color = "#c3ccdf",
                        icon_color_hover = "#c3ccdf",
                        icon_color_pressed = "#c3ccdf",
                        icon_color_active = "#c3ccdf",
                        bg_color = "#ff5555",
                        bg_color_hover = "#ff5555",
                        bg_color_pressed = "#ff5555",
                        context_color = "#ff5555",
                        tooltip_bottom=True
                    )
                else: 
                    if(i == 1):
                        button = PyIconButton(
                            btn_id = f"ButtonTop {i * columns + j + 1}",
                            icon_path = Functions.set_svg_icon("icon_maximize.svg"),
                            parent = parent,
                            app_parent=app_parent,
                            tooltip_text = f"GPIO {i * columns + j + 1}",
                            width = buttonWidth,
                            height = buttonHeight,
                            radius = buttonRadius,
                            dark_one = "#1b1e23",
                            icon_color = "#c3ccdf",
                            icon_color_hover = "#dce1ec",
                            icon_color_pressed = "#6c99f4",
                            icon_color_active = "#f5f6f9",
                            bg_color = buttonColour,
                            bg_color_hover = buttonColourHover,
                            bg_color_pressed = buttonColourPressed,
                            context_color = buttonColourActive,
                            tooltip_bottom=True
                        )
                    else:
                        button = PyIconButton(
                            btn_id = f"ButtonTop {i * columns + j + 1}",
                            icon_path = Functions.set_svg_icon("icon_maximize.svg"),
                            parent = parent,
                            app_parent=app_parent,
                            tooltip_text = f"GPIO {i * columns + j + 1}",
                            width = buttonWidth,
                            height = buttonHeight,
                            radius = buttonRadius,
                            dark_one = "#1b1e23",
                            icon_color = "#c3ccdf",
                            icon_color_hover = "#dce1ec",
                            icon_color_pressed = "#6c99f4",
                            icon_color_active = "#f5f6f9",
                            bg_color = buttonColour,
                            bg_color_hover = buttonColourHover,
                            bg_color_pressed = buttonColourPressed,
                            context_color = buttonColourActive
                        )
                    button.clicked.connect(lambda checked = None, index=i * columns + j: self.buttonStateUpdate(index))
                grid_layout_top.addWidget(button, i, j)
                
                # Set the initial button state to unchecked
                self.button_states.append(0)
                self.buttons.append(button)

        # Create a for loop to generate the buttons
        for i in range(rows):
            for j in range(columns):
                # Create a QPushButton widget and add it to the grid layout
                if (i * columns + j) == 25 or (i * columns + j) == 34:
                    button = PyIconButton(
                        btn_id = f"ButtonTop {i * columns + j + 1}",
                        icon_path = Functions.set_svg_icon("icon_minimize.svg"),
                        parent = parent,
                        app_parent=app_parent,
                        tooltip_text = "GND",
                        width = buttonWidth,
                        height = buttonHeight,
                        radius = buttonRadius,
                        dark_one = "#1b1e23",
                        icon_color = "#c3ccdf",
                        icon_color_hover = "#c3ccdf",
                        icon_color_pressed = "#c3ccdf",
                        icon_color_active = "#c3ccdf",
                        bg_color = "#272c36",
                        bg_color_hover = "#272c36",
                        bg_color_pressed = "#272c36",
                        context_color = "#272c36",
                        tooltip_bottom=True
                    )
                elif(i * columns + j) == 14:
                    button = PyIconButton(
                        btn_id = f"ButtonTop {i * columns + j + 1}",
                        icon_path = Functions.set_svg_icon("icon_plus.svg"),
                        parent = parent,
                        app_parent=app_parent,
                        tooltip_text = "5V",
                        width = buttonWidth,
                        height = buttonHeight,
                        radius = buttonRadius,
                        dark_one = "#1b1e23",
                        icon_color = "#c3ccdf",
                        icon_color_hover = "#c3ccdf",
                        icon_color_pressed = "#c3ccdf",
                        icon_color_active = "#c3ccdf",
                        bg_color = "#ff5555",
                        bg_color_hover = "#ff5555",
                        bg_color_pressed = "#ff5555",
                        context_color = "#ff5555"
                    )
                elif(i * columns + j) == 5:
                    button = PyIconButton(
                        btn_id = f"ButtonTop {i * columns + j + 1}",
                        icon_path = Functions.set_svg_icon("icon_plus.svg"),
                        parent = parent,
                        app_parent=app_parent,
                        tooltip_text = "3.3V",
                        width = buttonWidth,
                        height = buttonHeight,
                        radius = buttonRadius,
                        dark_one = "#1b1e23",
                        icon_color = "#c3ccdf",
                        icon_color_hover = "#c3ccdf",
                        icon_color_pressed = "#c3ccdf",
                        icon_color_active = "#c3ccdf",
                        bg_color = "#ff5555",
                        bg_color_hover = "#ff5555",
                        bg_color_pressed = "#ff5555",
                        context_color = "#ff5555"
                    )
                else: 
                    if(i == 1):
                        button = PyIconButton(
                            btn_id = f"ButtonBottom {i * columns + j + 1}",
                            icon_path = Functions.set_svg_icon("icon_maximize.svg"),
                            parent = parent,
                            app_parent=app_parent,
                            tooltip_text = f"GPIO {(i+2) * columns + j + 1}",
                            width = buttonWidth,
                            height = buttonHeight,
                            radius = buttonRadius,
                            dark_one = "#1b1e23",
                            icon_color = "#c3ccdf",
                            icon_color_hover = "#dce1ec",
                            icon_color_pressed = "#6c99f4",
                            icon_color_active = "#f5f6f9",
                            bg_color = buttonColour,
                            bg_color_hover = buttonColourHover,
                            bg_color_pressed = buttonColourPressed,
                            context_color = buttonColourActive,
                            tooltip_bottom=True
                        )
                    else:
                        button = PyIconButton(
                            btn_id = f"ButtonBottom {i * columns + j + 1}",
                            icon_path = Functions.set_svg_icon("icon_maximize.svg"),
                            parent = parent,
                            app_parent=app_parent,
                            tooltip_text = f"GPIO {(i+2) * columns + j + 1}",
                            width = buttonWidth,
                            height = buttonHeight,
                            radius = buttonRadius,
                            dark_one = "#1b1e23",
                            icon_color = "#c3ccdf",
                            icon_color_hover = "#dce1ec",
                            icon_color_pressed = "#6c99f4",
                            icon_color_active = "#f5f6f9",
                            bg_color = buttonColour,
                            bg_color_hover = buttonColourHover,
                            bg_color_pressed = buttonColourPressed,
                            context_color = buttonColourActive
                    )
                    button.clicked.connect(lambda _ = None, index= ( ((i+2)*(columns)) + j): self.buttonStateUpdate(index))
                grid_layout_bottom.addWidget(button, i, j)

                # Set the initial button state to unchecked
                self.button_states.append(0)
                self.buttons.append(button)

        self.sel_all_button = PyIconButton(
                        btn_id = f"ButtonTop {i * columns + j + 1}",
                        icon_path = Functions.set_svg_icon("icon_select_all.svg"),
                        parent = parent,
                        app_parent=app_parent,
                        tooltip_text = "Select All",
                        width = 30,
                        height = 30,
                        radius = 10,
                        dark_one = "#1b1e23",
                        icon_color = "#c3ccdf",
                        icon_color_hover = "#dce1ec",
                        icon_color_pressed = "#6c99f4",
                        icon_color_active = "#f5f6f9",
                        bg_color = buttonColour,
                        bg_color_hover = buttonColourHover,
                        bg_color_pressed = buttonColourPressed,
                        context_color = buttonColourActive
                    )
        self.desel_all_button = PyIconButton(
                        btn_id = f"ButtonTop {i * columns + j + 1}",
                        icon_path = Functions.set_svg_icon("icon_deselect_all.svg"),
                        parent = parent,
                        app_parent=app_parent,
                        tooltip_text = "Deselect all",
                        width = 30,
                        height = 30,
                        radius = 10,
                        dark_one = "#1b1e23",
                        icon_color = "#c3ccdf",
                        icon_color_hover = "#dce1ec",
                        icon_color_pressed = "#6c99f4",
                        icon_color_active = "#f5f6f9",
                        bg_color = buttonColour,
                        bg_color_hover = buttonColourHover,
                        bg_color_pressed = buttonColourPressed,
                        context_color = buttonColourActive
                    )
        
        
        spacer_layout.addWidget(self.desel_all_button)
        spacer_layout.addWidget(self.sel_all_button)

        self.sel_all_button.clicked.connect(self.selectAllButtons)
        self.desel_all_button.clicked.connect(self.deselectAllButtons)
        # Set the alignment of the grid layout to center vertically
        grid_layout_top.setAlignment(Qt.AlignVCenter)
        grid_layout_bottom.setAlignment(Qt.AlignVCenter)

        # Set the size policy of each row to Expanding
        for i in range(rows):
            grid_layout_top.setRowStretch(i, 1)
            grid_layout_bottom.setRowStretch(i, 1)

        # Set the size policy of each column to Expanding
        for j in range(columns):
            grid_layout_top.setColumnStretch(j, 1)
            grid_layout_bottom.setColumnStretch(j, 1)


    
    def selectAllButtons(self):
        self.button_states = []
        # start_time = time.time()
        # for index in range(20):
        #     self.buttons[index].set_active(1)
        #     self.buttons[index+20].set_active(1)
        #     self.buttons[index+40].set_active(1)
        #     self.buttons[index+60].set_active(1)
        # print(time.time()-start_time)
        start_time = time.time()
        for button in self.buttons:
            button.set_active(1)
            self.button_states.append(button.is_active())
        self.buttonStatesChanged.emit(self.button_states)
        print(time.time()-start_time)

    def deselectAllButtons(self):
        self.button_states = []
        for button in self.buttons:
            button.set_active(0)
            self.button_states.append(button.is_active())
        self.buttonStatesChanged.emit(self.button_states)

    def buttonStateUpdate(self, index):
        if self.buttons[index].is_active():
            self.buttons[index].set_active(0)
        else:
            self.buttons[index].set_active(1)
        self.button_states = []
        for button in self.buttons:
            self.button_states.append(button.is_active())
        self.buttonStatesChanged.emit(self.button_states)

    def setButtonStates(self, states):
        self.button_states = states
        for index, state in enumerate(states):
            self.buttons[index].set_active(state)

    def setButtonState(self, state, index):
        self.button_states[index] = state
        self.buttons[index].set_active(state)

    def getSerialData(self, statusbar):
        writeVal = bytearray()
        writeVal.append(0xAA)
        calc = 0
        index = 0
        bitCount = 0
        avoidIndex = [5,14,25,34,45,54,65,74]
        for state in self.button_states:
            if(index not in avoidIndex):
                calc = calc + state*(2**bitCount)
                bitCount = bitCount + 1      

            if(bitCount == 8):
                writeVal.append(calc)
                calc = 0
                bitCount = 0
                
            index = index + 1
        
        checksum = 0
        for index, value in enumerate(writeVal):
            if(index > 0):
                checksum = checksum ^ value
        
        writeVal.append(checksum)

        writeVal.append(0x55)

        for value in writeVal:
            print(bin(value))
        
        serialVal = ""
        for value in writeVal:
            serialVal = serialVal + (bin(value)[2:])
            serialVal = serialVal + " "
            statusbar.set_left_text(serialVal)

        return writeVal
        
        