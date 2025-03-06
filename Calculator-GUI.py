"""
This is a simple calculator app using Tkinter.
The app consists of a label to display the current calculation and result,
and buttons for digits, basic arithmetic operations (+, -, *, /), 
a 'Clear' button to reset the display, and an 'Equals' button to evaluate the expression.
"""

import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.display = tk.Label(root, text="", height=2, font=("Arial", 30), anchor="e")
        self.display.grid(row=0, column=0, columnspan=4)

        self.buttons = [
            ('1', '2', '3', '+'),
            ('4', '5', '6', '-'),
            ('7', '8', '9', '*'),
            ('0', '.', '=', '/')
        ]
        
        self.create_buttons()
        
    def create_buttons(self):
        row = 1
        for button_row in self.buttons:
            col = 0
            for button_text in button_row:
                button = tk.Button(self.root, text=button_text, height=3, width=6, font=("Arial", 20), command=lambda text=button_text: self.button_click(text))
                button.grid(row=row, column=col)
                col += 1
            row += 1
        
        clear_button = tk.Button(self.root, text="Clear", height=3, width=6, font=("Arial", 20), command=self.clear_display)
        clear_button.grid(row=row, column=0, columnspan=4)

    def button_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.display["text"]))
                self.display.config(text=result)
            except (SyntaxError, ZeroDivisionError):
                self.display.config(text="Error")
        else:
            current_text = self.display["text"]
            self.display.config(text=current_text + text)
    
    def clear_display(self):
        self.display.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
