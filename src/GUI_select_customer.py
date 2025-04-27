import tkinter as tk

class SelectCustomerWindow: 
    
    def __init__(self, app):
        
        self.app = app
        print("creating")
      
        
    def run(self):

        self.root = tk.Toplevel()
        self.root.title('Select your customer')
        self.root.grab_set() #Locking the interraction only for the popup
        
        screen_width = int(self.root.winfo_screenwidth()/4)
        screen_height = int(self.root.winfo_screenheight()/4)
        self.root.geometry(f"{screen_width}x{screen_height}")
        
        #Add customer to list
        self.add_new_custumer_button = tk.Button(self.root, text="+", command=self.app.add_new_customer_menu.run)
        self.add_new_custumer_button.place(relx=0.05, rely=0.1, relw=0.1, relh=0.15)
        
        #Customer list
        self.customer_list = tk.Listbox(self.root)
        self.customer_list.place(relx=0.05, rely=0.15, relw=0.9, relh=0.60)
        
        #Choose button
        self.add_custumer_button = tk.Button(self.root, text="Choose")
        self.add_custumer_button.place(relx=0.05, rely=0.8, relw=0.9, relh=0.15)
        
        #Define window setting
        self.root.configure(bg='#ffe4e1')
        self.root.mainloop()
        
    
    def stop(self):
        
        self.root.destroy()