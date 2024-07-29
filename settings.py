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

#numbers
NUMBERS = {
    '.' : {'col' : 2, 'row': 6, 'span': 1},
    0: {'col' : 0, 'row': 6, 'span': 2},
    1: {'col' : 0, 'row': 5, 'span': 1},
    2: {'col' : 1, 'row': 5, 'span': 1},
    3: {'col' : 2, 'row': 5, 'span': 1},
    4: {'col' : 0, 'row': 4, 'span': 1},
    5: {'col' : 1, 'row': 4, 'span': 1},
    6: {'col' : 2, 'row': 4, 'span': 1},
    7: {'col' : 0, 'row': 3, 'span': 1},
    8: {'col' : 1, 'row': 3, 'span': 1},
    9: {'col' : 2, 'row': 3, 'span': 1},
}

MATH_BUTTONS = {
    '/' : {'col' : '3', 'row' : '2', 'character' : '',  'image_path' : { 'light' : 'images/divide_light.png', 'dark' : 'images/divide_dark.png'}},
    '*' : {'col' : '3', 'row' : '3', 'character' : 'x',  'image_path' : None},
    '-' : {'col' : '3', 'row' : '4', 'character' : '-',  'image_path' : None},
    '+' : {'col' : '3', 'row' : '5', 'character' : '+',  'image_path' : None},
    '=' : {'col' : '3', 'row' : '6', 'character' : '=', 'image_path' : None},
}

# colors
BLACK = '#000000'
WHITE = '#EEEEEE'

COLORS = {
    'dark-gray' : {'fg' : ('#DDDDDA','#545454'), 'hover' : ('#B6B6AF','#6A6A6A'), 'text' : (BLACK,WHITE)},
    'light-gray' : {'fg' : ('#DDDDDA','#BBBBBB'), 'hover' : ('#B6B6AF','#DEDEDE'), 'text' : (WHITE,BLACK)}, # fix light version of light gray
    'orange' : {'fg' : ('#DDDDDA','#FFA500'), 'hover' : ('#B6B6AF','#DEDEDE'), 'text' : (BLACK,WHITE)}, # fix light version of orange
    
}