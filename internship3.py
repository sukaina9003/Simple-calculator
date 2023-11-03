import tkinter as tk

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.geometry("300x400")
root.title("Simple Calculator")
root.configure(bg="light blue")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill="both", padx=10, pady=10, ipadx=8, ipady=8, expand=True)

button_frame = tk.Frame(root)
button_frame.configure(bg="light pink")

button_frame.pack()

button_texts = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in button_texts:
    button = tk.Button(button_frame, text=text, font="lucida 15", padx=20, pady=20)
    button.grid(row=row, column=col)
    button.configure(bg="light pink")

    button.bind("<Button-1>", click)
  
root.mainloop()
