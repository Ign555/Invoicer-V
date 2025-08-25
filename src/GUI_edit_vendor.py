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
* EditVendor GUI
*
"""

class EditVendorGUI(tk.Toplevel):

    def __init__(self, app):
        
        ##############################-Toplevel init-##############################
        
        super().__init__(app, bg=styles.COLORS["window_background"])
        
        ##############################-Set Class Attributes-##############################
        
        self.app = app
        
        ##############################-Toplevel Settings-##############################
        
        #Define window settings
        self.title('Edit vendor')
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
        
        #vendor name feild label
        self.vendor_name_label = tk.Label(self, text="vendor name", bg=styles.COLORS["window_background"], anchor=tk.W)
        self.vendor_name_label.grid(row=0, column=0, padx=styles.GUI_AC_padx, pady=styles.GUI_AC_pady, sticky=tk.NSEW)
        
        #vendor name feild
        self.vendor_name = tk.Entry(self)
        self.vendor_name.grid(row=1, column=0, padx=styles.GUI_AC_padx, pady=styles.GUI_AC_pady, sticky=tk.NSEW)
        self.vendor_name.insert(tk.END, app.cfg.vendor.name)
        
        #vendor immatriculation label
        self.vendor_immatriculation_label = tk.Label(self, text="vendor Immatriculation", bg=styles.COLORS["window_background"], anchor=tk.W)
        self.vendor_immatriculation_label.grid(row=0, column=1, padx=styles.GUI_AC_padx, pady=styles.GUI_AC_pady, sticky=tk.NSEW)
        
        #vendor immatriculation feild
        self.vendor_immatriculation = tk.Entry(self)
        self.vendor_immatriculation.grid(row=1, column=1, padx=styles.GUI_AC_padx, pady=styles.GUI_AC_pady, sticky=tk.NSEW)
        self.vendor_immatriculation.insert(tk.END, app.cfg.vendor.immatriculation)
        
        
        #vendor address label
        self.vendor_street_label = tk.Label(self, text="vendor Address", bg=styles.COLORS["window_background"], anchor=tk.W)
        self.vendor_street_label.grid(row=2, column=0, padx=styles.GUI_AC_padx, pady=styles.GUI_AC_pady, sticky=tk.NSEW)
        
        #vendor address feild
        self.vendor_street = tk.Entry(self)
        self.vendor_street.grid(row=3, column=0, columnspan=2, padx=styles.GUI_AC_padx, pady=styles.GUI_AC_pady, sticky=tk.NSEW)
        self.vendor_street.insert(tk.END, app.cfg.vendor.address["street"])
        
        #vendor city label
        self.vendor_city_label = tk.Label(self, text="vendor city", bg=styles.COLORS["window_background"], anchor=tk.W)
        self.vendor_city_label.grid(row=4, column=0, padx=styles.GUI_AC_padx, pady=styles.GUI_AC_pady, sticky=tk.NSEW)
        
        #vendor city feild
        self.vendor_city = tk.Entry(self)
        self.vendor_city.grid(row=5, column=0, padx=styles.GUI_AC_padx, pady=styles.GUI_AC_pady, sticky=tk.NSEW)
        self.vendor_city.insert(tk.END, app.cfg.vendor.address["city"])
        
        #vendor postcode label
        self.vendor_postcode_label = tk.Label(self, text="Postcode", bg=styles.COLORS["window_background"], anchor=tk.W)
        self.vendor_postcode_label.grid(row=4, column=1, padx=styles.GUI_AC_padx, pady=styles.GUI_AC_pady, sticky=tk.NSEW)
        
        #vendor postcode feild
        self.vendor_postcode = tk.Entry(self)
        self.vendor_postcode.grid(row=5, column=1, padx=styles.GUI_AC_padx, pady=styles.GUI_AC_pady, sticky=tk.NSEW)
        self.vendor_postcode.insert(tk.END, app.cfg.vendor.address["postcode"])
        
        #vendor phone label
        self.vendor_phone_label = tk.Label(self, text="vendor phone", bg=styles.COLORS["window_background"], anchor=tk.W)
        self.vendor_phone_label.grid(row=6, column=0, padx=styles.GUI_AC_padx, pady=styles.GUI_AC_pady, sticky=tk.NSEW)
        
        #vendor phone feild
        self.vendor_phone = tk.Entry(self)
        self.vendor_phone.grid(row=7, column=0, padx=styles.GUI_AC_padx, pady=styles.GUI_AC_pady, sticky=tk.NSEW)
        self.vendor_phone.insert(tk.END, app.cfg.vendor.phone)
        
        #vendor mail label
        self.vendor_email_label = tk.Label(self, text="vendor mail", bg=styles.COLORS["window_background"], anchor=tk.W)
        self.vendor_email_label.grid(row=6, column=1, padx=styles.GUI_AC_padx, pady=styles.GUI_AC_pady, sticky=tk.NSEW)
        
        #vendor mail feild
        self.vendor_email = tk.Entry(self)
        self.vendor_email.grid(row=7, column=1, padx=styles.GUI_AC_padx, pady=styles.GUI_AC_pady, sticky=tk.NSEW)
        self.vendor_phone.insert(tk.END, app.cfg.vendor.mail)
        
        #Edit button
        self.add_button = tk.Button(self, text="Edit", command=self.app.edit_vendor)
        self.add_button.grid(row=8, column=0, padx=styles.GUI_AC_padx, pady=styles.GUI_AC_pady, columnspan=2, sticky=tk.NSEW)
        
    def close(self):
        
        self.destroy()
        self.update()