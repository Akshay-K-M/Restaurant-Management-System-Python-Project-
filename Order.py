import Menu
import csv
class Display_Menu:
    def __init__(self) -> None:
        obj=Menu.Menu()
        self.order={}
        self.ch="y"
        self.orderid=1 #default value incase no orders
        with open('Order.csv', 'r', newline='') as csv_file:
            reader=csv.reader(csv_file)
            count=0
            for i in reader:
                if len(i)==3: # to  find orderid of most recent order and add 1 to it for new orderid
                    self.orderid=int((i[0].split())[-1])+1               
        
    def confirm_order(self,customer_name): 
        with open('Order.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([f"Order ID: {self.orderid}",f"Customer Name: {customer_name}","Status = Incomplete"])
            
            for item, quantity in self.order.items():
                writer.writerow([item,quantity])
            self.orderid+=1
            self.order.clear()
        #print("{:<15} {:<5} {:<10}".format('Food','Quantity','Price (Rs)'))  # Adjusted formatting
    def orderlist(self):
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
      
    

