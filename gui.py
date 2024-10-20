import tkinter 
from tkinter import font, messagebox,simpledialog
from PIL import Image, ImageTk
import gui
import Menu
import Order
import csv

#Initialize order and menu objects
order=Order.Display_Menu()
obj=Menu.Menu()


    
class WelcomeWindow():
    def __init__(self, runcustomer=None, runadmin=None):
        # Initialize customer and admin run functions
        self.runcustomer = runcustomer
        self.runadmin = runadmin
        # Set up the main welcome window
        self.welcome = tkinter.Tk()
        self.welcome.title("Restaurant Management System (RMS)")
        self.welcome.geometry("1280x720")

        # Load and resize the background image
        self.background_image = Image.open("menu_bg.jpg")  # Update with your image path
        self.background_image = self.background_image.resize((1280, 720))  # Resize to fit the window
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a canvas for the welcome window
        self.canvas = tkinter.Canvas(self.welcome, width=1280, height=720)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")


        # Welcome message
        self.label = tkinter.Label(self.welcome, text="Welcome To Flavourful!", font=("Brush Script Mt", 60), bg="#B22222", fg="black")
        self.canvas.create_window(640, 250, window=self.label)  

        # Button to place order
        self.customerbutton = tkinter.Button(self.welcome, text="Place Order", font=("Arial Black", 30), bg="#FF7D40", fg="black", command=self.gotocustomer)
        self.canvas.create_window(600, 400, window=self.customerbutton)  

        # Button to manage menu
        self.adminbutton = tkinter.Button(self.welcome, text="Manage Menu", font=("Arial Black", 30),  bg="#FF7D40", fg="black", command=self.gotoadmin)
        self.canvas.create_window(600, 500, window=self.adminbutton)  # Centered in the canvas

        # Start the Tkinter main loop   
        self.welcome.mainloop()

    
    
    def gotocustomer(self):
        self.welcome.destroy()
        self.user=tkinter.Tk()
        self.user.title("Customer")
        self.user.geometry("1280x720")
        
        
        #self.canvas = tkinter.Canvas(self.user, bg="#282828")
        #self.canvas.pack(fill="both", expand=True)

        # Go back button for the customer interface
        self.gobackbutton=tkinter.Button(self.user,text="Go Back",font=("Cooper Black", 25),command=self.goback1, fg="#941b1b", bg="#282828")
        self.gobackbutton.pack(side="top", anchor="nw", padx=25,pady=25)
        #self.canvas.create_window(20, 20, anchor="nw", window=self.gobackbutton)
        # Call the customer function if provided
        if self.runcustomer:
            self.runcustomer(self)
        # Start the customer interface main loop
        self.user.mainloop()
        
    
        
    def gotoadmin(self):

        # Switch to the admin
        self.welcome.destroy()
        self.admin=tkinter.Tk()
        self.admin.title("Admin")
        self.admin.geometry("1280x720")
        self.admin.configure(bg="#6e1414")
        # Go back button for the admin interface
        self.gobackbutton=tkinter.Button(self.admin,text="Go Back",font=("Arial Black", 25), fg="#941b1b", bg="#282828",command=self.goback2)
        self.gobackbutton.pack(side="top", anchor="nw", padx=25,pady=25)
        # Call the admin function if provided
        if self.runadmin:
            self.runadmin(self)
        self.admin.mainloop()

    def goback1(self): # go back from customer
        order.order={}
        self.user.destroy()
        WelcomeWindow(self.runcustomer,self.runadmin) 
    
    def goback2(self): #go back from admin
        self.admin.destroy()
        WelcomeWindow(self.runcustomer,self.runadmin) # Return to the welcome window


def customer(self):
    # Create a scrollable frame for customer order input
    canvas=tkinter.Canvas(self.user)
    scrollbar=tkinter.Scrollbar(self.user,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right",fill="y")
    canvas.pack(fill="both",expand=True)
    container=tkinter.Frame(canvas)
    canvas.create_window((0,0),window=container, anchor="nw")

    # Frame for input fields
    inputframe=tkinter.Frame(container)
    inputframe.pack(side="right",anchor="ne",padx=100,pady=5)
    # Input for item name
    itemlabel=tkinter.Label(inputframe,text="Enter item name to order:",font=("Arial Black",30), bg = "#8B2252")
    itemlabel.pack()
    itementry=tkinter.Entry(inputframe,width=50)
    itementry.pack()
    # Dropdown for quantity
    qtylabel=tkinter.Label(inputframe,text="Select Quantity",font=("Arial Black",30))
    qtylabel.pack()
    qtyvar=tkinter.StringVar(inputframe)
    qtyvar.set("1")
    qtydropdown=tkinter.OptionMenu(inputframe,qtyvar,"-1","1","2","3","4","5","6","7","8","9","10")
    qtydropdown.pack()
    labels=[] # List to hold labels
    def displaydata():
        # Clear previous labels displaying updated order
        for label in labels:
            label.pack_forget()
        labels.clear()
        # Retrieve and display current order details
        data,totalamt=order.orderlist()
        orderlabel=tkinter.Label(inputframe,text="Current Order:",font=("Courier New",20))
        orderlabel.pack()
        orderlabel2=tkinter.Label(inputframe, text="{:<15} {:<8} {:<5}".format("  Item", "Quantity", "Price"), font=("Courier New", 20))
        orderlabel2.pack()
        labels.append(orderlabel)
        labels.append(orderlabel2)
        # Loop through the order date to create labels
        for item_name, quantity, price in data:
            bill = tkinter.Label(inputframe, text="{:<15} {:<8} {:<6.2f}".format(item_name, quantity, price), font=("Courier New", 18))
            bill.pack()
            labels.append(bill)
        # Display the total amount
        total_amt = tkinter.Label(inputframe, text="Total Amount = {:.2f}".format(totalamt), font=("Courier New", 20))
        total_amt.pack()
        labels.append(total_amt)
    
    def addtoorder():
        # Add an item to the current order
        item=itementry.get().strip() #Get item name from entry
        qty=qtyvar.get()
        if item in obj.food_menu and item != "Item": # Check if the item is valid
            qty=int(qty)
            if item not in order.order and qty>=1: # New item 
                order.order[item]=qty
                displaydata()
            elif item in order.order and (order.order[item]+qty)==0 : # Remove item if quantity is Zero
                order.order.pop(item)  
                if order.order=={}: #Clear labels if no items left
                    for label in labels:
                        label.pack_forget()
                    labels.clear()
                else:
                    displaydata() # Refresh display
            elif len(order.order)!=0 and item in order.order and (order.order[item]+qty)>=0:
                order.order[item]+=qty # Update Quantity
                displaydata()
            else:
                messagebox.showerror("ERROR","Invalid Quantity") # Error for invalid quantity
            
        else:
            messagebox.showerror("ERROR"," Invalid Item!") # Error for invalid item

    def placeorder():
        # Place the order and confirm with customer
        if len(order.order)!=0:
            customer_name=simpledialog.askstring("Input", "Enter your name", parent=self.user)


            if (customer_name != None) and len(customer_name) == 0:
                messagebox.showerror("ERROR","Please enter your name")
                placeorder() # Retry if name is empty   
            if (customer_name != None) and len(customer_name) != 0: # Confirm the order 
                order.confirm_order(customer_name)
            if customer_name != None:
                for label in labels: # Clear labels after order is placed
                    label.pack_forget()
                labels.clear()
            if (customer_name !=None) and len(customer_name) !=0:
                messagebox.showinfo("Confirmed!","Your order has been placed! Please collect it from the counter!")
            if (customer_name == None):
                order.order={}
                for label in labels: # Clear labels after order is placed
                    label.pack_forget()
                labels.clear()
        else:
            messagebox.showerror("Error!","Kindly add to cart!") # Error if no items in order
    
    #  Buttons for adding order and placing order
    addtoorderbutton=tkinter.Button(inputframe, text="Add to order",command=addtoorder)
    addtoorderbutton.pack()
    placeorderbutton=tkinter.Button(inputframe, text="Place order",command=placeorder)
    placeorderbutton.pack()
    # Create header labels
    # Define column widths
    item_width = 20  # Width for item names
    price_width = 10  # Width for prices

    # Create header labels
    header_label = tkinter.Label(container, text="{:<{}} {:<{}}".format(" Item Name", item_width,"Price", price_width), font=("Courier New", 20))
    header_label.pack()

    # Loop through the food menu and create labels
    for item_name, item_price in obj.food_menu.items():
        try:
            item_price = float(item_price)  # Ensure item_price is a float
            formatted_label = tkinter.Label(container, text="{:<{}}  {:<{}}".format(item_name, item_width, f"{item_price:.2f}", price_width), font=("Courier New", 18))
            formatted_label.pack()
        except ValueError:
            pass
       
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    container.bind("<Configure>",on_configure)


# ADMIN

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
        self.gobackbutton=tkinter.Button(self.change,text="Go Back",font=("Arial Black", 25),fg="#941b1b", bg="#282828", command=goback3)
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
        row = 0  # Start at the first row for the header

        # Create header labels
        header_item = tkinter.Label(container, text="Item Name", font=("Arial Black", 15))
        header_item.grid(row=row, column=0, padx=10, pady=10)

        header_price = tkinter.Label(container, text="Price", font=("Arial Black", 15))
        header_price.grid(row=row, column=1, padx=10, pady=10)

        # Increment row for the item list
        row += 1

        # Fill the table with items
        for item_name, item_price in obj.food_menu.items():
            if item_name!="Item" and item_price!="Price(Rs)":
                item_label = tkinter.Label(container, text=item_name, font=("Arial Black", 12))
                item_label.grid(row=row, column=0, padx=10, pady=5)

                price_label = tkinter.Label(container, text=item_price, font=("Arial Black", 12))
                price_label.grid(row=row, column=1, padx=10, pady=5)

            row += 1  # Move to the next row for the next
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
                elif type(item_name)== str and item_name.isnumeric():
                    messagebox.showerror("ERROR","Enter valid item name!")  
                if item_name != None: #makes sure user didnt cancel, only then calls add
                    add() 
         # Function to remove an item
        def remove():
            try:
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
            except FileNotFoundError:
                print("Error: 'Order.csv' file not found.")
            except Exception as e:
                 print(f"Error reading 'Order.csv': {e}")         
     
        addbutton=tkinter.Button(self.change, text="Add item to Menu",font=("Arial Black", 25),command=add,bg="orange")
        addbutton.pack()
        removebutton=tkinter.Button(self.change, text="Remove item from Menu",font=("Arial Black", 25),command=remove,bg="orange")
        removebutton.pack()
        self.change.mainloop()
    self.changemenubutton=tkinter.Button(self.admin,text="Edit Menu",font=("Arial Black", 25),command=change_menu)
    self.changemenubutton.pack(anchor="ne", padx=25,pady=25)
    def dropdowndisplay():
        try:
            ordernos.clear()
            with open('Order.csv', 'r', newline='') as csv_file:
                reader=csv.reader(csv_file)
                for i in reader:
                    if len(i)==3:
                        ordernos.append((i[0].split())[-1]) # taking order id string i[0], and splitting so last part becomes orderid (-1)
            if len(ordernos)!=0:
                orderdropdown=tkinter.OptionMenu(self.admin,orderno,*ordernos) # * unpacks the list, if 4 order it would just show one option 1 2 3 4 otherwise.
                orderdropdown.config(width=20,font=("Arial", 15))
                orderdropdown.pack()
                labels2.append(orderdropdown)
            if len(ordernos)==0:
                orderdropdown=tkinter.OptionMenu(self.admin,orderno,"No Current Orders") 
                orderdropdown.config(width=20,font=("Arial", 15))
                order.orderid=1
                orderdropdown.pack()
                labels2.append(orderdropdown)
        except FileNotFoundError:
            print("Error: 'Order.csv' file not found.")
        except Exception as e:
            print(f"Error reading 'Order.csv': {e}")
    dropdowndisplay()
 

    def on_orderno_change(*args):
        def mark_order_as_complete(): # Fucntion to mark status of order as complete
            try:
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
            except FileNotFoundError:
                print("Error: 'Order.csv' file not found.")
            except Exception as e:
                print(f"Error reading 'Order.csv': {e}")


        for label in labels2:
            label.pack_forget()
        labels2.clear()
        dropdowndisplay()

        orderid=orderno.get()
        found=False
        try:
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
        except FileNotFoundError:
            print("Error: 'Order.csv' file not found.")
        except Exception as e:
            print(f"Error reading 'Order.csv': {e}")                    
    orderno.trace("w", on_orderno_change)
#Admin
    def goback3(): #go back from admin
        self.change.destroy()
        self.admin=tkinter.Tk()
        self.admin.title("Admin")
        self.admin.geometry("1280x720")
        self.admin.configure(bg="#6e1414")
        self.gobackbutton=tkinter.Button(self.admin,text="Go Back",font=("Arial Black", 25), fg="#941b1b", bg="#282828",command=self.goback2)
        self.gobackbutton.pack( anchor="nw", padx=25,pady=25)
        if self.runadmin:
            self.runadmin(self)
        self.admin.mainloop()

        
    

        

