# -*- coding: utf-8 -*-

"""
*
*
* INVOICER-V - invoice making software
* Created by Ign555
* Version : v0.9
* Project Creation : 10/04/2025
*
*
"""

import tkinter as tk
import csv
import os
import ast
from datetime import date

import settings

import GUI_invoice as invoice_gui
import GUI_select_customer as select_customer_gui
import GUI_add_product as add_product_gui
import GUI_add_customer as add_customer_gui

import invoice as iv
import customer as cr
import vendor as v
import product_row as pr
import settings as settings
from styles import COLORS

"""
*
* Main
*
"""

class InvoicerV(tk.Tk):
    
    customers = []
    product_rows = []
    selected_customer = cr.Customer()
    vendor = v.Vendor()
    
    def __init__(self):
        
        ##############################-App init-##############################
        
        super().__init__(screenName="InvoicerV", baseName="InvoicerV")
        
        ##############################-App Window Settings-##############################
        
        #Define window settings
        self.title('Invoicer-V')
        self.configure(bg=COLORS["window_background"])
        
        #Set window size
        width = int(self.winfo_screenwidth()/2)
        height = int(self.winfo_screenheight()/2)
        self.geometry(f"{width}x{height}")
        
        #Default -> mode fullscreen
        self.state('zoomed')
        
        ##############################-Data & Settings loading-##############################
        
        #Load settings
        self.cfg = settings.Settings()
        
        #Load customer
        self.load_customer()
        
        ##############################-Set GUI Settings-##############################
        
        #Configure window grid for frame
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        ##############################-Set GUI Widgets-##############################
        
        #Add app menu
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)
        
        self.invoice_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='Invoices', menu=self.invoice_menu)
        self.invoice_menu.add_command(label="Import..")
        
        self.customer_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='Customer', menu=self.customer_menu)
        
        self.vendor_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='Company', menu=self.vendor_menu)
        self.vendor_menu.add_command(label="Edit..")
        
        self.settings_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='Settings', menu=self.settings_menu)
        
        self.help_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='Help', menu=self.help_menu)
        
        
        #Load invoice making gui
        self.gui_invoice = invoice_gui.InvoiceMenu(self)
        
        #Refresh it before running
        self.gui_invoice.refresh()
        
        self.is_running = True 
        
    ##############################-Invoke app GUI-##############################
    
    def GUI_choose_customer(self):
        self.gui_choose_customer = select_customer_gui.SelectCustomerWindow(self)
    
    def GUI_create_product(self):
        self.gui_add_product_row = add_product_gui.AddProductMenu(self)
    
    def GUI_create_customer(self):
        self.gui_add_new_customer = add_customer_gui.AddNewCustomerGUI(self)
    
    ##############################-Edit app GUI-##############################
    
    def create_preview(self):
        
        invoice = iv.Invoice(self.gui_invoice.invoice_number_text_input.get(), date.today(), self.cfg.vendor, self.selected_customer, self.product_rows)
        invoice.export_PDF(".preview.pdf")
        
    ##############################-Add data to app-##############################
    
    def add_new_customer(self):

        customer_name = self.gui_add_new_customer.customer_name.get()
        customer_address = {"street" : self.gui_add_new_customer.customer_street.get(), "city" : self.gui_add_new_customer.customer_city.get(), "postcode" : self.gui_add_new_customer.customer_postcode.get()}
        customer_immatriculation = self.gui_add_new_customer.customer_immatriculation.get()
        
        if customer_name != "":
            self.customers.append(cr.Customer(customer_name, customer_address, customer_immatriculation))  
            self.gui_add_new_customer.close()
            self.gui_choose_customer.refresh()
        else:
            self.incomplete_form_message_box("Un client droit au moins avoir un nom")
    
    ##############################-Edit invoice informations-##############################
    
    def set_invoice_customer(self):
        
        if hasattr(self, 'gui_choose_customer'):
            self.selected_customer = self.customers[self.gui_choose_customer.customer_list.curselection()[0]]
            self.gui_choose_customer.close()
        else:
            print("do no exist")
        
        self.gui_invoice.refresh()
        
    def add_product(self):
        
        p_qty_str = self.gui_add_product_row.product_quantity_input.get()
        p_name = self.gui_add_product_row.product_name_input.get()
        p_price_str = self.gui_add_product_row.product_price_input.get()
        
        if p_qty_str != "" and p_name != "" and p_price_str != "":
            self.product_rows.append(pr.ProductRow(int(p_qty_str), p_name, float(p_price_str)))
            self.gui_add_product_row.close()
            self.gui_invoice.refresh()
        else:
            ms_message = "Vous devez remplir tout les champs avant d'enregistrer un nouveau produit"
            self.incomplete_form_message_box(ms_message)
    
    def remove_product(self):
    
        if(len(self.gui_invoice.product_list.curselection()) > 0):
            self.product_rows.pop((self.gui_invoice.product_list.curselection()[0]))
        
        self.gui_invoice.refresh()
             
        
    ##############################-Customer files management-##############################
    
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
                        self.customers.append(cr.Customer(customer['name'], ast.literal_eval(customer['address']), customer['immatriculation']))  
        
    def save_customer(self):
            
        with open("../data/customers.csv", "w") as customers_file:

            customers_csv = csv.writer(customers_file, delimiter=";")
            
            customers_csv.writerow(["name", "address", "immatriculation", "phone", "email"])
            
            for customer in self.customers:
                customers_csv.writerow([customer.name, str(customer.address), customer.immatriculation, customer.phone, customer.mail])
   
    ##############################-Export data-##############################
    
    def create_invoice(self):
        
        #Ask user where does he want to save the file
        files = [('All files', '*.*'), ('PDF Files', '*.pdf')]
        file = tk.filedialog.asksaveasfilename(filetypes = files, defaultextension = files)
        
        #Create the pdf invoice and save it
        invoice = iv.Invoice(self.gui_invoice.invoice_number_text_input.get(), date.today(), self.cfg.vendor, self.selected_customer, self.product_rows)
        invoice.export_PDF(file)
    
    ##############################-Tools-##############################
    
    def incomplete_form_message_box(self, message=""):
        tk.messagebox.showwarning(message=message, title="Formulaire incomplet")
    
    ##############################-Close app-##############################
    
    def close(self):
            
          self.save_customer()
          self.destroy()
    
app = InvoicerV()

#Event on quit 

app.protocol("WM_DELETE_WINDOW", app.close)

app.mainloop()