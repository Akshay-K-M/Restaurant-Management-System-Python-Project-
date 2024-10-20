import csv 
class Menu:
    def __init__(self) -> None:
        self.food_menu={}
        try:
            # Reading data from file
            with open('Menu.csv','r') as csv_file:
                reader=csv.reader(csv_file)      
                for i in reader: 
                    self.food_menu[i[0]]=i[1]
            # Writing onto the file
            with open('Menu.csv', 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)

                for item, price in self.food_menu.items():
                    writer.writerow([item, price])
        except FileNotFoundError:
            # Handle the case where the file does not exist
            print("Error: 'Menu.csv' file not found. Please ensure the file exists.")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"Unexpected error: {e}")


    