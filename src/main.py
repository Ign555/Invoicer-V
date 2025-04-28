import tkinter as tk
import os
import csv

import GUI_invoice as invoice_gui
import GUI_select_customer as select_customer_gui
import GUI_add_product as add_product_gui
import GUI_add_customer as add_customer_gui

import invoice as iv
import customer as cr
import product_row as pr
import settings as settings

class InvoicerV:
    
    customers = []
    product_rows = []
    selected_customer = cr.Customer()
    
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
        self.gui_invoice = invoice_gui.InvoiceMenu(self)
        self.gui_choose_customer = select_customer_gui.SelectCustomerWindow(self)
        self.gui_add_product_row = add_product_gui.AddProductMenu(self)
        self.gui_add_new_customer = add_customer_gui.AddNewCustomerGUI(self)
        
        #Run invoice menu
        self.gui_invoice.run()
        
        self.is_running = True 
        
    def set_invoice_customer(self):
        
        self.selected_customer = self.customers[self.gui_choose_customer.customer_list.curselection()[0]]
        self.gui_choose_customer.close()
        
        self.gui_invoice.refresh()
        
    def add_product(self):
        
        self.product_rows.append(pr.ProductRow(self.gui_add_product_row.product_quantity_input.get(), self.gui_add_product_row.product_name_input.get(), self.gui_add_product_row.product_price_input.get()))
        self.gui_add_product_row.close()
        
        self.gui_invoice.refresh()
    
    def remove_product(self):
        
        self.product_rows.pop((self.gui_invoice.product_list.curselection()[0]))
    
    def add_new_customer(self):

        self.customers.append(cr.Customer(self.gui_add_new_customer.customer_name.get(), self.gui_add_new_customer.customer_address.get(), self.gui_add_new_customer.customer_immatriculation.get()))  
        self.gui_add_new_customer.close()
        
        self.gui_choose_customer.refresh()
        
    def create_invoice(self):
        
        print("test")
        #Create invoice here
        
    def load_customer(self):
        
        #Check if customer file exist
        if os.path.exists("../data/customers.csv") == False:
            
            if os.path.exists("../data") == False:
                
                os.mkdir("../data")
           
            with open("../data/customers.csv", "w", newline="") as customers_file:
                writer = csv.writer(customers_file, delimiter=";")
                writer.writerow(["name", "address", "immatriculation", "phone", "email"])
            
        else:
            #load customer csv here
            with open("../data/customers.csv") as customers_file:
                customers_list = csv.DictReader(customers_file, delimiter=";")
                for customer in customers_list:
                        self.customers.append(cr.Customer(customer['name'], customer['address'], customer['immatriculation']))  
        
    
    def save_customer(self):
            
        with open("../data/customers.csv", "w") as customers_file:
            
            customers_csv = csv.writer(customers_file, delimiter=";")
            
            customers_csv.writerow(["name", "address", "immatriculation", "phone", "email"])
            
            for customer in self.customers:
                customers_csv.writerow([customer.name, customer.address, customer.immatriculation, customer.phone, customer.mail])
            
    def close(self):
            
          self.save_customer()
          self.root.destroy()
    
root = tk.Tk(screenName="InvoicerV", baseName="InvoicerV")
app = InvoicerV(root)

#Event on quit 
root.protocol("WM_DELETE_WINDOW", app.close)

root.mainloop()