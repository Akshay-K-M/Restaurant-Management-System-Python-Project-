import csv
class Menu:
    def __init__(self) -> None:
        self.food_menu={}
        with open('Menu.csv','r') as csv_file:
            reader=csv.reader(csv_file)
            for i in reader:
                self.food_menu[i[0]]=i[1]
        # Writing the initial menu to CSV
        with open('Menu.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            # Writing the header

            # Writing the menu items
            for item, price in self.food_menu.items():
                writer.writerow([item, price])

    def csv_write(self):
        # Writing the updated menu to CSV
        with open('Menu.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Item", "Price"])
            for item, price in self.food_menu.items():
                writer.writerow([item, price])

    def display_menu(self):
        print("{:<25} {:<10}".format('Food', 'Price (Rs)'))  # Adjusted formatting
        for label, price in self.food_menu.items():
            print("{:<25} {:<10}".format(label, price))

    def add_update_menu(self, food, price):
        self.food_menu[food] = price
        print(f"{food} has been added/updated with price {price}")
        self.csv_write()

    def remove_menu(self, food):
        if food in self.food_menu:
            self.food_menu.pop(food)
            print(f"{food} has successfully been removed from the menu")
        else:
            print(f"No item named '{food}' found in the menu")
        self.csv_write()
if __name__=="__main__":
    obj=Menu()
    obj.display_menu()
    