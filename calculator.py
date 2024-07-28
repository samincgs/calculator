import customtkinter as ctk
import darkdetect
from settings import *

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
        
        # widgets
        self.create_widgets()
        
        # run
        self.mainloop()

    def create_widgets(self):
        #output labels
        OutputLabel(self, 0, 'se') # formula
        OutputLabel(self, 1, 'e') # result

class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor):
        super().__init__(master=parent, text='123')
        self.grid(row = row, column = 0, columnspan = 4, sticky = anchor, padx = 10)
        

if __name__ == '__main__':
    is_dark = darkdetect.isDark()
    Calculator(is_dark)