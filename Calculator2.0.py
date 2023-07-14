import math
import tkinter as tk

calculation = ""
def add_to_calculation(symbol):
    global calculation 
    calculation =+ str(symbol)
    Text_result.delete(1.0, "end")
    Text_result.insert(1.0, calculation)

def evaluate_calculation():
    pass
def clear_field():
    pass

root = tk.Tk()
root.title("AKing Calculator 2.0")
root.geometry("500x500")


Text_result = tk.Text (root, height=2, width=30, font=("Arial", 24))
Text_result.grid(columnspan=5)
root.mainloop()
