import tkinter as tk

def create_pedidos(frame_tk):
    frame_tk.pack(side="top",fill="both",expand=True)
    frame_tk.pack_propagate(False)

    # Adicionando widgets ao frame
    label = tk.Label(frame_tk, text="pedidos", bg="#EEE8AA")
    label.grid(row=0,column=0)