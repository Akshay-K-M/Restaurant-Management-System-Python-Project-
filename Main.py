import gui
import Menu
import tkinter
import Order
import csv
from tkinter import messagebox,simpledialog
order=Order.Display_Menu()
obj=Menu.Menu()    
window=gui.WelcomeWindow(runcustomer=gui.customer,runadmin=gui.admin)

