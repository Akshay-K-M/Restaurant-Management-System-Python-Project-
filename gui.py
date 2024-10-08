import tkinter 
from tkinter import font

class welcomewindow():
    def __init__(self,runcustomer=None,runadmin=None):
        self.runcustomer=runcustomer
        self.runadmin=runadmin
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
        self.user=tkinter.Tk()
        self.user.title("Customer")
        self.user.geometry("1280x720")
        
        self.gobackbutton=tkinter.Button(self.user,text="Go Back",font=("Helvetica", 40),command=self.goback1)
        self.gobackbutton.pack(side="top", anchor="nw", padx=25,pady=25)
        if self.runcustomer:
            self.runcustomer(self)
        self.user.mainloop()
        
    
        
    def gotoadmin(self):
        self.welcome.destroy()
        self.admin=tkinter.Tk()
        self.admin.title("Admin")
        self.admin.geometry("1280x720")
        self.gobackbutton=tkinter.Button(self.admin,text="Go Back",font=("Helvetica", 40),command=self.goback2)
        self.gobackbutton.pack(side="top", anchor="nw", padx=25,pady=25)
        if self.runadmin:
            self.runadmin(self)
        self.admin.mainloop()

    def goback1(self): # go back from customer
        self.user.destroy()
        welcomewindow(self.runcustomer,self.runadmin)
    
    def goback2(self): #go back from admin
        self.admin.destroy()
        welcomewindow(self.runcustomer,self.runadmin)


if __name__=="__main__":
    def customer():
        print("User is in customer")

    def admin():
        print("User is in admin")
    window=welcomewindow(runcustomer=customer,runadmin=admin)