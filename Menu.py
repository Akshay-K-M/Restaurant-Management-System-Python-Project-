import csv
class Menu:
    def __init__(self) -> None:
        self.food_menu={}
        try:
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
        except FileNotFoundError:
            print("Error: 'Menu.csv' file not found. Please ensure the file exists.")
        except Exception as e:
            print(f"Unexpected error: {e}")


    