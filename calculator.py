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
        
        
        # run
        self.mainloop()



if __name__ == '__main__':
    is_dark = darkdetect.isDark()
    Calculator(is_dark)