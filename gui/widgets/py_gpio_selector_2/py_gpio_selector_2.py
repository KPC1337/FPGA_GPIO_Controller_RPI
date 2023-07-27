# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
from gui.widgets import PyIconButton
from gui.core.functions import Functions
from gui.core.json_themes import Themes
import time
import os
class PyGpioSelector2(QWidget):
    buttonClicked = Signal(int)
    buttonStatesChanged = Signal(list)
    
    def __init__(
            self, 
            app_parent,
            parent,   
            board = "DE10 nano",
            radius = 10,
            color = "#272c36", 
            sideBorders = 0, 
            topBorders = 0, 
            bottomBorders = 0, 
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

        # Create a QGraphicsScene
        self.scene = QGraphicsScene()

        # Create a QGraphicsView and set the scene
        self.view = QGraphicsView()
        self.view.setScene(self.scene)
        self.view.setDragMode(QGraphicsView.NoDrag)
        self.view.setFrameStyle(Qt.FramelessWindowHint)

        # Create a QGraphicsPixmapItem to display the image
        self.image_item = QGraphicsPixmapItem()

        self.button_states = []
        self.buttons = []
        pictureWidth = 693
        pictureHeight = 390

        # Set the size of the widget
        self.setMinimumSize(pictureWidth+10, pictureHeight+10)

        rows = 0
        columns = 0 
        vSpacing = 0
        if(board == "DE10 nano"):
            rows = 2
            columns = 14
            width = 385
            height = 79
            vSpacing = 15

            pin_map_dict = {
                # Header P3 -- Top header
                0: "GND",       1: "VCC 3.3",
                2: "RST",       3: "GND",
                4: "PIN 142",   5: "PIN 143",
                6: "PIN 139",   7: "PIN 141",
                8: "PIN 136",   9: "PIN 137",
                10: "PIN 134",  11: "PIN 135",
                12: "PIN 132",  13: "PIN 133",
                14: "PIN 126",  15: "PIN 129",
                16: "PIN 122",  17: "PIN 125",
                18: "PIN 120",  19: "PIN 121",
                20: "PIN 118",  21: "PIN 119",
                22: "PIN 114",  23: "PIN 115",
                24: "PIN 112",  25: "PIN 113",
                26: "GND",      27: "GND",
                # Header P2 -- Right header
                28: "VCC 3.3",  29: "GND",
                30: "GND",      31: "PIN 104",
                32: "PIN 103",  33: "PIN 101",
                34: "PIN 100",  35: "PIN 99",
                36: "PIN 97",   37: "PIN 96",
                38: "PIN 94",   39: "PIN 93",
                40: "PIN 92",   41: "PIN 91",
                42: "PIN 90",   43: "PIN 89",
                44: "PIN 88",   45: "PIN 87",
                46: "PIN 86",   47: "PIN 81",
                48: "PIN 80",   49: "PIN 79",
                50: "PIN 76",   51: "PIN 75",
                52: "PIN 74",   53: "PIN 73",
                54: "GND",      55: "GND",
                # Header P1 -- Bottom header
                56: "PIN 41",   57: "PIN 40",
                58: "PIN 43",   59: "PIN 42",
                60: "PIN 45",   61: "PIN 44",
                62: "PIN 48",   63: "PIN 47",
                64: "PIN 52",   65: "PIN 51",
                66: "PIN 55",   67: "PIN 53",
                68: "PIN 58",   69: "PIN 57",
                70: "PIN 60",   71: "PIN 59",
                72: "PIN 64",   73: "PIN 63",
                74: "PIN 67",   75: "PIN 65",
                76: "PIN 70",   77: "PIN 69",
                78: "PIN 72",   79: "PIN 71",
                80: "GND",      81: "GND",
                82: "VCC 3.3",  83: "VCC 3.3",
                # Header P4 -- left header
                84: "GND",      85: "GND",
                86: "LED D2",    87: "PIN 4",
                88: "LED D4",    89: "PIN 8",
                90: "LED D5",    91: "GND",
                92: "GND",      93: "GND",
                94: "PIN 18",   95: "CLK",
                96: "PIN 22",   97: "PIN 21",
                98: "PIN 25",   99: "PIN 24",
                100: "PIN 27",  101: "PIN 26",
                102: "VCC 1.2", 103: "VCC 1.2",
                104: "PIN 30",  105: "PIN 28",
                106: "UART TX",  107: "UART RX",
                108: "GND",     109: "GND",
                110: "VCC 3.3", 111: "VCC 3.3"
            }

            normal_pin = {
                "icon": "icon_maximize.svg",
                "icon_color":"#c3ccdf",
                "icon_color_hover": "#dce1ec",
                "icon_color_pressed":"#6c99f4",
                "icon_color_active":"#f5f6f9",
                "bg_color":buttonColour,
                "bg_color_hover":buttonColourHover,
                "bg_color_pressed":buttonColourPressed,
                "context_color":buttonColourActive
            }

            voltage_pin = {
                "icon": "icon_plus.svg",
                "icon_color":"#c3ccdf",
                "icon_color_hover": "#c3ccdf",
                "icon_color_pressed":"#c3ccdf",
                "icon_color_active":"#c3ccdf",
                "bg_color": "#ff5555",
                "bg_color_hover":"#ff5555",
                "bg_color_pressed":"#ff5555",
                "context_color":"#ff5555"
            }

            ground_pin = {
                "icon": "icon_minimize.svg",
                "icon_color":"#c3ccdf",
                "icon_color_hover": "#c3ccdf",
                "icon_color_pressed":"#c3ccdf",
                "icon_color_active":"#c3ccdf",
                "bg_color": "#272c36",
                "bg_color_hover":"#272c36",
                "bg_color_pressed":"#272c36",
                "context_color":"#272c36"
            }

            pin_theme_dict = {
                "VCC":voltage_pin,
                "GND":ground_pin,
                "PIN":normal_pin,
                "CLK":ground_pin,
                "RST":ground_pin,
                "UAR":ground_pin,
                "LED":ground_pin
            }

            app_path = os.path.abspath(os.getcwd())
            folder = "gui/images/images/cyclone_2_bigger.png"
            path = os.path.join(app_path, folder)
            # pixmap = QPixmap("C:/Code/qt creator projects/FPGA_GPIO_Controller/gui/images/images/de10_nano_blue_crop.png")
            pixmap = QPixmap(path)
            # Load the image
            self.image_item.setPixmap(pixmap)
            self.image_item.setScale(0.3611)

            # Add the image item to the scene
            self.scene.addItem(self.image_item)

            #self.FPGA_IMAGE.setMask(pixmap.mask())
            self.backgroundWidgetTop = QWidget()
            self.backgroundWidgetTop.setStyleSheet(f"background-color: {color}; border-radius: {radius}")
            self.backgroundWidgetTop.setFixedSize(width, height)
            self.backgroundWidgetTop.setContentsMargins(sideBorders, topBorders, sideBorders, bottomBorders)
            

            self.backgroundWidgetBottom = QWidget()
            self.backgroundWidgetBottom.setStyleSheet(f"background-color: {color}; border-radius: {radius}")
            self.backgroundWidgetBottom.setFixedSize(width, height)
            self.backgroundWidgetBottom.setContentsMargins(sideBorders, topBorders, sideBorders, bottomBorders)
            
            self.backgroundWidgetLeft = QWidget()
            self.backgroundWidgetLeft.setStyleSheet(f"background-color: {color}; border-radius: {radius}")
            self.backgroundWidgetLeft.setFixedSize(height, width)
            self.backgroundWidgetLeft.setContentsMargins(sideBorders, topBorders, sideBorders, bottomBorders)
            self.backgroundWidgetRight = QWidget()
            self.backgroundWidgetRight.setStyleSheet(f"background-color: {color}; border-radius: {radius}")
            self.backgroundWidgetRight.setFixedSize(height, width)
            self.backgroundWidgetRight.setContentsMargins(sideBorders, topBorders, sideBorders, bottomBorders)
        

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

            # Create a grid layout to hold the buttons
            grid_layout_right = QGridLayout(self.backgroundWidgetRight)
            grid_layout_right.setHorizontalSpacing(vSpacing)
            grid_layout_right.setVerticalSpacing(buttonSpacing)

            # Create a grid layout to hold the buttons
            grid_layout_left = QGridLayout(self.backgroundWidgetLeft)
            grid_layout_left.setHorizontalSpacing(vSpacing)
            grid_layout_left.setVerticalSpacing(buttonSpacing)

            # Set the alignment of the grid layout to center vertically
            grid_layout_top.setAlignment(Qt.AlignVCenter)
            grid_layout_bottom.setAlignment(Qt.AlignVCenter)
            grid_layout_right.setAlignment(Qt.AlignHCenter)
            grid_layout_left.setAlignment(Qt.AlignHCenter)

            # Set the size policy of each row to Expanding
            for i in range(rows):
                grid_layout_top.setRowStretch(i, 1)
                grid_layout_bottom.setRowStretch(i, 1)
                grid_layout_right.setColumnStretch(i, 1)
                grid_layout_left.setColumnStretch(i, 1)


            # Set the size policy of each column to Expanding
            for j in range(columns):
                grid_layout_top.setColumnStretch(j, 1)
                grid_layout_bottom.setColumnStretch(j, 1)
                grid_layout_right.setRowStretch(j, 1)
                grid_layout_left.setRowStretch(j, 1)

            top_buttons = []
            bottom_buttons = []
            right_buttons = []
            left_buttons = []
            for i in range(columns):
                for j in range(rows):
                    avoid_text = ["GND", "VCC", "RST", "CLK", "UAR", "LED"]
                    buttonTop = PyIconButton(
                            btn_id = f"ButtonTop {i * rows + j + 1}",
                            icon_path = Functions.set_svg_icon(pin_theme_dict[pin_map_dict[(i*rows)+j][:3]]["icon"]),
                            parent = parent,
                            app_parent=app_parent,
                            tooltip_text = pin_map_dict[(i*rows)+j],
                            width = buttonWidth,
                            height = buttonHeight,
                            radius = buttonRadius,
                            dark_one = "#1b1e23",
                            icon_color          = pin_theme_dict[pin_map_dict[(i*rows)+j][:3]]["icon_color"],
                            icon_color_hover    = pin_theme_dict[pin_map_dict[(i*rows)+j][:3]]["icon_color_hover"],
                            icon_color_pressed  = pin_theme_dict[pin_map_dict[(i*rows)+j][:3]]["icon_color_pressed"],
                            icon_color_active   = pin_theme_dict[pin_map_dict[(i*rows)+j][:3]]["icon_color_active"],
                            bg_color            = pin_theme_dict[pin_map_dict[(i*rows)+j][:3]]["bg_color"],
                            bg_color_hover      = pin_theme_dict[pin_map_dict[(i*rows)+j][:3]]["bg_color_hover"],
                            bg_color_pressed    = pin_theme_dict[pin_map_dict[(i*rows)+j][:3]]["bg_color_pressed"],
                            context_color       = pin_theme_dict[pin_map_dict[(i*rows)+j][:3]]["context_color"],
                        )
                    top_buttons.append(buttonTop)
                    # Set the initial button state to unchecked
                    self.button_states.append(0)
                    
                    if(pin_map_dict[(i*rows)+j][:3] not in avoid_text):
                        buttonTop.clicked.connect(lambda _ = None, index=  (i*rows+ j): self.buttonStateUpdate(index))
                    grid_layout_top.addWidget(buttonTop, j, i)

                    buttonBottom = PyIconButton(
                            btn_id = f"ButtonBottom {i * rows + j + 1}",
                            icon_path = Functions.set_svg_icon(pin_theme_dict[pin_map_dict[(i*rows)+j + 56][:3]]["icon"]),
                            parent = parent,
                            app_parent=app_parent,
                            tooltip_text = pin_map_dict[(i*rows)+j +56],
                            width = buttonWidth,
                            height = buttonHeight,
                            radius = buttonRadius,
                            dark_one = "#1b1e23",
                            icon_color          = pin_theme_dict[pin_map_dict[(i*rows)+j + 56][:3]]["icon_color"],
                            icon_color_hover    = pin_theme_dict[pin_map_dict[(i*rows)+j + 56][:3]]["icon_color_hover"],
                            icon_color_pressed  = pin_theme_dict[pin_map_dict[(i*rows)+j + 56][:3]]["icon_color_pressed"],
                            icon_color_active   = pin_theme_dict[pin_map_dict[(i*rows)+j + 56][:3]]["icon_color_active"],
                            bg_color            = pin_theme_dict[pin_map_dict[(i*rows)+j + 56][:3]]["bg_color"],
                            bg_color_hover      = pin_theme_dict[pin_map_dict[(i*rows)+j + 56][:3]]["bg_color_hover"],
                            bg_color_pressed    = pin_theme_dict[pin_map_dict[(i*rows)+j + 56][:3]]["bg_color_pressed"],
                            context_color       = pin_theme_dict[pin_map_dict[(i*rows)+j + 56][:3]]["context_color"],
                        )
                    bottom_buttons.append(buttonBottom)
                    # Set the initial button state to unchecked
                    self.button_states.append(0)
                    if(pin_map_dict[(i*rows)+j+56][:3] not in avoid_text):
                        buttonBottom.clicked.connect(lambda _ = None, index=  (i*rows+ j + 56): self.buttonStateUpdate(index))
                    grid_layout_bottom.addWidget(buttonBottom, j, i)

                    buttonRight = PyIconButton(
                            btn_id = f"ButtonRight {i * rows + j + 1}",
                            icon_path = Functions.set_svg_icon(pin_theme_dict[pin_map_dict[(i*rows)+j +28][:3]]["icon"]),
                            parent = parent,
                            app_parent=app_parent,
                            tooltip_text = pin_map_dict[(i*rows)+j + 28],
                            width = buttonWidth,
                            height = buttonHeight,
                            radius = buttonRadius,
                            dark_one = "#1b1e23",
                            icon_color          = pin_theme_dict[pin_map_dict[(i*rows)+j+28][:3]]["icon_color"],
                            icon_color_hover    = pin_theme_dict[pin_map_dict[(i*rows)+j+28][:3]]["icon_color_hover"],
                            icon_color_pressed  = pin_theme_dict[pin_map_dict[(i*rows)+j+28][:3]]["icon_color_pressed"],
                            icon_color_active   = pin_theme_dict[pin_map_dict[(i*rows)+j+28][:3]]["icon_color_active"],
                            bg_color            = pin_theme_dict[pin_map_dict[(i*rows)+j+28][:3]]["bg_color"],
                            bg_color_hover      = pin_theme_dict[pin_map_dict[(i*rows)+j+28][:3]]["bg_color_hover"],
                            bg_color_pressed    = pin_theme_dict[pin_map_dict[(i*rows)+j+28][:3]]["bg_color_pressed"],
                            context_color       = pin_theme_dict[pin_map_dict[(i*rows)+j+28][:3]]["context_color"],
                        )
                    right_buttons.append(buttonRight)
                    # Set the initial button state to unchecked
                    self.button_states.append(0)
                    if(pin_map_dict[(i*rows)+j+28][:3] not in avoid_text):
                        buttonRight.clicked.connect(lambda _ = None, index=  (i*rows+ j + 28): self.buttonStateUpdate(index))
                    grid_layout_right.addWidget(buttonRight, i, j)

                    buttonLeft = PyIconButton(
                            btn_id = f"ButtonRight {i * rows + j + 1}",
                            icon_path = Functions.set_svg_icon(pin_theme_dict[pin_map_dict[(i*rows)+j+84][:3]]["icon"]),
                            parent = parent,
                            app_parent=app_parent,
                            tooltip_text = pin_map_dict[(i*rows)+j+84],
                            width = buttonWidth,
                            height = buttonHeight,
                            radius = buttonRadius,
                            dark_one = "#1b1e23",
                            icon_color          = pin_theme_dict[pin_map_dict[(i*rows)+j+84][:3]]["icon_color"],
                            icon_color_hover    = pin_theme_dict[pin_map_dict[(i*rows)+j+84][:3]]["icon_color_hover"],
                            icon_color_pressed  = pin_theme_dict[pin_map_dict[(i*rows)+j+84][:3]]["icon_color_pressed"],
                            icon_color_active   = pin_theme_dict[pin_map_dict[(i*rows)+j+84][:3]]["icon_color_active"],
                            bg_color            = pin_theme_dict[pin_map_dict[(i*rows)+j+84][:3]]["bg_color"],
                            bg_color_hover      = pin_theme_dict[pin_map_dict[(i*rows)+j+84][:3]]["bg_color_hover"],
                            bg_color_pressed    = pin_theme_dict[pin_map_dict[(i*rows)+j+84][:3]]["bg_color_pressed"],
                            context_color       = pin_theme_dict[pin_map_dict[(i*rows)+j+84][:3]]["context_color"],
                        )
                    left_buttons.append(buttonLeft)
                    # Set the initial button state to unchecked
                    self.button_states.append(0)
                    if(pin_map_dict[(i*rows)+j+84][:3] not in avoid_text):
                        buttonLeft.clicked.connect(lambda _ = None, index=  (i*rows+ j + 84): self.buttonStateUpdate(index))
                    grid_layout_left.addWidget(buttonLeft, i, j)

            for button in top_buttons:
                self.buttons.append(button)

            for button in right_buttons:
                self.buttons.append(button)

            for button in bottom_buttons:
                self.buttons.append(button)

            for button in left_buttons:
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
            
            
            # spacer_layout.addWidget(self.desel_all_button)
            # spacer_layout.addWidget(self.sel_all_button)

            self.sel_all_button.clicked.connect(self.selectAllButtons)
            self.desel_all_button.clicked.connect(self.deselectAllButtons)
            
            
            # This was done because the button was not showing up at the right position without being inside a widget
            # Create a QVBoxLayout
            layout1 = QVBoxLayout()

            # Create a QWidget to hold the layout
            widget1 = QWidget()
            widget1.setStyleSheet("background-color: transparent;")
            widget1.setLayout(layout1)
            layout1.addWidget(self.sel_all_button)

             # Create a QVBoxLayout
            layout2 = QVBoxLayout()

            # Create a QWidget to hold the layout
            widget2 = QWidget()
            widget2.setStyleSheet("background-color: transparent;")
            widget2.setLayout(layout2)
            layout2.addWidget(self.desel_all_button)

            sel_all_buttons_proxy = QGraphicsProxyWidget()
            sel_all_buttons_proxy.setWidget(widget1)
            sel_all_buttons_proxy.setPos(180, 175)

            self.scene.addItem(sel_all_buttons_proxy)

            desel_all_buttons_proxy = QGraphicsProxyWidget()
            desel_all_buttons_proxy.setWidget(widget2)
            desel_all_buttons_proxy.setPos(460, 175)
            
            self.scene.addItem(desel_all_buttons_proxy)

            top_buttons_proxy = QGraphicsProxyWidget()
            top_buttons_proxy.setWidget(self.backgroundWidgetTop)
            top_buttons_proxy.setPos(154,4)

            self.scene.addItem(top_buttons_proxy)

            bottom_buttons_proxy = QGraphicsProxyWidget()
            bottom_buttons_proxy.setWidget(self.backgroundWidgetBottom)
            bottom_buttons_proxy.setPos(154,308)

            self.scene.addItem(bottom_buttons_proxy)

            left_buttons_proxy = QGraphicsProxyWidget()
            left_buttons_proxy.setWidget(self.backgroundWidgetLeft)
            left_buttons_proxy.setPos(51,2)

            self.scene.addItem(left_buttons_proxy)

            right_buttons_proxy = QGraphicsProxyWidget()
            right_buttons_proxy.setWidget(self.backgroundWidgetRight)
            right_buttons_proxy.setPos(563,2)

            self.scene.addItem(right_buttons_proxy)

            

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setAlignment(Qt.AlignVCenter)
        main_layout.addWidget(self.view)


    
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
        bitCount = 0
        for index, state in enumerate(self.button_states):
            buttonText = self.buttons[index].get_tooltip_text()
            avoid_text = ["GND", "VCC", "RST", "CLK", "UAR", "LED"]
            if(buttonText[:3] not in avoid_text):
                print(buttonText, index)
                calc = calc + state*(2**bitCount)
                bitCount = bitCount + 1      

            if(bitCount == 8):
                writeVal.append(calc)
                calc = 0
                bitCount = 0
            elif(index == 107):
                writeVal.append(calc)
                
        
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
        
        