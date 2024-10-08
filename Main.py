import gui
import Menu
import tkinter

obj=Menu.Menu()
def customer(self):
    canvas=tkinter.Canvas(self.user)
    scrollbar=tkinter.Scrollbar(self.user,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right",fill="y")
    canvas.pack(fill="both",expand=True)
    container=tkinter.Frame(canvas)
    canvas.create_window((0,0),window=container, anchor="nw")
    
    for i in obj.food_menu:
        Label=(tkinter.Label(container, text=f"{i, obj.food_menu[i]}",font=("Helvetica", max(10,40-(len(obj.food_menu)//2)))))
        Label.pack()

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    container.bind("<Configure>",on_configure)
def admin(self):
    print("User is in admin")
window=gui.welcomewindow(runcustomer=customer,runadmin=admin)

