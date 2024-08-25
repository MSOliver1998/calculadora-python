import tkinter as tk
from products import products_list

def create_catalogo(frame_tk):
    frame_tk.pack(side="top",fill="both",expand=True)
    frame_tk.pack_propagate(False)
    for index,product in enumerate(products_list):
        product_name_label=tk.Label(frame_tk,text=f'{product['name']}')
        product_price_label=tk.Label(frame_tk,text=f'R$: {product['price']:.2f}')
        editar_btn=tk.Button(frame_tk,text="editar",bg="orange")
        deletar_btn=tk.Button(frame_tk,text="deletar",bg="#B22222")

        product_name_label.grid(row=index+1,column=0,sticky="we")
        product_price_label.grid(row=index+1,column=1,padx=20,sticky="we")
        editar_btn.grid(row=index+1,column=2)
        deletar_btn.grid(row=index+1,column=3)

    label=tk.Label(frame_tk,text="catalogo",bg="#FFC0CB")
    label.grid(row=0,column=0)
