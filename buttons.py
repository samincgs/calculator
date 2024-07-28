from customtkinter import CTkButton
from settings import *

class Button(CTkButton):
    def __init__(self, parent, text, col, row, font, color='dark-gray'):
        super().__init__(master=parent, 
                         text=text, 
                         corner_radius=STYLES['corner-radius'],
                         font=font,
                         fg_color=COLORS[color]['fg'],
                         hover_color=COLORS[color]['hover'],
                         text_color=COLORS[color]['text']
                         )
        self.grid(column=col, row=row, sticky='nsew') 