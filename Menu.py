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

    