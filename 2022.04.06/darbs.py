from msilib.schema import RadioButton
import tkinter as tk
import tkinter.ttk as ttk

class Window:
    def __init__ (self, master):
        style = ttk.Style()
        print(style.theme_names())
        style.theme_create("custom")
        style.theme_use("default")
        style.theme_settings("default", {
           "TButton": {
               "configure": {"padding": 10},
               "map": {
                   "background": [("active", "yellow3"),
                                  ("!disabled", "yellow")],
                   "foreground": [("focus", "Red"),
                                  ("active", "green"),
                                  ("!disabled", "Blue")]
            }
           }
        })
        button = ttk.Button(master, text = "Uzspied uz mani" )
        button.pack(padx = 5, pady = 5)
        
        label = ttk.Label(master, text = "label")
        label.pack(padx = 5, pady = 5)

        radioButton = ttk.Radiobutton(master, text = "kaut kas ")
        radioButton.pack(padx = 3, pady = 3)

root = tk.Tk()
root.geometry('200x200')
window = Window(root)
root.mainloop()
