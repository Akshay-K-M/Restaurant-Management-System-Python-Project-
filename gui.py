import tkinter 
from tkinter import font, messagebox,simpledialog
from PIL import Image, ImageTk
import gui
import Menu
import Order
import csv

order=Order.Display_Menu()
obj=Menu.Menu()


    
class WelcomeWindow():
    def __init__(self, runcustomer=None, runadmin=None):
        self.runcustomer = runcustomer
        self.runadmin = runadmin
        self.welcome = tkinter.Tk()
        self.welcome.title("Restaurant Management System (RMS)")
        self.welcome.geometry("1280x720")

        # Load and resize the background image
        self.background_image = Image.open("menu_bg.jpg")  # Update with your image path
        self.background_image = self.background_image.resize((1280, 720))  # Resize to fit the window
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = tkinter.Canvas(self.welcome, width=1280, height=720)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        self.label = tkinter.Label(self.welcome, text="Welcome To Flavourful!", font=("Brush Script Mt", 60), bg="#B22222", fg="black")
        self.canvas.create_window(640, 250, window=self.label)  

        self.customerbutton = tkinter.Button(self.welcome, text="Place Order", font=("Arial Black", 30), bg="#FF7D40", fg="black", command=self.gotocustomer)
        self.canvas.create_window(600, 400, window=self.customerbutton)  

        self.adminbutton = tkinter.Button(self.welcome, text="Manage Menu", font=("Arial Black", 30),  bg="#FF7D40", fg="black", command=self.gotoadmin)
        self.canvas.create_window(600, 500, window=self.adminbutton)  # Centered in the canvas

        self.welcome.mainloop()

    
    
    def gotocustomer(self):
        self.welcome.destroy()
        self.user=tkinter.Tk()
        self.user.title("Customer")
        self.user.geometry("1280x720")
        
        
        #self.canvas = tkinter.Canvas(self.user, bg="#282828")
        #self.canvas.pack(fill="both", expand=True)

        self.gobackbutton=tkinter.Button(self.user,text="Go Back",font=("Cooper Black", 40),command=self.goback1, fg="#941b1b", bg="#282828")
        self.gobackbutton.pack(side="top", anchor="nw", padx=25,pady=25)
        #self.canvas.create_window(20, 20, anchor="nw", window=self.gobackbutton)
        if self.runcustomer:
            self.runcustomer(self)
        self.user.mainloop()
        
    
        
    def gotoadmin(self):
        self.welcome.destroy()
        self.admin=tkinter.Tk()
        self.admin.title("Admin")
        self.admin.geometry("1280x720")
        self.admin.configure(bg="#6e1414")
        self.gobackbutton=tkinter.Button(self.admin,text="Go Back",font=("Arial Black", 40), fg="#941b1b", bg="#282828",command=self.goback2)
        self.gobackbutton.pack(side="top", anchor="nw", padx=25,pady=25)
        if self.runadmin:
            self.runadmin(self)
        self.admin.mainloop()

    def goback1(self): # go back from customer
        self.user.destroy()
        WelcomeWindow(self.runcustomer,self.runadmin)
    
    def goback2(self): #go back from admin
        self.admin.destroy()
        WelcomeWindow(self.runcustomer,self.runadmin)


def customer(self):
    canvas=tkinter.Canvas(self.user)
    scrollbar=tkinter.Scrollbar(self.user,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right",fill="y")
    canvas.pack(fill="both",expand=True)
    container=tkinter.Frame(canvas)
    canvas.create_window((0,0),window=container, anchor="nw")

    inputframe=tkinter.Frame(container)
    inputframe.pack(side="right",anchor="ne",padx=10,pady=100)
    itemlabel=tkinter.Label(inputframe,text="Enter item name to order:",font=("Arial Black",30), bg = "#8B2252")
    itemlabel.pack()
    itementry=tkinter.Entry(inputframe,width=50)
    itementry.pack()
    qtylabel=tkinter.Label(inputframe,text="Select Quantity",font=("Arial Black",30))
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
        orderlabel=tkinter.Label(inputframe,text="Current Order:",font=("Arial Black",20))
        orderlabel.pack()
        orderlabel2=tkinter.Label(inputframe,text="Item    Quantity    Price",font=("Arial Black",20))
        orderlabel2.pack()
        labels.append(orderlabel)
        labels.append(orderlabel2)
        for i in data:
            Label=tkinter.Label(inputframe,text=f"{i[0]} {i[1]} {i[2]}" ,font=("Arial Black",20))
            Label.pack()
            labels.append(Label)
        Label2=tkinter.Label(inputframe,text=f"Total Amount = {totalamt}", font=("Arial Black",20))
        Label2.pack()
        labels.append(Label2)
    
    def addtoorder():
        item=itementry.get()
        qty=qtyvar.get()
        if item in obj.food_menu and item != "Item":
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
            messagebox.showerror("ERROR"," Invalid Item!")

    def placeorder():
        if len(order.order)!=0:
            customer_name=simpledialog.askstring("Input", "Enter your name", parent=self.user)


            if (customer_name != None) and len(customer_name) == 0:
                messagebox.showerror("ERROR","Please enter your name")
                placeorder()
            if (customer_name != None) and len(customer_name) != 0:
                order.confirm_order(customer_name)
            if customer_name != None:
                for label in labels:
                    label.pack_forget()
                labels.clear()
            if (customer_name !=None) and len(customer_name) !=0:
                messagebox.showinfo("Confirmed!","Your order has been placed! Please collect it from the counter!")
        else:
            messagebox.showerror("Error!","Kindly add to cart!")
    
    addtoorderbutton=tkinter.Button(inputframe, text="Add to order",command=addtoorder)
    addtoorderbutton.pack()
    placeorderbutton=tkinter.Button(inputframe, text="Place order",command=placeorder)
    placeorderbutton.pack()
    for i in obj.food_menu:
        Label=(tkinter.Label(container, text=f"{i} {obj.food_menu[i]}",font=("Arial Black", max(10,40-(len(obj.food_menu)//2)))))
        Label.pack()
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    container.bind("<Configure>",on_configure)
# ADMINNN
def admin(self):
    orderno=tkinter.StringVar(self.admin)
    orderno.set("Choose Order No")
    ordernos=[]
    labels2=[]
    def change_menu(source="admin"):
        self.change=tkinter.Tk()
        self.change.title("Edit Menu")
        self.change.geometry("1280x720")
        self.change.config(bg="#282828")
        self.gobackbutton=tkinter.Button(self.change,text="Go Back",font=("Arial Black", 40),fg="#941b1b", bg="#282828", command=goback3)
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
            Label=(tkinter.Label(container, text=f"{i} {obj.food_menu[i]}",font=("Arial Black", max(10,40-(len(obj.food_menu)//2)))))
            Label.pack()
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        container.bind("<Configure>",on_configure)
        def add():
        # Pop-up to get the item name
            item_name = simpledialog.askstring("Input", "Enter the item name:", parent=self.change)
            if item_name == "Item":
                messagebox.showerror("ERROR","Invalid Input")
            if item_name and item_name not in obj.food_menu and not(item_name.isnumeric()) and item_name != "Item":
                # Pop-up to get the item price
                item_price = simpledialog.askstring("Input", "Enter the item price:", parent=self.change)
                try:
                    if int(item_price) > 0:
                    
                    # Saving the data onto csv file
                        with open('Menu.csv', 'a', newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow([item_name, item_price])
                            obj.food_menu[item_name]=item_price
                            self.change.destroy()
                            f.flush()
                            change_menu(source="change_menu") 
                    elif int(item_price) <=0:
                        messagebox.showerror("ERROR", "Invalid Price")   

                            
                except:
                        messagebox.showerror("ERROR", "Invalid Price")      
            else:
                if item_name == "":
                    messagebox.showerror("ERROR","Enter item name!")  
                elif item_name in obj.food_menu:
                    messagebox.showerror("ERROR","Item already exists on the menu!")
                elif item_name.isnumeric():
                    messagebox.showerror("ERROR","Enter valid item name!")  
                if item_name != None: #makes sure user didnt cancel, only then calls add
                    add() 
         # Function to remove an item (by Name)
        def remove():
            # Pop-up to get the name of the item to remove
            item_name = simpledialog.askstring("Input", "Enter the name of the item to remove:", parent=self.change)
            if item_name == "Item":
                messagebox.showerror("ERROR","Invalid Input")
            if item_name and item_name != "Item":
                # Read the current items from the CSV
                updated_items = []
                item_found = False
                with open('Menu.csv', 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    for row in reader:
                        print(row[0] + item_name)
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
     
        addbutton=tkinter.Button(self.change, text="Add item to Menu",font=("Arial Black", 40),command=add)
        addbutton.pack()
        removebutton=tkinter.Button(self.change, text="Remove item from Menu",font=("Arial Black", 40),command=remove)
        removebutton.pack()
        self.change.mainloop()
    self.changemenubutton=tkinter.Button(self.admin,text="Edit Menu",font=("Arial Black", 40),command=change_menu)
    self.changemenubutton.pack( anchor="ne", padx=25,pady=25)
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
        def mark_order_as_complete():
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
            messagebox.showinfo("Success!","Order has been marked as complete!")
          


        for label in labels2:
            label.pack_forget()
        labels2.clear()
        dropdowndisplay()

        orderid=orderno.get()
        found=False
        with open('Order.csv', 'r', newline='') as csv_file:
            reader=csv.reader(csv_file)
            for i in reader:
                if found==True:
                    if len(i)!=3: # adds items to list until order is complete
                        Label=tkinter.Label(self.admin,text=f"{i[0]} {i[1]}",font=("Arial Black",25))
                        Label.pack()
                        labels2.append(Label)
                    else: # breaks upon reaching next header
                        break
                if len(i)==3:
                    if (i[0].split())[-1]==orderid:
                        found=True
                        status=i[-1]
                        Label=tkinter.Label(self.admin,text=f"{i[0]}  {i[1]}  {i[2]}" ,font=("Arial Black",25))
                        Label.pack()
                        Label2=tkinter.Label(self.admin,text="Item, Quantity",font=("Arial Black",25))
                        Label2.pack()
                        labels2.append(Label2)
                        labels2.append(Label)
            if orderid!="Choose Order No" and orderid!="No Current Orders" and status !="Status = Complete":
                deletebutton=tkinter.Button(self.admin,text="Mark as complete",command=mark_order_as_complete)
                deletebutton.pack()
                labels2.append(deletebutton)
                            
    orderno.trace("w", on_orderno_change)
#Admin
    def goback3(): #go back from admin
        self.change.destroy()
        self.admin=tkinter.Tk()
        self.admin.title("Admin")
        self.admin.geometry("1280x720")
        self.admin.configure(bg="#6e1414")
        self.gobackbutton=tkinter.Button(self.admin,text="Go Back",font=("Arial Black", 40), fg="#941b1b", bg="#282828",command=self.goback2)
        self.gobackbutton.pack( anchor="nw", padx=25,pady=25)
        if self.runadmin:
            self.runadmin(self)
        self.admin.mainloop()

        
    

        

