import tkinter 
from tkinter import font
import gui
import Menu
import tkinter
import Order
import csv
from tkinter import messagebox,simpledialog
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
        if len(order.order)!=0:
            customer_name=simpledialog.askstring("Input", "Enter your name", parent=self.user)
            order.confirm_order(customer_name)
            for label in labels:
                label.pack_forget()
            labels.clear()
            messagebox.showinfo("Confirmed!","Your order has been placed!")
        else:
            messagebox.showerror("Error!","Kindly add to cart!")
    
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
            with open('Order.csv', 'r', newline='') as csv_file:
                reader=csv.reader(csv_file)
                for i in reader:
                    if len(i)==3:
                        if orderidtodelete!=(i[0].split())[-1]:
                            data.append(i)
                        else:
                            data.append(i[0:2]+["Status = Complete"])
                    if len(i)!=3:
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
                        Label=tkinter.Label(self.admin,text=f"{i}",font=("Helvetica",25))
                        Label.pack()
                        labels2.append(Label)
                    else: # breaks upon reaching next header
                        break
                if len(i)==3:
                    if (i[0].split())[-1]==orderid:
                        status=i[-1]
                        found=True
                        l.append(i)
                        Label=tkinter.Label(self.admin,text=f"{i}",font=("Helvetica",25))
                        Label.pack()
                        Label2=tkinter.Label(self.admin,text="Item, Quantity",font=("Helvetica",25))
                        Label2.pack()
                        labels2.append(Label2)
                        labels2.append(Label)
            
            if orderid!="Choose Order No" and orderid!="No Current Orders" and status !="Status = Complete":
                deletebutton=tkinter.Button(self.admin,text="Mark as complete",command=deleteorder)
                deletebutton.pack()
                labels2.append(deletebutton)                        
    orderno.trace("w", on_orderno_change)

#Admin
    def goback3(): #go back from admin
        self.change.destroy()
        self.admin=tkinter.Tk()
        self.admin.title("Admin")
        self.admin.geometry("1280x720")
        self.gobackbutton=tkinter.Button(self.admin,text="Go Back",font=("Helvetica", 40),command=self.goback2)
        self.gobackbutton.pack(side="top", anchor="nw", padx=25,pady=25)
        if self.runadmin:
            self.runadmin(self)
        self.admin.mainloop()

    def change_menu(source="admin"):
        self.change=tkinter.Tk()
        self.change.title("Edit Menu")
        self.change.geometry("1280x720")
        self.gobackbutton=tkinter.Button(self.change,text="Go Back",font=("Helvetica", 40),command=goback3)
        self.gobackbutton.pack(side="top", anchor="nw", padx=25,pady=25)
        canvas=tkinter.Canvas(self.change)
        scrollbar=tkinter.Scrollbar(self.change,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right",fill="y")
        canvas.pack(fill="both",expand=True)
        container=tkinter.Frame(canvas)
        canvas.create_window((0,0),window=container, anchor="nw")  
        if source=="admin":
            self.admin.destroy()
        for i in obj.food_menu:
            Label=(tkinter.Label(container, text=f"{i} {obj.food_menu[i]}",font=("Helvetica", max(10,40-(len(obj.food_menu)//2)))))
            Label.pack()
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        container.bind("<Configure>",on_configure)
        def add():
        # Pop-up to get the item name
            item_name = simpledialog.askstring("Input", "Enter the item name:", parent=self.change)
            if item_name:
                # Pop-up to get the item price
                item_price = simpledialog.askstring("Input", "Enter the item price:", parent=self.change)
                if item_price:
                    # Add the item as a label in the container
                    label = tkinter.Label(container, text=f"{item_name} {item_price}", font=("Helvetica", max(10,40-(len(obj.food_menu)//2))))
                    label.pack()
                    # Optionally save this data in a list or a file (CSV)
                    with open('Menu.csv', 'a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow([item_name, item_price])
                        obj.food_menu[item_name]=item_price




         # Function to remove an item (by Name)
        def remove():
            # Pop-up to get the name of the item to remove
            item_name = simpledialog.askstring("Input", "Enter the name of the item to remove:", parent=self.change)
            if item_name:
                # Read the current items from the CSV
                updated_items = []
                item_found = False
                with open('Menu.csv', 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    for row in reader:
                        if row[0] != item_name:
                            updated_items.append(row)
                        else:
                            item_found = True
                            obj.food_menu.pop(item_name)                    

                # Write back the updated items to the CSV
                with open('Menu.csv', 'w', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerows(updated_items)
                    
                # Notify the user if the item was removed or not found
                if item_found:
                    messagebox.showinfo("Success", f"{item_name} has been removed from the menu.")
                    self.change.destroy()
                    change_menu(source="change_menu") 
                else:
                    messagebox.showwarning("Not Found", f"{item_name} was not found in the menu.")            
     
        addbutton=tkinter.Button(self.change, text="Add items to Menu",font=("Helvetica", 40),command=add)
        addbutton.pack()
        removebutton=tkinter.Button(self.change, text="Remove items from Menu",font=("Helvetica", 40),command=remove)
        removebutton.pack()
        self.change.mainloop()
    self.changemenubutton=tkinter.Button(self.admin,text="Edit Menu",font=("Helvetica", 40),command=change_menu)
    self.changemenubutton.pack(side="top", anchor="ne", padx=25,pady=25)
    

        

    
class welcomewindow():
    def __init__(self,runcustomer=None,runadmin=None):
        self.runcustomer=runcustomer
        self.runadmin=runadmin
        self.welcome=tkinter.Tk()
        self.welcome.title("Restaurant Management System (RMS)")
        self.welcome.geometry("1280x720")

    
        self.label = tkinter.Label(self.welcome, text="Welcome To Flavourful!",font=("Helvetica", 80))
        self.label.pack(fill="both",pady=40)

        self.customerbutton=tkinter.Button(self.welcome,text="Place Order",font=("Helvetica", 80),command=self.gotocustomer)
        self.customerbutton.pack(pady=100)

        self.adminbutton=tkinter.Button(self.welcome,text="Manage Menu",font=("Helvetica", 80),command=self.gotoadmin)
        self.adminbutton.pack(pady=5)
        self.welcome.mainloop()
    
    
    def gotocustomer(self):
        self.welcome.destroy()
        self.user=tkinter.Tk()
        self.user.title("Customer")
        self.user.geometry("1280x720")
        
        self.gobackbutton=tkinter.Button(self.user,text="Go Back",font=("Helvetica", 40),command=self.goback1)
        self.gobackbutton.pack(side="top", anchor="nw", padx=25,pady=25)
        if self.runcustomer:
            self.runcustomer(self)
        self.user.mainloop()
        
    
        
    def gotoadmin(self):
        self.welcome.destroy()
        self.admin=tkinter.Tk()
        self.admin.title("Admin")
        self.admin.geometry("1280x720")
        self.gobackbutton=tkinter.Button(self.admin,text="Go Back",font=("Helvetica", 40),command=self.goback2)
        self.gobackbutton.pack(side="top", anchor="nw", padx=25,pady=25)
        if self.runadmin:
            self.runadmin(self)
        self.admin.mainloop()

    def goback1(self): # go back from customer
        self.user.destroy()
        welcomewindow(self.runcustomer,self.runadmin)
    
    def goback2(self): #go back from admin
        self.admin.destroy()
        welcomewindow(self.runcustomer,self.runadmin)


if __name__=="__main__":
    def customer():
        print("User is in customer")

    def admin():
        print("User is in admin")
    window=welcomewindow(runcustomer=customer,runadmin=admin)