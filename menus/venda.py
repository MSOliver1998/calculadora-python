import tkinter as tk

def create_vendas(frame_tk):
    products=[]
    def add_product():
        product=input_product.get()
        quantidade=input_quantidade.get()
        products.append({f'{product}':quantidade})
        rows=len(products)+1
        new_product_quantidade=tk.Label(frame_tk,text=f'{quantidade}')
        new_product_nome=tk.Label(frame_tk,text=f'{product}')
        new_product_quantidade.grid(row=rows,column=0,sticky="we")
        new_product_nome.grid(row=rows,column=1,columnspan=2,sticky="we")

    def finalizar_pedido():
        print(products)

    frame_tk.pack(side="top",expand=True,fill="both")
    frame_tk.pack_propagate(False)

    label=tk.Label(frame_tk,text="vendas",bg="#D8BFD8")

    input_quantidade=tk.Entry(frame_tk,width=5)
    input_product=tk.Entry(frame_tk)
    add_product_butn=tk.Button(frame_tk,text="adicionar",bg="#32CD32",command=add_product)
    finalizar_pedido_btn=tk.Button(frame_tk,text="finalizar",bg="#00FA9A",command=finalizar_pedido)

    label.grid(row=0,column=0)

    input_quantidade.grid(row=1,column=0)
    input_product.grid(row=1,column=1)
    add_product_butn.grid(row=1,column=2,padx=20)
    finalizar_pedido_btn.grid(row=1,column=3)