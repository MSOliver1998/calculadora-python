import tkinter as tk
from menus.compras import create_lista 
from menus.venda import create_vendas
from menus.pedidos import create_pedidos
from menus.catalogo import create_catalogo
from menus.calculadora import create_calculadora

frame_tk=None

def pedidos():
    global frame_tk
    if frame_tk is not None:
        frame_tk.destroy()
    # Criação do frame que ocupará toda a largura da janela
    frame_tk = tk.Frame(root, bg="#EEE8AA",height=500,width=500)
    create_pedidos(frame_tk)
    
def venda():
    global frame_tk
    if frame_tk is not None:
        frame_tk.destroy()
    frame_tk = tk.Frame(root,width=500,height=500,background="#D8BFD8")
    create_vendas(frame_tk)

def lista_de_compras():
    global frame_tk
    if frame_tk is not None:
        frame_tk.destroy()
    frame_tk=tk.Frame(root,bg="#B0E0E6",width=500,height=500)
    create_lista(frame_tk)
    
def calculadora():
    global frame_tk
    if frame_tk is not None:
        frame_tk.destroy()
    frame_tk=tk.Frame(root,bg="#F5FFFA",width=500,height=500)
    create_calculadora(frame_tk)

def catalogo():
    global frame_tk
    if frame_tk is not None:
        frame_tk.destroy()
    frame_tk=tk.Frame(root,bg="#FFC0CB",width=500,height=500)
    create_catalogo(frame_tk)

#janela principal
root = tk.Tk()
root.title("Sunshine")
root["bg"]="#DB7093"
root.geometry("500x500")

#widgets
top_frame=tk.Frame(root,background="yellow",height=30,width=500)
top_frame.grid_propagate(False)
frame_tk=tk.Frame(root,background="#D8BFD8",width=500,height=500)
frame_tk.grid_propagate(False)
venda()

venda_btn=tk.Button(top_frame,text="venda",fg="black",bg="#D8BFD8",command=venda)
pedidos_btn=tk.Button(top_frame,text="pedidos",fg="black",bg="#EEE8AA",command=pedidos)
lista_de_compras_btn=tk.Button(top_frame,text="compras",bg="#B0E0E6",fg="black",command=lista_de_compras)
catalogo_btn=tk.Button(top_frame,text="catalogo",bg="#FFC0CB",fg="black",command=catalogo)
calculadora_btn=tk.Button(top_frame,text="calculadora",bg="#F5FFFA",fg="black",command=calculadora)


# posições
top_frame.pack(side="top")
frame_tk.pack(side="bottom")

venda_btn.grid(row=0,column=0)
pedidos_btn.grid(row=0,column=1)
lista_de_compras_btn.grid(row=0,column=2)
catalogo_btn.grid(row=0,column=3)
calculadora_btn.grid(row=0,column=4)

# Inicia o loop principal da interface gráfica
root.mainloop()
