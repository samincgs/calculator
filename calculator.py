import customtkinter as ctk
import darkdetect
from PIL import Image
from settings import *
from buttons import Button, ImageButton, NumButton

class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        super().__init__(fg_color=(WHITE, BLACK))
        ctk.set_appearance_mode('dark' if is_dark else 'light')
        self.title('Calculator')
        self.geometry(f'{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}')
        self.iconbitmap('empty.ico')
        self.resizable(False, False)
        
        #layout
        rows = list(range(MAIN_ROWS))
        cols = list(range(MAIN_COLS))
        self.rowconfigure(rows, weight=1, uniform='a')
        self.grid_columnconfigure(cols, weight=1, uniform='a')
        
        #data
        self.formula_string = ctk.StringVar(value='')
        self.result_string = ctk.StringVar(value='0')
        
        #widgets
        self.create_widgets()
        
        #run
        self.mainloop()

    
    def create_widgets(self):
        #fonts
        main_font = ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)
        
        #output labels
        OutputLabel(self, 0, 'se', main_font, self.formula_string) # formula
        OutputLabel(self, 1, 'e', result_font, self.result_string) # result
        
        # clear button (AC)
        Button(parent = self, 
               func= self.clear,
               text= OPERATORS['clear']['text'], 
               col = OPERATORS['clear']['col'], 
               row = OPERATORS['clear']['row'],
               font=main_font,
               )
        
        # percentage button %
        Button(parent = self, 
               func= self.percent,
               text= OPERATORS['percent']['text'], 
               col = OPERATORS['percent']['col'], 
               row = OPERATORS['percent']['row'],
               font=main_font,
               )

        #invert button
        invert_image = ctk.CTkImage(light_image= Image.open(OPERATORS['invert']['image_path']['dark']), 
                                    dark_image= Image.open(OPERATORS['invert']['image_path']['light']))
        ImageButton(parent = self, 
               func= self.invert,
               col = OPERATORS['invert']['col'], 
               row = OPERATORS['invert']['row'],
               image=invert_image)
        
        # number buttons
        for num,data in NUMBERS.items():
                NumButton(
                    parent= self,
                    text=num,
                    func = self.num_press,
                    col = data['col'],
                    row = data['row'],
                    font=main_font,
                    span=data['span']
                )
    
    def num_press(self, value):
        print(value)
    
    def clear(self):
        print('clear')
        
    def percent(self):
        print('percent')
        
    def invert(self):
        print('invert')

class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master=parent, textvariable=string_var, font=font)
        self.grid(row = row, column = 0, columnspan = 4, sticky = anchor, padx = 10)

if __name__ == '__main__':
    is_dark = darkdetect.isDark()
    # Calculator(False)
    Calculator(is_dark)