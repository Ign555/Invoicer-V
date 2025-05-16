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
import styles as s

"""
*
* Select Customer GUI
*
"""

class SelectCustomerWindow(tk.Toplevel): 
    
    def __init__(self, app):
        
        ##############################-Toplevel init-##############################
        
        super().__init__(app, bg="white")
        
        ##############################-Set Class Attributes-##############################
        
        self.app = app
        
        ##############################-Toplevel Settings-##############################
        
        #Define window settings
        self.title("Select your customer")
        self.grab_set() #Locking the interraction only for the popup
        
        #Set top level size
        screen_width = int(self.winfo_screenwidth()/4)
        screen_height = int(self.winfo_screenheight()/4)
        self.geometry(f"{screen_width}x{screen_height}")
        
        ##############################-Set GUI Settings-##############################        
        
        #Configure column
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0, minsize=s.GUI_SC_row_minsize)
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1, minsize=s.GUI_SC_row_minsize)
        
        ##############################-Set GUI Widgets-##############################
        
        #Customer list label
        self.customer_list_label = tk.Label(self, text="Customers", bg="#ffe4e1", anchor=tk.W)
        self.customer_list_label.grid(row=0, column=0, padx=s.GUI_SC_padx, pady=(s.GUI_SC_pady, 0), sticky=tk.SW)
        
        #Add customer to list button
        self.add_new_customer_button = tk.Button(self, text="+", command=self.app.GUI_create_customer)
        self.add_new_customer_button.grid(row=0, column=1, padx=s.GUI_SC_padx, pady=(s.GUI_SC_pady, 0), sticky=tk.NSEW)
        
        #Customer list
        self.customer_list = tk.Listbox(self, selectmode=tk.SINGLE)
        self.customer_list.grid(row=1, column=0, padx=s.GUI_SC_padx, columnspan=2, sticky=tk.NSEW)
        
        #Load customer into the list
        self.load_customers()
        
        #Choose button
        self.add_custumer_button = tk.Button(self, text="Choose", command=self.app.set_invoice_customer)
        self.add_custumer_button.grid(row=2, column=0, padx=s.GUI_SC_padx, pady=s.GUI_SC_pady, columnspan=2, sticky=tk.NSEW)
        
    def refresh(self):
        
        self.customer_list.delete(0, tk.END)
        self.load_customers()
    
    def load_customers(self):
        
        i=1
        for customer in self.app.customers:
            self.customer_list.insert(i, customer.name)
            i+=1
            
        self.customer_list.select_set(0)
        self.customer_list.grid(row=1, column=0, padx=s.GUI_SC_padx, columnspan=2, sticky=tk.NSEW)
        
    def close(self):
        
        self.destroy()
        self.update()
        