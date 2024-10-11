import gui
import Menu
import tkinter
import Order
import csv
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
    qtydropdown=tkinter.OptionMenu(inputframe,qtyvar,"-1","1","2","3","4","5","6","7","8","9","10")
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
            if item not in order.order and qty>=1:
                order.order[item]=qty
                displaydata()
            elif item in order.order and (order.order[item]+qty)==0 :
                order.order.pop(item)  
                if order.order=={}:
                    for label in labels:
                        label.pack_forget()
                    labels.clear()
                else:
                    displaydata()
            elif len(order.order)!=0 and item in order.order and (order.order[item]+qty)>=0:
                order.order[item]+=qty
                displaydata()
            else:
                messagebox.showerror("ERROR","Invalid Quantity")
            
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


# ADMINNN
def admin(self):
    orderno=tkinter.StringVar(self.admin)
    orderno.set("Choose Order No")
    ordernos=[]
    labels2=[]
    def dropdowndisplay():
        ordernos.clear()
        with open('Order.csv', 'r', newline='') as csv_file:
            reader=csv.reader(csv_file)
            for i in reader:
                if len(i)==3:
                    ordernos.append((i[0].split())[-1]) # taking orderid string i[0], and splitting so last part becomes orderid (-1)
        if len(ordernos)!=0:
            orderdropdown=tkinter.OptionMenu(self.admin,orderno,*ordernos) # * unpacks the list, if 4 order it would just show one option 1 2 3 4 otherwise.
            orderdropdown.pack()
            labels2.append(orderdropdown)
        if len(ordernos)==0:
            orderdropdown=tkinter.OptionMenu(self.admin,orderno,"No Current Orders") # * unpacks the list, if 4 order it would just show one option 1 2 3 4 otherwise.
            order.orderid=1
            orderdropdown.pack()
            labels2.append(orderdropdown)
    dropdowndisplay()
 

    def on_orderno_change(*args):
        def deleteorder():
            orderidtodelete=orderno.get()
            deletebutton.pack_forget()
            data=[]
            found=False
            with open('Order.csv', 'r', newline='') as csv_file:
                reader=csv.reader(csv_file)
                for i in reader:
                    if len(i)==3:
                        if orderidtodelete!=(i[0].split())[-1]:
                            data.append(i)
                            found=False
                        else:
                            found=True
                    if len(i)!=3 and found==False:
                        data.append(i)
            with open('Order.csv','w',newline='') as csv_file:
                writer=csv.writer(csv_file)
                for i in data:
                    writer.writerow(i)
            orderno.set("Choose Order No")
          


        for label in labels2:
            label.pack_forget()
        labels2.clear()
        dropdowndisplay()

        orderid=orderno.get()
        l=[]
        found=False
        with open('Order.csv', 'r', newline='') as csv_file:
            reader=csv.reader(csv_file)
            for i in reader:
                if found==True:
                    if len(i)!=3: # adds items to list until order is complete
                        l.append(i)
                        Label=tkinter.Label(self.admin,text=f"{i}",font=("Helvetica",40))
                        Label.pack()
                        labels2.append(Label)
                    else: # breaks upon reaching next header
                        break
                if len(i)==3:
                    if (i[0].split())[-1]==orderid:
                        found=True
                        l.append(i)
                        Label=tkinter.Label(self.admin,text=f"{i}",font=("Helvetica",40))
                        Label.pack()
                        labels2.append(Label)
            if orderid!="Choose Order No" and orderid!="No Current Orders":
                deletebutton=tkinter.Button(self.admin,text="Delete this order",command=deleteorder)
                deletebutton.pack()
                labels2.append(deletebutton)
                            
        
    orderno.trace("w", on_orderno_change)
    




window=gui.welcomewindow(runcustomer=customer,runadmin=admin)

