import Menu
import csv
class Display_Menu:
    def __init__(self) -> None:
        obj=Menu.Menu()
        self.order={}
        self.ch="y"
        self.orderid=1 #default value incase no orders
        try:
            with open('Order.csv', 'r', newline='') as csv_file:
                reader=csv.reader(csv_file)
                count=0
                for i in reader:
                    if len(i)==3: # to find orderid of most recent order and add 1 to it for new order id
                        self.orderid=int((i[0].split())[-1])+1    
        except FileNotFoundError:
            print("Error: 'Order.csv' file not found.")
        except Exception as e:
            print(f"Error reading 'Order.csv': {e}")           
        
    def confirm_order(self,customer_name): 
        try:
             # Opening the file in append mode to add a new order
            with open('Order.csv', 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([f"Order ID: {self.orderid}",f"Customer Name: {customer_name}","Status = Incomplete"])
                for item, quantity in self.order.items():
                    writer.writerow([item,quantity])

                 # Increment the order ID for the next order
                self.orderid+=1
                 # Clear the current order after confirming
                self.order.clear()
        except Exception as e:
             # Incase of any errors
            print(f"Error writing to 'Order.csv': {e}")
    def orderlist(self):
        try: 
            # Opening the file
            with open('Menu.csv', 'r', newline='') as csv_file:
                reader = csv.reader(csv_file)
                menu_items = list(reader)[1:]  # Read menu items into a list, skipping the header
                amt=0.0 
                listofitems=[] # List to hold ordered item details
                for item, quantity in self.order.items():
                    for menu_item in menu_items:
                        # Check for case-insensitive match between ordered item and menu item
                        if item.lower() == menu_item[0].lower():  
                            price = float(menu_item[1]) 
                            amt += price * quantity 
                            listofitems.append([item,quantity,price*quantity]) # Item quantity, total price for that item
                 # Return the list of ordered items and the total amount
                return listofitems,amt   
        except FileNotFoundError:
             # Handle case where the file does not exist
            print("Error: 'Menu.csv' file not found.")
        except Exception as e:
            # Handle any other error
            print(f"Error reading 'Menu.csv': {e}")
           
    

