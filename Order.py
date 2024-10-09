import Menu
import csv
class Display_Menu:
    def __init__(self) -> None:
        obj=Menu.Menu()
        obj.display_menu()
        self.order={}
        self.ch="y"
    def add_order(self):
        count=0
        self.ch="y"
        with open('Menu.csv', 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            while self.ch.lower()=="y":
                item=input("Enter item you want to buy: ")
                for i in reader:
                    if item in i[0]:
                        count=1
                        qty=int(input("Quantity: "))
                        self.order[item]=qty
                        self.ch=input("\n\nWould you like to order?(y/n): ")
                        break 
                if count!=1:                      
                    print("Sorry! Item not available in Menu ")                        
                
        self.confirm_order()
        
    def confirm_order(self):
        with open('Order.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Item", "Quantity"])
            for item, quantity in self.order.items():
                writer.writerow([item, quantity])
        print("{:<15} {:<5} {:<10}".format('Food','Quantity','Price (Rs)'))  # Adjusted formatting
        with open('Menu.csv', 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            menu_items = list(reader)[1:]  # Read menu items into a list, skipping the header
            amt=0.0
            for item, quantity in self.order.items():
                for menu_item in menu_items:
                    if item.lower() == menu_item[0].lower():  
                        price = float(menu_item[1])
                        amt += price * quantity
                        print("{:<25} {:<10} {:<10}".format(item, quantity, price * quantity))
        
        print(f"Total Amount: {amt:.2f} Rs")
        confirm = input("Would you like to confirm the order? (y/n): ")
        if confirm.lower() == "y":
            print("Thank you for your order!")
        else:
            print("Order has been canceled.")
            self.order.clear()  # Clear the order if not confirmed
            self.add_order()  # Optionally, allow reordering

        
if __name__=="__main__":
    obj1=Display_Menu()
    obj1.add_order()
