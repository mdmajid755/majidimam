from tkinter import *


class MathOperations:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b != 0:
            result = a / b
        else:
            result = "Cannot divide by zero"
        return result


class Calculator:
    def __init__(self, window):
        window.geometry("350x350")
        window.resizable(0, 0)
        window.title("Calculator")
        self.math_operations = MathOperations()
        self.window = window
        self.current_operation = None
        self.operand1 = ""
        self.operand2 = ""
        self.create_ui_elements()

    def create_ui_elements(self):
        self.input_text = StringVar()

        input_frame = Frame(self.window, width=312, height=50, bd=0, highlightbackground="white", highlightcolor="grey",
                            highlightthickness=2)
        input_frame.pack(side=TOP)
        input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#aaa",
                            justify=RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        buttons = Frame(window, width=320, height=280, bg="white")
        buttons.pack()
        button1 = Button(buttons, text=' 1 ', fg='black', bg='gray',
                         command=lambda: self.press(1), height=1, width=5)
        button1.grid(row=2, column=0)
        button2 = Button(buttons, text=' 2 ', fg='black', bg='gray',
                         command=lambda: self.press(2), height=1, width=5)
        button2.grid(row=2, column=1)
        button3 = Button(buttons, text=' 3 ', fg='black', bg='gray',
                         command=lambda: self.press(3), height=1, width=5)
        button3.grid(row=2, column=2)
        button4 = Button(buttons, text=' 4 ', fg='black', bg='gray',
                         command=lambda: self.press(4), height=1, width=5)
        button4.grid(row=3, column=0)
        button5 = Button(buttons, text=' 5 ', fg='black', bg='gray',
                         command=lambda: self.press(5), height=1, width=5)
        button5.grid(row=3, column=1)
        button6 = Button(buttons, text=' 6 ', fg='black', bg='gray',
                         command=lambda: self.press(6), height=1, width=5)
        button6.grid(row=3, column=2)
        button7 = Button(buttons, text=' 7 ', fg='black', bg='gray',
                         command=lambda: self.press(7), height=1, width=5)
        button7.grid(row=4, column=0)
        button8 = Button(buttons, text=' 8 ', fg='black', bg='gray',
                         command=lambda: self.press(8), height=1, width=5)
        button8.grid(row=4, column=1)

        button9 = Button(buttons, text=' 9 ', fg='black', bg='gray',
                         command=lambda: self.press(9), height=1, width=5)
        button9.grid(row=4, column=2)
        button0 = Button(buttons, text=' 0 ', fg='black', bg='gray',
                         command=lambda: self.press(0), height=1, width=5)
        button0.grid(row=5, column=0)
        plus = Button(buttons, text=' + ', fg='black', bg='gray',
                      command=lambda: self.press("+"), height=1, width=5)
        plus.grid(row=2, column=3)
        minus = Button(buttons, text=' - ', fg='black', bg='gray',
                       command=lambda: self.press("-"), height=1, width=5)
        minus.grid(row=3, column=3)
        multiply = Button(buttons, text=' * ', fg='black', bg='gray',
                          command=lambda: self.press("*"), height=1, width=5)
        multiply.grid(row=4, column=3)
        divide = Button(buttons, text=' / ', fg='black', bg='gray',
                        command=lambda: self.press("/"), height=1, width=5)
        divide.grid(row=5, column=3)
        equal = Button(buttons, text=' = ', fg='black', bg='gray',
                       command=lambda: self.button_equal_clicked(), height=1, width=5)
        equal.grid(row=5, column=2)
        clear = Button(buttons, text='Clear', fg='black', bg='red',
                       command=lambda: self.button_clear_click(), height=1, width=5)
        clear.grid(row=5, column=1)

    def button_clear_click(self):
        self.input_text.set("")
        self.operand1 = ""
        self.operand2 = ""
        self.current_operation = None

    def button_equal_clicked(self):
        if self.operand1 and self.operand2 and self.current_operation:
            result = self.calculate()
            self.input_text.set(result)
            self.operand1 = result
            self.operand2 = ""
            self.current_operation = None

    def press(self, symbol):
        print("press", symbol)
        if str(symbol).isdigit() or symbol == ".":
            if not self.current_operation:
                self.operand1 += str(symbol)
            else:
                self.operand2 += str(symbol)
            self.input_text.set(self.operand1 + (self.current_operation or "") + self.operand2)
        elif symbol in {"+", "-", "*", "/"}:
            if self.operand1 and not self.operand2:
                self.current_operation = symbol
                self.input_text.set(self.operand1 + symbol)
            elif self.operand1 and self.operand2:
                self.button_equal_clicked()

    def calculate(self):
        if self.operand1 and self.operand2 and self.current_operation:
            try:
                operand1 = float(self.operand1)
                operand2 = float(self.operand2)

                if self.current_operation == "+":
                    result = self.math_operations.add(operand1, operand2)
                elif self.current_operation == "-":
                    result = self.math_operations.sub(operand1, operand2)
                elif self.current_operation == "*":
                    result = self.math_operations.mul(operand1, operand2)
                elif self.current_operation == "/":
                    result = self.math_operations.div(operand1, operand2)
                return result
            except Exception as e:
                print("Error in calculation:", e)
                return "Error"


if __name__ == "__main__":
    window = Tk()
    calculator = Calculator(window)
    window.mainloop()
