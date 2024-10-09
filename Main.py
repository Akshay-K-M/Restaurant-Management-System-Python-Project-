import gui
import Menu
import tkinter
import Order
from tkinter import messagebox
order=Order.Display_Menu()
obj=Menu.Menu()
def customer(self):
    canvas=tkinter.Canvas(self.user)
    scrollbar=tkinter.Scrollbar(self.user,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right",fill="y")
    canvas.pack(fill="both",expand=True)
    container=tkinter.Frame(canvas)
    canvas.create_window((0,0),window=container, anchor="nw")

    inputframe=tkinter.Frame(container)
    inputframe.pack(side="right",anchor="ne",padx=20,pady=10)
    itemlabel=tkinter.Label(inputframe,text="Enter item name to order:",font=("Helvetica",40))
    itemlabel.pack()
    itementry=tkinter.Entry(inputframe,width=50)
    itementry.pack()
    qtylabel=tkinter.Label(inputframe,text="Select Quantity",font=("Helvetica",40))
    qtylabel.pack()
    qtyvar=tkinter.StringVar(inputframe)
    qtyvar.set("1")
    qtydropdown=tkinter.OptionMenu(inputframe,qtyvar,"1","2","3","4","5","6","7","8","9","10")
    qtydropdown.pack()
    labels=[]
    def displaydata():
        for label in labels:
            label.pack_forget()
        labels.clear()
        data,totalamt=order.orderlist()
        orderlabel=tkinter.Label(inputframe,text="Current Order:",font=("Helvetica",40))
        orderlabel.pack()
        orderlabel2=tkinter.Label(inputframe,text="Item    Quantity    Price",font=("Helvetica",40))
        orderlabel2.pack()
        labels.append(orderlabel)
        labels.append(orderlabel2)
        for i in data:
            print(i)
            Label=tkinter.Label(inputframe,text=f"{i[0]} {i[1]} {i[2]}" ,font=("Helvetica",40))
            Label.pack()
            labels.append(Label)
        Label2=tkinter.Label(inputframe,text=f"Total Amount = {totalamt}", font=("Helvetica",40))
        Label2.pack()
        labels.append(Label2)
    
    def addtoorder():
        item=itementry.get()
        qty=qtyvar.get()
        if item in obj.food_menu:
            qty=int(qty)
            if item not in order.order:
                order.order[item]=qty
            else:
                order.order[item]+=qty
            displaydata()
        else:
            messagebox.showerror("ERROR"," Item Does Not Exist!")

    def placeorder():
        order.confirm_order()
        for label in labels:
            label.pack_forget()
        labels.clear()
        messagebox.showinfo("Confirmed!","Your order has been placed!")
        
        

    


    addtoorderbutton=tkinter.Button(inputframe, text="Add to order",command=addtoorder)
    addtoorderbutton.pack()
    placeorderbutton=tkinter.Button(inputframe, text="Place Order",command=placeorder)
    placeorderbutton.pack()
    for i in obj.food_menu:
        Label=(tkinter.Label(container, text=f"{i} {obj.food_menu[i]}",font=("Helvetica", max(10,40-(len(obj.food_menu)//2)))))
        Label.pack()
    print(obj.food_menu)
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    container.bind("<Configure>",on_configure)
def admin(self):
    print("User is in admin")
window=gui.welcomewindow(runcustomer=customer,runadmin=admin)

