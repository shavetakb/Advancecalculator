from tkinter import *

def on_click(event):
    text = event.widget["text"]
    current = entry.get()

    if text == "=":
        try:
            current = current.replace("^", "**")
            result = str(eval(current))
            entry.delete(0, END)
            entry.insert(0, result)
        except:
            entry.delete(0, END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, END)
    elif text == "()":
        
        if entry.get().count("(") > entry.get().count(")"):
            entry.insert(END, ")")
        else:
            entry.insert(END, "(")
    else:
        entry.insert(END, text)

root = Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="#f0f8ff")  


entry = Entry(root, font="Arial 20", borderwidth=5, relief=RIDGE, justify=RIGHT, bg="#c1dada")
entry.pack(fill=X, ipadx=8, ipady=15, padx=10, pady=10)


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"],
    ["()", "%", ".", "^"]
]


for row in buttons:
    frame = Frame(root, bg="#f2f3f5")
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        if btn_text in "0123456789":
            bg_color = "#c0ccd1"
        elif btn_text in "+-*/%":
            bg_color = "#83a7aa"
        elif btn_text == "=":
            bg_color = "#8ca8b3"
        elif btn_text == "C":
            bg_color = "#ffb6b9"
        else:  # '()', '.', '^'
            bg_color = "#99d2d6"

        button = Button(frame, text=btn_text, font="Arial 18", bg=bg_color, fg="black", relief=RAISED, border=3)
        button.pack(side=LEFT, expand=True, fill="both", padx=2, pady=2)
        button.bind("<Button-1>", on_click)

root.mainloop()


