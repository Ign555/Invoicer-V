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

"""
*
* AddNewCustomer GUI
*
"""

class AddNewCustomerGUI(tk.Toplevel):

    def __init__(self, app):
        
        ##############################-Toplevel init-##############################
        
        super().__init__(app, bg="white")
        
        ##############################-Set Class Attributes-##############################
        
        self.app = app
        
        ##############################-Toplevel Settings-##############################
        
        #Define window settings
        self.title('Add new product')
        self.grab_set() #Locking the interraction only for the popup
        
        #Set Toplevel size
        screen_width = int(self.winfo_screenwidth()/3)
        screen_height = int(self.winfo_screenheight()/2)
        self.geometry(f"{screen_width}x{screen_height}")
        
        ##############################-Set GUI Settings-##############################
        
        #Configure column
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)
        self.rowconfigure(5, weight=0)
        self.rowconfigure(6, weight=0)
        self.rowconfigure(7, weight=0)
        self.rowconfigure(8, weight=0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        
        ##############################-Set GUI Widgets-##############################
        
        #Customer name feild label
        self.customer_name_label = tk.Label(self, text="Customer name", bg='#ffe4e1', anchor=tk.W)
        self.customer_name_label.grid(row=0, column=0)
        
        #Customer name feild
        self.customer_name = tk.Entry(self)
        self.customer_name.grid(row=1, column=0)
        
        #Customer immatriculation label
        self.customer_immatriculation_label = tk.Label(self, text="Customer Immatriculation", bg='#ffe4e1', anchor=tk.W)
        self.customer_immatriculation_label.grid(row=0, column=1)
        
        #Customer immatriculation feild
        self.customer_immatriculation = tk.Entry(self)
        self.customer_immatriculation.grid(row=1, column=1)
        
        #Customer street label
        self.customer_street_label = tk.Label(self, text="Customer street", bg='#ffe4e1', anchor=tk.W)
        self.customer_street_label.grid(row=2, column=0, columnspan=2)
        
        #Customer street feild
        self.customer_street = tk.Entry(self)
        self.customer_street.grid(row=3, column=0, columnspan=2)
        
        #Customer city label
        self.customer_city_label = tk.Label(self, text="Customer city", bg='#ffe4e1', anchor=tk.W)
        self.customer_city_label.grid(row=4, column=0)
        
        #Customer city feild
        self.customer_city = tk.Entry(self)
        self.customer_city.grid(row=5, column=0)
        
        #Customer postcode label
        self.customer_postcode_label = tk.Label(self, text="Postcode", bg='#ffe4e1', anchor=tk.W)
        self.customer_postcode_label.grid(row=4, column=1)
        
        #Customer postcode feild
        self.customer_postcode = tk.Entry(self)
        self.customer_postcode.grid(row=5, column=1)
        
        #Customer phone label
        self.customer_phone_label = tk.Label(self, text="Customer phone", bg='#ffe4e1', anchor=tk.W)
        self.customer_phone_label.grid(row=6, column=0)
        
        #Customer phone feild
        self.customer_phone = tk.Entry(self)
        self.customer_phone.grid(row=7, column=0)
        
        #Customer mail label
        self.customer_email_label = tk.Label(self, text="Customer mail", bg='#ffe4e1', anchor=tk.W)
        self.customer_email_label.grid(row=6, column=1)
        
        #Customer mail feild
        self.customer_email = tk.Entry(self)
        self.customer_email.grid(row=7, column=1)
        
        #Add button
        self.add_button = tk.Button(self, text="Add", command=self.app.add_new_customer)
        self.add_button.grid(row=8, column=0, columnspan=2)
        
    def close(self):
        
        self.destroy()
        self.update()