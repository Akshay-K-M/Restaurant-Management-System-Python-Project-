import csv

class Menu:
    def __init__(self) -> None:
        self.food_menu = {
            # Appetizers
            "Garlic Bread": 29,  
            "Mozzarella Sticks": 49,  
            "Chicken Wings": 69,  
            "Stuffed Mushrooms": 59,  

            # Soups & Salads
            "Tomato Soup": 29,  
            "Caesar Salad": 49,  
            "House Salad": 39,  

            # Main Courses
            "Cheeseburger": 99,  
            "Grilled Chicken Sandwich": 89,  
            "Spaghetti Bolognese": 109,  
            "Grilled Salmon": 149,  
            "BBQ Chicken Pizza": 129,  
            "Vegan Stir-fry": 109,  

            # Side Dishes
            "French Fries": 39,  
            "Onion Rings": 49,  
            "Mashed Potatoes": 49,  

            # Beverages
            "Coca Cola": 19,  
            "Iced Tea": 29,  
            "Coffee": 39,  
            "Lemonade": 29,  

            # Desserts
            "Chocolate Cake": 59,  
            "Ice Cream": 39,  
            "Apple Pie": 49}

        # Writing the initial menu to CSV
        with open('Menu.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            # Writing the header (fieldnames)
            writer.writerow(["Item", "Price(Rs)"])
            # Writing the rows (menu items)
            for item, price in self.food_menu.items():
                writer.writerow([item, price])

    def csv_write(self):
        # Writing the updated menu to CSV
        with open('Menu.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Item", "Price"])  # Writing the header
            for item, price in self.food_menu.items():
                writer.writerow([item, price])  # Writing each item

    def display_menu(self):
        return self.food_menu

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
    