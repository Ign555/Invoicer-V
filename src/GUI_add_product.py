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
import styles

"""
*
* Add product GUI
*
"""

class AddProductMenu(tk.Toplevel):
    
    def __init__(self, app):
        
        ##############################-Toplevel init-##############################
        
        super().__init__(app, bg=styles.COLORS["window_background"])
        
        ##############################-Set Class Attributes-##############################
        
        self.app = app
        
        ##############################-Toplevel Settings-##############################
        
        #Define window settings
        self.title('Add new product')
        self.grab_set() #Locking the interraction only for the popup
        
        #Set Toplevel size
        screen_width = int(self.winfo_screenwidth()/4)
        screen_height = int(self.winfo_screenheight()/4)
        self.geometry(f"{screen_width}x{screen_height}")
        
        ##############################-Set GUI Settings-##############################
        
        #Configure column
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        
        ##############################-Set GUI Widgets-##############################
        
        #Product name label
        self.product_name_input_label = tk.Label(self, bg="#ffe4e1", anchor=tk.W, text="Product name")
        self.product_name_input_label.grid(row=0, column=0, columnspan=2)
        
        #Product name input
        self.product_name_input = tk.Entry(self, bg="white")
        self.product_name_input.grid(row=1, column=0, columnspan=2, padx=styles.GUI_AP_padx, pady=styles.GUI_AP_pady, sticky=tk.NSEW)
        
        #Product price label
        self.product_price_input_label = tk.Label(self, bg="#ffe4e1", anchor=tk.W, text="Price")
        self.product_price_input_label.grid(row=2, column=0)
        
        #Product price input
        self.product_price_input = tk.Spinbox(self, bg="white", from_=0, to=99999, increment=0.01)
        self.product_price_input.grid(row=3, column=0, padx=styles.GUI_AP_padx, pady=styles.GUI_AP_pady, sticky=tk.NSEW)
        
        #Product quantity label
        self.product_quantity_input_label = tk.Label(self, bg="#ffe4e1", anchor=tk.W, text="Qty")
        self.product_quantity_input_label.grid(row=2, column=1)
        
        #Product quantity input
        self.product_quantity_input = tk.Spinbox(self, bg="white", from_=0, to=99999, increment=1)
        self.product_quantity_input.grid(row=3, column=1, padx=styles.GUI_AP_padx, pady=styles.GUI_AP_pady, sticky=tk.NSEW)
        
        #Add button
        self.add_product_button = tk.Button(self, text="Add", command=self.app.add_product)
        self.add_product_button.grid(row=4, column=0, columnspan=2, padx=styles.GUI_AP_padx, pady=styles.GUI_AP_pady, sticky=tk.NSEW)
        
    def close(self):
        
        self.destroy()
        self.update()