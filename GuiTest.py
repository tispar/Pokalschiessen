import tkinter as tk

# Test, ob tkinter korrekt funktioniert
#tkinter._test()

root = tk.Tk()

#Settings
root.title("Programmname")
root.geometry("800x600")
root.minsize(width=640, height= 480)
root.maxsize(width=1280, height= 720)

#root.resizable(width= False, height = False)

#creating
label1 = tk.Label(root, text="Hallo Welt")
label2 = tk.Label(root, text="Ich heiße Kai")

#placing
#label1.pack()
label1.grid(row=0, column=0)
label2.grid(row=1, column=3)

#crating and placing at once
label3 = tk.Label(root, text="Test").grid(row=5 , column=2)

#Creating buttons
def myClick():
    myLabel = tk.Label(root, text="Ein Button wurde geklickt!")
    myLabel.grid(row=6, column=1)

myButton = tk.Button(root, text="Klick mich", padx=20 , pady=20, command=myClick , fg="red", bg="blue")
myButton.grid(row=6, column=0)

root.mainloop() 