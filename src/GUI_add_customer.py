import tkinter as tk 

class AddNewCustomerGUI:

    def __init__(self, app):
        
        self.app = app
        
    def run(self):
        
        self.root = tk.Toplevel()
        self.root.title('Add new customer')
        self.root.grab_set() #Locking the interraction only for the popup
        
        screen_width = int(self.root.winfo_screenwidth()/4)
        screen_height = int(self.root.winfo_screenheight()/2)
        self.root.geometry(f"{screen_width}x{screen_height}")
        
        #Customer information input
        self.customer_name = tk.Entry(self.root)
        self.customer_address = tk.Entry(self.root)
        self.customer_immatriculation = tk.Entry(self.root)
        self.customer_phone = tk.Entry(self.root)
        self.customer_email = tk.Entry(self.root)
        
        self.customer_name.place(relx=0.05, rely=0.15, relw=0.90, relh=0.05)
        self.customer_address.place(relx=0.05, rely=0.30, relw=0.90, relh=0.05)
        self.customer_immatriculation.place(relx=0.05, rely=0.45, relw=0.90, relh=0.05)
        self.customer_phone.place(relx=0.05, rely=0.60, relw=0.90, relh=0.05)
        self.customer_email.place(relx=0.05, rely=0.75, relw=0.90, relh=0.05)
        
        #Add button
        self.add_button = tk.Button(self.root, text="Add", command=self.app.add_new_customer)
        self.add_button.place(relx=0.05, rely=0.85, relw=0.9, relh=0.10)
        
        #GUI Entry Label
        customer_name_label_text = tk.StringVar()
        customer_name_label_text.set("Customer full name")
        customer_address_label_text = tk.StringVar()
        customer_address_label_text.set("Customer address")
        customer_immatriculation_label_text = tk.StringVar()
        customer_immatriculation_label_text.set("Customer Immatriculation")
        customer_phone_label = tk.StringVar()
        customer_phone_label.set("Customer phone")
        customer_email_label = tk.StringVar()
        customer_email_label.set("Customer mail")
        
        self.customer_name_label = tk.Label(self.root, textvariable=customer_name_label_text, anchor=tk.W, font=("Arial", 16, "bold"))
        self.customer_address_label = tk.Label(self.root, textvariable=customer_address_label_text, anchor=tk.W, font=("Arial", 16, "bold"))
        self.customer_immatriculation_label = tk.Label(self.root, textvariable=customer_immatriculation_label_text, anchor=tk.W, font=("Arial", 16, "bold"))
        self.customer_phone_label = tk.Label(self.root, textvariable=customer_phone_label, anchor=tk.W, font=("Arial", 16, "bold"))
        self.customer_email_label = tk.Label(self.root, textvariable=customer_email_label, anchor=tk.W)
        
        self.customer_name_label.place(relx=0.05, rely=0.10, relw=0.9, relh=0.05)
        self.customer_address_label.place(relx=0.05, rely=0.25, relw=0.9, relh=0.05)
        self.customer_immatriculation_label.place(relx=0.05, rely=0.40, relw=0.9, relh=0.05)
        self.customer_phone_label.place(relx=0.05, rely=0.55, relw=0.9, relh=0.05)
        self.customer_email_label.place(relx=0.05, rely=0.70, relw=0.9, relh=0.05)
        
        #Define window setting
        self.root.configure(bg='#ffe4e1')
        self.root.mainloop()
        
    def close(self):
        
        self.root.destroy()
        self.root.update()