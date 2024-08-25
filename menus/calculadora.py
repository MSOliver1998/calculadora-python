import tkinter as tk 

def create_calculadora(frame_tk):
    frame_tk.pack(side="top",expand=True,fill="both")
    frame_tk.pack_propagate(False) 

    label=tk.Label(frame_tk,text="calculadora",bg="#F5FFFA")
    label.grid(row=0,column=0)