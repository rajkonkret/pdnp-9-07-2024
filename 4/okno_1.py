import tkinter as tk

root = tk.Tk()
root.title("Okno Tkinter")
root.geometry("640x480")
label = tk.Label(root, text="Hello, Tkinter")
label.pack()
root.mainloop()
