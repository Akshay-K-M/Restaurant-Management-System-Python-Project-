import tkinter 
from tkinter import font
class welcomewindow():
    def __init__(self):
        self.welcome=tkinter.Tk()
        self.welcome.title("Restaurant Management System (RMS)")
        self.welcome.geometry("1280x720")

    
        self.label = tkinter.Label(self.welcome, text="Welcome To Flavourful!",font=("Helvetica", 80))
        self.label.pack(fill="both",pady=40)

        self.customerbutton=tkinter.Button(self.welcome,text="Place Order",font=("Helvetica", 80),command=self.gotocustomer)
        self.customerbutton.pack(pady=100)

        self.adminbutton=tkinter.Button(self.welcome,text="Manage Menu",font=("Helvetica", 80),command=self.gotoadmin)
        self.adminbutton.pack(pady=5)
        self.welcome.mainloop()
    
    
    def gotocustomer(self):
        self.welcome.destroy()
        customer()
    
    def gotoadmin(self):
        self.welcome.destroy()
        admin()

class customer():
    def __init__(self):
        self.user=tkinter.Tk()
        self.user.title("Customer")
        self.user.geometry("1280x720")
        

        self.gobackbutton=tkinter.Button(self.user,text="Go Back",font=("Helvetica", 40),command=self.goback)
        self.gobackbutton.pack(side="top", anchor="nw", padx=25,pady=25)
        self.user.mainloop()
    def goback(self):
        self.user.destroy()
        welcomewindow()
    

class admin():
    def __init__(self):
        self.admin=tkinter.Tk()
        self.admin.title("Admin")
        self.admin.geometry("1280x720")
        self.gobackbutton=tkinter.Button(self.admin,text="Go Back",font=("Helvetica", 40),command=self.goback)
        self.gobackbutton.pack(side="top", anchor="nw", padx=25,pady=25)
        self.admin.mainloop()
    def goback(self):
        self.admin.destroy()
        welcomewindow()

if __name__=="__main__":
    welcomewindow()
    