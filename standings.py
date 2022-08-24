#Initalisierung (imports, Variablen, laden von gespeicherten Variablen)
import tkinter as tk

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print("width: " + str(screen_width) + " height: " + str(screen_height))

root.minsize(width=int(screen_width/2), height= int(screen_height/2))
root.maxsize(width=screen_width, height= screen_height)

root.title("Pokalschießen Rönneburg 2022")
root.geometry(str(int(screen_width/2))+"x"+str(screen_height))

JubiläumspokalButton = tk.Button(root, text="Jubiläumspokal", padx=20 , pady=20)
BestmannButton = tk.Button(root,text="Bestmann", padx=20 , pady=20)
PreisButton = tk.Button(root,text="Preisschießen", padx=20 , pady=20)

JubiläumspokalButton.pack(pady=50, padx=50)
BestmannButton.pack(pady=50, padx=50)
PreisButton.pack(pady=50, padx=50)

root.mainloop() 

#Hauptmenü

