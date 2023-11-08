import tkinter as tk
from tkinter import ttk
class SimpleCalc:
    def __init__(self, root):
        self.root = root
        self.root.title("Visual Simple Calculator")
        self.root.geometry("550x300")
        self.expression = ""
        self.result = tk.StringVar()       
        style = ttk.Style()
        style.configure("TButton", background="black", foreground="grey", font=("Arial", 14))       
        button_frame = ttk.Frame(root)
        button_frame.grid(row=1, column=0)        
        self.entry = tk.Entry(root, textvariable=self.result, font=("Arial", 18), bg="black", fg="white")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        button_labels = [
            '1', '2', '3', '+',
            '4', '5', '6', '-',
            '7', '8', '9', '*',
            '0', 'Clear', '=', '/'
        ]
        row = 0
        col = 0
        for label in button_labels:
            if label in {'C', '='}:
                button = ttk.Button(button_frame, text=label, width=10, command=lambda l=label: self.on_button_click(l), style="TButton")
            else:
                button = ttk.Button(button_frame, text=label, width=10, command=lambda l=label: self.on_button_click(l))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
    
    def on_button_click(self, label):
        if label == '=':
            try:
                self.expression = str(eval(self.expression))
            except ZeroDivisionError:
                self.expression = "Error"
        elif label == 'Clear':
            self.expression = ""
        else:
            self.expression += label
        self.result.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalc(root)
    root.configure(bg="grey")  
    root.mainloop()