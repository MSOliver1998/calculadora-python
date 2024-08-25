import tkinter as tk

def create_lista(frame_tk):    
    
    frame_tk.pack(side="top",fill="both",expand=True)
    frame_tk.pack_propagate(False)

    label=tk.Label(frame_tk,text="lista de compras",bg="#B0E0E6")
    label.grid(row=0,column=0)
