#size
WINDOW_SIZE = (400, 700)
MAIN_ROWS = 7
MAIN_COLS = 4

#text
FONT = 'Helvetica'
OUTPUT_FONT_SIZE = 66
NORMAL_FONT_SIZE = 30

#styles
STYLES = {
    'corner-radius' : 0,
    'gap': 0.5
}

# operators
OPERATORS = {
    'clear' : {'col' : 0, 'row': 2, 'text': 'AC', 'image_path' : None },
    'invert' : {'col' : 1, 'row': 2, 'text': '', 'image_path' : {'light' : 'images/invert_light.png', 'dark' : 'images/invert_dark.png'} },
    'percent': {'col' : 2, 'row': 2, 'text': '%', 'image_path' : None },
    
}














# colors
BLACK = '#000000'
WHITE = '#EEEEEE'

COLORS = {
    'dark-gray' : {'fg' : ('#DDDDDA','#545454'), 'hover' : ('#B6B6AF','#6A6A6A'), 'text' : (BLACK,WHITE)},
    
}