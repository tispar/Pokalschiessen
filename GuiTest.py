import tkinter as tk

# Test, ob tkinter korrekt funktioniert
#tkinter._test()

root = tk.Tk()
root.title("Programmname")
root.geometry("800x600")
root.minsize(width=640, height= 480)
root.maxsize(width=1280, height= 720)

#root.resizable(width= False, height = False)

label1 = tk.Label(root, text="Hallo Welt")
label1.pack()

root.mainloop() 