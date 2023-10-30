import tkinter as tk
import tkinter.ttk as ttk

def clearTextBox():
    global textBox
    textBox.delete('1.0',tk.END)

window = tk.Tk()
window.title('Hello Python')
#window.geometry("300x200+10+20")

myImage= tk.PhotoImage(file='Screenshot.png')

greeting = tk.Label(text="Hello, Tkinter")
#greeting['image'] = myImage
ttkgreating = ttk.Label(text="Hello Tkinter ttk")
greeting.pack()
ttkgreating.pack()


styledLabel = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width=500,
    height=500,
    image=myImage
)

styledLabel.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=clearTextBox,
)
button.pack()

entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()

entry.insert(0,"entered by program")

textBox=tk.Text()
textBox.pack()

myFrame =tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=10)
myFrame.pack(fill=tk.Y,side=tk.BOTTOM)

frameLabel = ttk.Label(master=myFrame, text='label in frame')
frameLabel.pack()

frameButton =ttk.Button(master=myFrame, text="frame button")
frameButton.pack()


preciseFrame = tk.Frame(master=window, width=150, height=150)
preciseFrame.pack()

label1 = tk.Label(master=preciseFrame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=preciseFrame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)
outerGridFrame = tk.Frame(master=window)
outerGridFrame.pack(fill=tk.BOTH, expand=True)

for i in range(3):
    outerGridFrame.columnconfigure(i, weight=1, minsize=75)
    outerGridFrame.rowconfigure(i, weight=1, minsize=50)
    outerGridFrame.rowconfigure(i+3, weight=1, minsize=50)
    for j in range(3):
        gridFrame = tk.Frame(
            master=outerGridFrame,
            relief=tk.RAISED,
            borderwidth=1
        )
        gridFrame.grid(row=i, column=j, padx=3)
        btn = tk.Label(master=gridFrame, text=f"Row {i}\nColumn {j}")
        btn.pack()

        gridFrame = tk.Frame(
            master=outerGridFrame,
            relief=tk.RAISED,
            borderwidth=1
        )
        gridFrame.grid(row=3+i, column=j, padx=3)
        btn = tk.Button(master=gridFrame, text=f"Row {i}\nColumn {j}")
        btn.pack()


window.mainloop()

print("done")
