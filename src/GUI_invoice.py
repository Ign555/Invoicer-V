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
from math import sqrt
import pymupdf
import utils as u
import styles
from PIL import Image, ImageTk

"""
*
* Invoice GUI
*
"""

class InvoiceMenu(tk.Frame):
    
    def __init__(self, app):
        
        super().__init__(app, bg=styles.COLORS["window_background"])
        
        self.app = app 
        
        for i in range(0, 8):
            self.rowconfigure(i, weight=1)
            
        for i in range(0, 4):
            self.columnconfigure(i, weight=1)
      
        self.grid(row=0, column=0, padx=0,  pady=0, sticky=tk.NSEW)
        
        
        self.preview_canvas = tk.Canvas(self)
        self.preview_canvas.grid(row=0, column=3, rowspan=8, sticky=tk.NSEW)
       
        self.invoice_number_text_input_label = tk.Label(self, text="Invoice reference", bg=styles.COLORS["window_background"])
        self.invoice_number_text_input_label.grid(row=0, column=0, columnspan=3, padx=styles.GUI_invoice_padx, pady=styles.GUI_invoice_pady, sticky=tk.NSEW)
        
        self.invoice_number_text_input = tk.Entry(self, bg="white")
        self.invoice_number_text_input.grid(row=1, column=0, columnspan=3, padx=styles.GUI_invoice_padx, pady=styles.GUI_invoice_pady, sticky=tk.NSEW)
        
        #Invoice mention 
        self.invoice_mention_text_input_label = tk.Label(self, text="Invoice metion", bg=styles.COLORS["window_background"])
        self.invoice_mention_text_input_label.grid(row=2, column=0, columnspan=3, padx=styles.GUI_invoice_padx, pady=styles.GUI_invoice_pady, sticky=tk.NSEW)
        
        self.invoice_mention_text_input = tk.Entry(self, bg="white")
        self.invoice_mention_text_input.grid(row=3, column=0, columnspan=3, padx=styles.GUI_invoice_padx, pady=styles.GUI_invoice_pady, sticky=tk.NSEW)

        #Invoice choose customer button 
        self.load_customer_button = tk.Button(self, command=self.app.GUI_choose_customer)
        self.load_customer_button.grid(row=4, column=0, columnspan=3, padx=styles.GUI_invoice_padx, pady=styles.GUI_invoice_pady, sticky=tk.NSEW)
        
        self.display_customer()
        
        #Product list
        self.product_list_label = tk.Label(self, text="Products", bg="#ffe4e1")
        self.product_list_label.grid(row=5, column=0, columnspan=1, padx=styles.GUI_invoice_padx, pady=styles.GUI_invoice_pady, sticky=tk.NSEW)
        
        self.product_list = tk.Listbox(self)
        self.product_list.grid(row=6, column=0, columnspan=3, padx=styles.GUI_invoice_padx, pady=styles.GUI_invoice_pady, sticky=tk.NSEW)
        
        #Add product button
        self.product_add_button = tk.Button(self, text="+", command=self.app.GUI_create_product)
        self.product_add_button.grid(row=5, column=1, columnspan=1, padx=styles.GUI_invoice_padx, pady=styles.GUI_invoice_pady, sticky=tk.NSEW)
        self.product_del_button = tk.Button(self, text="-", command=self.app.remove_product)
        self.product_del_button.grid(row=5, column=2, columnspan=1, padx=styles.GUI_invoice_padx, pady=styles.GUI_invoice_pady, sticky=tk.NSEW)
        
        self.create_invoice_button = tk.Button(self, text="Create invoice", command=self.app.create_invoice)
        self.create_invoice_button.grid(row=7, column=0, columnspan=3, padx=styles.GUI_invoice_padx, pady=styles.GUI_invoice_pady, sticky=tk.NSEW)
        #self.invoice_preview()
        #self.app.create_invoice()

    def display_customer(self):
        
        load_customer_button_text = ""
        
        if(self.app.selected_customer.is_defined):
            load_customer_button_text = self.app.selected_customer.name 
        else: 
            load_customer_button_text = "Choose customer"
        
        self.load_customer_button.config(text=load_customer_button_text)
    
    def display_product_rows(self):
        
        self.product_list.delete(0, tk.END) #Delete item from the product list ( widget )
        
        i=1
        for product_row in self.app.product_rows:
            self.product_list.insert(i, f"{product_row.qty}x {product_row.name}({product_row.uprice})")
            i+=1
    
    def invoice_preview(self):
        
        invoice_pdf = pymupdf.Document(".preview.pdf")
        page = invoice_pdf.load_page(0)
        pix = page.get_pixmap()
        invoice_pdf.close()

        new_height = self.preview_canvas.winfo_height()
        new_width = int(new_height/sqrt(2))
        
        self.preview_image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        self.preview_image = self.preview_image.resize((new_width, new_height))
        self.preview_image_tk = ImageTk.PhotoImage(self.preview_image)
        
        self.preview_canvas.delete("all")
        self.preview_canvas.create_image(u.centerx(self.preview_canvas, new_width), u.centery(self.preview_canvas, new_height), image=self.preview_image_tk, anchor=tk.NW)

        self.preview_canvas.grid(row=0, column=3, rowspan=8, sticky=tk.NSEW)
        self.after(100, self.invoice_preview)
        
    def refresh(self):
        
        self.app.update() #update tkinter
        
        self.display_customer()
        self.display_product_rows()
        self.invoice_preview()
        
        self.app.create_preview()
        
        
    def stop(self):
        
        self.create_invoice.destroy()