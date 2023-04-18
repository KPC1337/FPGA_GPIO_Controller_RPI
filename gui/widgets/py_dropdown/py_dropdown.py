from qt_core import *

style = '''
QComboBox{{
	background-color: {_bg_color};
	border-radius: {_radius};
	border: {_border_size}px solid {_border_color};
	padding: 5px;
	padding-left: 10px;
}}
QComboBox:hover{{
	border: {_border_size}px solid {_hover_color};
}}
QComboBox::drop-down {{
	subcontrol-origin: padding;
	subcontrol-position: top right;
	width: {_width}px; 
	border-left-width: 3px;
	border-left-color: {_border_right_color};
	border-left-style: solid;
	border-top-right-radius: 3px;
	border-bottom-right-radius: 3px;	
	background-image: url(gui/images/png_icons/cil-arrow-bottom.png);
	background-position: center;
	background-repeat: no-repeat;
}}
QComboBox QAbstractItemView {{
	color: {_item_text_color};	
	background-color: {_item_background_color};
	padding: 10px;
	selection-background-color: {_selection_background_color};
}}

/* /////////////////////////////////////////////////////////////////////////////////////////////////
QScrollArea */

QScrollArea {{	
	background-color: {_bg_color};
	padding: 5px;
	border-radius: {_radius}px;
    color: {_color};
}}

/* /////////////////////////////////////////////////////////////////////////////////////////////////
ScrollBars */
QScrollBar:horizontal {{
    border: none;
    background: {_scroll_bar_bg_color};
    height: 8px;
    margin: 0px 21px 0 21px;
	border-radius: 0px;
}}
QScrollBar::handle:horizontal {{
    background: {_context_color};
    min-width: 25px;
	border-radius: 4px
}}
QScrollBar::add-line:horizontal {{
    border: none;
    background: {_scroll_bar_btn_color};
    width: 20px;
	border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}}
QScrollBar::sub-line:horizontal {{
    border: none;
    background: {_scroll_bar_btn_color};
    width: 20px;
	border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{{
     background: none;
}}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{{
     background: none;
}}
QScrollBar:vertical {{
	border: none;
    background: {_scroll_bar_bg_color};
    width: 8px;
    margin: 21px 0 21px 0;
	border-radius: 0px;
}}
QScrollBar::handle:vertical {{	
	background: {_context_color};
    min-height: 25px;
	border-radius: 4px
}}
QScrollBar::add-line:vertical {{
     border: none;
    background: {_scroll_bar_btn_color};
     height: 20px;
	border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
}}
QScrollBar::sub-line:vertical {{
	border: none;
    background: {_scroll_bar_btn_color};
     height: 20px;
	border-top-left-radius: 4px;
    border-top-right-radius: 4px;
     subcontrol-position: top;
     subcontrol-origin: margin;
}}
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
     background: none;
}}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
     background: none;
}}
'''
class PyDropDown(QComboBox):
    def __init__(
            self, 
            bg_color = "#1B1D23",
            radius = 5,
            name = None,
            border_size = 2,
            border_color = "#21252B",
            hover_color = "#404758",
            item_text_color = "#FF79C6",
            item_background_color = "#21252B",
            selection_background_colour = "#272C36",
            scroll_bar_bg_color = "#272c36",
            scroll_bar_btn_color = "#333333",
            context_color = "#00ABE8", 
            border_right_color = "#272c36",
            color = "#FFF",
            width = 25,
        ):
        super().__init__()

        # SET STYLESHEET
        self.set_stylesheet(
            radius,
            border_size,
            border_color,
            hover_color,
            item_text_color,
            width,
            item_background_color,
            selection_background_colour,
            scroll_bar_bg_color,
            scroll_bar_btn_color,
            context_color, 
            bg_color,
            border_right_color,
            color
        )
        self.setObjectName(name)

    # SET STYLESHEET
    def set_stylesheet(
        self,
        radius,
        border_size,
        border_color,
        hover_color,
        item_text_color,
        width,
        item_background_color,
        selection_background_colour,
        context_color,
        scroll_bar_btn_color,
        scroll_bar_bg_color,
        bg_color,
        border_right_color,
        color
    ):
        # APPLY STYLESHEET
        style_format = style.format(
            _radius = radius,
            _border_size =border_size,
            _border_color = border_color,
            _hover_color = hover_color,
            _item_text_color = item_text_color,
            _width = width,
            _item_background_color = item_background_color,
            _selection_background_color = selection_background_colour,
            _scroll_bar_bg_color = scroll_bar_bg_color,
            _scroll_bar_btn_color = scroll_bar_btn_color,
            _context_color = context_color, 
            _bg_color = bg_color,
            _border_right_color = border_right_color,
            _color = color
        )
        self.setStyleSheet(style_format)