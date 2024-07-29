import customtkinter as ctk
import darkdetect
from PIL import Image
from settings import *
from buttons import Button, ImageButton, NumButton, MathButton, MathImageButton

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
        self.display_nums = []
        self.full_operation = []
        
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
                
        # math buttons
        for operator, data in MATH_BUTTONS.items():
            if operator == '/':
                # image button
                divide_image = ctk.CTkImage(light_image=Image.open(data['image_path']['dark']), 
                                            dark_image=Image.open(data['image_path']['light']))
                MathImageButton(
                    parent = self,
                    operator = operator, 
                    func=self.math_press, 
                    col = data['col'], 
                    row = data['row'], 
                    image = divide_image
                )
            else:
                MathButton(
                    parent=self,
                    text=data['character'],
                    operator=operator,
                    func=self.math_press,
                    col = data['col'],
                    row = data['row'],
                    font=main_font
                )
    
    
    
    def num_press(self, value):
        self.display_nums.append(str(value))
        full_num = ''.join(self.display_nums)
        self.result_string.set(full_num)
    
    def math_press(self, value):
        current_num = ''.join(self.display_nums)
        
        if current_num:
            self.full_operation.append(current_num)
            if value != '=':
                #update data
                self.full_operation.append(value)
                self.display_nums.clear()
                
                #display data
                self.result_string.set('')
                self.formula_string.set(' '.join(self.full_operation))
            else:
                formula = ' '.join(self.full_operation)
                result = eval(formula)
                
                #format the result
                if isinstance(result, float):
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 3)
                
                # update output
                self.formula_string.set(formula)
                self.result_string.set(result)
                
                self.full_operation.clear()
                self.display_nums.clear()
                
                self.display_nums.append(str(result))
                
    def clear(self):
        self.display_nums.clear()
        self.full_operation.clear()
        
        self.result_string.set(0)
        self.formula_string.set('')
        
    def percent(self):
        current_number = ''.join(self.display_nums)
        
        if current_number:
            result = float(current_number) / 100
            
            self.result_string.set(result)
            self.display_nums.pop()
            self.display_nums.append(str(result))
              
    def invert(self):
        current_number = ''.join(self.display_nums)
        
        if current_number:
            # positive or negative
            if float(current_number) > 0:
                self.display_nums.insert(0, '-')
            else:
                if current_number[0] == '-':
                    self.display_nums.pop(0)
                     
            current_number = ''.join(self.display_nums)
            self.result_string.set(current_number)
        

class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master=parent, textvariable=string_var, font=font)
        self.grid(row = row, column = 0, columnspan = 4, sticky = anchor, padx = 10)

if __name__ == '__main__':
    is_dark = darkdetect.isDark()
    # Calculator(False)
    Calculator(is_dark)