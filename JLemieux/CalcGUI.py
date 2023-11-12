import tkinter as tk

# define the calculator class
class SimpleCalc:
    # current result starts at 0 and there's no operation
    def __init__(self):
        self.result = 0
        self.current = ""
        self.operation = None

    # adds string of a number to the current input
    def add(self, num):
        self.current += str(num)

    # updates the result w/ current input as a float, resets the current input, and stores op 
    def set_operation(self, op):
        if self.current:
            self.result = float(self.current)
            self.current = ""
            self.operation = op

    # if an operation was pressed and there's a value for current input
    def calculate(self):
        if self.operation is not None and self.current:
            if self.operation == "+":
                self.result += float(self.current)
            elif self.operation == "-":
                self.result -= float(self.current)
            elif self.operation == "*":
                self.result *= float(self.current)
            elif self.operation == "/":
                self.result /= float(self.current)
            # converts result back to a string
            self.current = str(self.result)

    # clear calc
    def clear_entry(self):
        self.current = ""

    # backspace
    def backspace(self):
        if self.current:
            self.current = self.current[:-1]

# GUI
class CalculatorApp:
    def __init__(self, master):
        # instance of calculator
        self.calc = SimpleCalc()

        # textbox for input, top of window at row0 and column0 spanning 4 columns
        self.result_display = tk.Entry(master, font=('Arial', 24), justify='right', bd=10)
        self.result_display.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'Clear', 'AC'  
        ]

        # starts at row1 because textbox is above
        row = 1
        col = 0

        # a loop iterating through the buttons, lambda passes button text as argument for button click function
        for button_text in buttons:
            tk.Button(master, text=button_text, font=('Arial', 18), width=5, command=lambda text=button_text: self.button_click(text)).grid(row=row, column=col, sticky='nsew')
            # keeping track of position in the grid
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # clear backspace button, made span two columns
        tk.Button(master, text='Clear', font=('Arial', 18), width=5, command=lambda: self.button_click('Clear')).grid(row=5, column=0, columnspan=2, sticky='nsew')

        # all clear button, made span two columns
        tk.Button(master, text='AC', font=('Arial', 18), width=5, command=lambda: self.button_click('AC')).grid(row=5, column=2, columnspan=2, sticky='nsew')

    # button functions
    def button_click(self, text):
        # loop
        # updates the textbox to show the result of a calculation and then clears the current input
        if text == '=':
            self.calc.calculate() # since = was pressed, it calls the calculate function
            self.result_display.delete(0, tk.END) # clears what's displayed
            self.result_display.insert(0, self.calc.current) # inserts the result of the calculation function
            self.calc.current = "" # clears current calc
            self.calc.operation = None # clears operation
        
        # updating the textbox to backspace what's in there
        elif text == 'Clear':
            self.calc.backspace() # calls backspace function
            self.result_display.delete(0, tk.END)
            self.result_display.insert(0, self.calc.current)
        
        # new instance of calculator which resets it. clear textbox
        elif text == 'AC':
            self.calc = SimpleCalc()
            self.result_display.delete(0, tk.END)

        # everything else must be a number or op
        else:
            # if number or decimal, add it to the textbox
            if text in '0123456789.':
                self.calc.add(text)
                self.result_display.insert(tk.END, text)
            # if operation, add it as well
            else:
                self.calc.set_operation(text)
                self.result_display.insert(tk.END, text)

# running directly
if __name__ == '__main__':
    # creates window for app
    root = tk.Tk()
    # title
    root.title("Simple Calculator")

    # creates instance of app
    app = CalculatorApp(root)

    # sets up grid layout for window
    for i in range(5):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    # starts main event loop and keeps program running unless exited
    root.mainloop()
