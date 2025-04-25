import tkinter as tk
import os
import csv

import gui.invoice_menu as invoice_gui
import gui.select_customer_menu as select_customer_gui

import lib.invoice as iv
import lib.customer as cstr
import lib.settings as settings

class InvoicerV:
    
    def __init__(self, root):
        
        self.root = root
        
        #Load settings
        self.settings = settings.Settings()
        
        #Load customer
        self.load_customer()
        
        #Define window setting
        self.root.title('Invoicer-V')
        self.root.configure(bg='#ffe4e1')
        
        #Set window full screen
        screen_width = int(self.root.winfo_screenwidth()/2)
        screen_height = int(self.root.winfo_screenheight()/2)
        self.root.geometry(f"{screen_width}x{screen_height}")
        
        #Default fullscreen
        self.root.state('zoomed') 

        #Declare GUI
        self.invoice_menu = invoice_gui.InvoiceMenu(self)
        self.choose_customer_menu = select_customer_gui.SelectCustomerWindow(self)
        
        #Run invoice menu
        self.invoice_menu.run()
        
        self.is_running = True 
        
        
    def create_invoice(self):
        
        print("test")
        #Create invoice here
        
    def load_customer(self):
        
        #Check if customer file exist
        if os.path.exists("data/customers.csv") == False:
            
            if os.path.exists("data") == False:
                
                os.mkdir("data")
           
            with open("data/customers.csv", "w", newline="") as customers_file:
                writer = csv.writer(customers_file, delimiter=";")
                writer.writerow(["name", "address", "immatriculation"])
            
        else:
            #load customer csv here
            with open("data/customers.csv") as customers_file:
                customers_list = csv.DictReader(customers_file, delimiter=";")
                for customer in customers_list:
                        self.customers.append(cstr.Customer(customer['name'], customer['address'], customer['immatriculation']))  
        
    
root = tk.Tk(screenName="InvoicerV", baseName="InvoicerV")
app = InvoicerV(root)

root.mainloop()