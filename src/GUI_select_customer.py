import tkinter as tk

class SelectCustomerWindow: 
    
    def __init__(self, app):
        
        self.app = app
        print("creating")
    
    def set_invoice_customer(self):
        
        self.app.selected_customer = ""
        
    def run(self):

        self.root = tk.Toplevel()
        self.root.title('Select your customer')
        self.root.grab_set() #Locking the interraction only for the popup
        
        screen_width = int(self.root.winfo_screenwidth()/4)
        screen_height = int(self.root.winfo_screenheight()/4)
        self.root.geometry(f"{screen_width}x{screen_height}")
        
        #Add customer to list
        self.add_new_custumer_button = tk.Button(self.root, text="+", command=self.app.gui_add_new_customer.run)
        self.add_new_custumer_button.place(relx=0.05, rely=0.1, relw=0.1, relh=0.15)
        
        #Customer list
        self.customer_list = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.customer_list.place(relx=0.05, rely=0.15, relw=0.9, relh=0.60)
        
        #Load customer into the list
        self.load_customer()
        
        #Choose button
        self.add_custumer_button = tk.Button(self.root, text="Choose", command=self.set_invoice_customer)
        self.add_custumer_button.place(relx=0.05, rely=0.8, relw=0.9, relh=0.15)
        
        #Define window setting
        self.root.configure(bg='#ffe4e1')
        self.root.mainloop()
        
    def refresh(self):
        
        self.customer_list.delete(0, tk.END)
        self.load_customer()
    
    def load_customer(self):
        
        i=1
        for customer in self.app.customers:
            self.customer_list.insert(i, customer.name)
            i+=1
    
        self.customer_list.place(relx=0.05, rely=0.15, relw=0.9, relh=0.60)
        
    def stop(self):
        
        self.root.destroy()