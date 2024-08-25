import tkinter as tk
from products import products_list
from uteis import findByName

def create_vendas(frame_tk):
    products=[]
    options = [objeto["name"] for objeto in products_list]

    selected_option = tk.StringVar()
    selected_option.set(options[0]) 

    def add_product():
        product=selected_option.get()
        quantidade=int(input_quantidade.get())
        index_products_list=findByName(products_list,product)
        if len(products)==0:
            products.append({'name':product,'quantidade':quantidade})
            rows=len(products)+1
        else:
            index_products=findByName(products,product)
            print(index_products)
            if(index_products==-1):
                products.append({'name':product,'quantidade':quantidade})
                rows=len(products)+1
            else:
                products[index_products]['quantidade']+=quantidade
                quantidade=products[index_products]['quantidade']
                rows=index_products+2
        

        new_product_quantidade=tk.Label(frame_tk,text=f'{quantidade}')
        new_product_nome=tk.Label(frame_tk,text=f'{product}')
        new_product_total=tk.Label(frame_tk,text=f'R$: {(products_list[index_products_list]['price']*quantidade):.2f}')

        new_product_quantidade.grid(row=rows,column=0,sticky="we")
        new_product_nome.grid(row=rows,column=1,columnspan=2,sticky="we")
        new_product_total.grid(row=rows,column=3,sticky="we")

    def finalizar_pedido():
        print(products)

    frame_tk.pack(side="top",expand=True,fill="both")
    frame_tk.pack_propagate(False)

    label=tk.Label(frame_tk,text="vendas",bg="#D8BFD8")

    input_quantidade=tk.Entry(frame_tk,width=5)
    input_product=tk.OptionMenu(frame_tk,selected_option,*options)
    add_product_butn=tk.Button(frame_tk,text="adicionar",bg="#32CD32",command=add_product)
    finalizar_pedido_btn=tk.Button(frame_tk,text="finalizar",bg="#00FA9A",command=finalizar_pedido)

    label.grid(row=0,column=0)

    input_quantidade.grid(row=1,column=0)
    input_product.grid(row=1,column=1)
    add_product_butn.grid(row=1,column=2,padx=20)
    finalizar_pedido_btn.grid(row=1,column=3)