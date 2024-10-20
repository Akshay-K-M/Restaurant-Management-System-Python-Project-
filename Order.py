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
                    if len(i)==3: # to  find orderid of most recent order and add 1 to it for new orderid
                        self.orderid=int((i[0].split())[-1])+1    
        except FileNotFoundError:
            print("Error: 'Order.csv' file not found. Starting with order ID 1.")
        except Exception as e:
            print(f"Error reading 'Order.csv': {e}")           
        
    def confirm_order(self,customer_name): 
        try:
            with open('Order.csv', 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([f"Order ID: {self.orderid}",f"Customer Name: {customer_name}","Status = Incomplete"])
                
                for item, quantity in self.order.items():
                    writer.writerow([item,quantity])
                self.orderid+=1
                self.order.clear()
        #print("{:<15} {:<5} {:<10}".format('Food','Quantity','Price (Rs)'))  # Adjusted formatting
        except Exception as e:
            print(f"Error writing to 'Order.csv': {e}")
    def orderlist(self):
        try:
            with open('Menu.csv', 'r', newline='') as csv_file:
                reader = csv.reader(csv_file)
                menu_items = list(reader)[1:]  # Read menu items into a list, skipping the header
                amt=0.0
                listofitems=[]
                for item, quantity in self.order.items():
                    for menu_item in menu_items:
                        if item.lower() == menu_item[0].lower():  
                            price = float(menu_item[1])
                            amt += price * quantity
                            listofitems.append([item,quantity,price*quantity])
                return listofitems,amt    #print("{:<25} {:<10} {:<10}".format(item, quantity, price * quantity))
        except FileNotFoundError:
            print("Error: 'Menu.csv' file not found.")
        except Exception as e:
            print(f"Error reading 'Menu.csv': {e}")
            return [], 0.0
    

