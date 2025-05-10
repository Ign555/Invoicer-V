import tkinter as tk
import pymupdf
import utils
from PIL import Image, ImageTk

class InvoiceMenu:
    
    def __init__(self, app):
        
        self.root = app.root
        self.app = app
       
        self.preview_canvas = tk.Canvas(self.root)
        self.preview_canvas.place(relx = 0.6, rely = 0.2)
        
    def run(self):
        
        #Creates menu 
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        invoice_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='Invoices', menu=invoice_menu)
        invoice_menu.add_command(label="Import..")
        
        customer_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='Customer', menu=customer_menu)
        
        settings_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='Settings', menu=settings_menu)
        
        help_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label='Help', menu=help_menu)
        
        #Invoice number input
        self.invoice_number_text_input_label = tk.Label(self.root, text="Invoice reference", bg="#ffe4e1", anchor=tk.W)
        self.invoice_number_text_input_label.place(relx=0.066, rely=0.147, relw=0.266, relh=0.03)
        
        self.invoice_number_text_input = tk.Entry(self.root, bg="white")
        self.invoice_number_text_input.place(relx=0.066, rely=0.177, relw=0.266, relh=0.06)
        
        #Invoice mention 
        self.invoice_mention_text_input_label = tk.Label(self.root, text="Invoice metion", bg="#ffe4e1", anchor=tk.W)
        self.invoice_mention_text_input_label.place(relx=0.066, rely=0.265, relw=0.266, relh=0.03)
        
        self.invoice_mention_text_input = tk.Entry(self.root, bg="white")
        self.invoice_mention_text_input.place(relx=0.066, rely=0.295, relw=0.266, relh=0.06)

        #Invoice choose customer button 
        self.load_customer_button = tk.Button(self.root, command=self.app.gui_choose_customer.run)
        self.load_customer_button.place(relx=0.066, rely=0.414, relw=0.266, relh=0.06)
        
        self.display_customer()
        
        #Product list
        self.product_list_label = tk.Label(self.root, text="Products", bg="#ffe4e1", anchor=tk.W)
        self.product_list_label.place(relx=0.066, rely=0.502, relw=0.266, relh=0.03)
        
        self.product_list = tk.Listbox(self.root)
        self.product_list.place(relx=0.066, rely=0.532, relw=0.266, relh=0.237)
        
        #Add product button
        self.product_add_button = tk.Button(self.root, text="+", command=self.app.gui_add_product_row.run)
        self.product_add_button.place(relx=0.066+0.25, rely=0.502, relw=0.016, relh=0.03)
        self.product_del_button = tk.Button(self.root, text="-", command=self.app.remove_product)
        self.product_del_button.place(relx=0.066+0.23, rely=0.502, relw=0.016, relh=0.03)
        
        #Create invoice button
        self.create_invoice_button = tk.Button(self.root, text="Create invoice", command=self.app.create_invoice)
        self.create_invoice_button.place(relx=0.066, rely=0.80, relw=0.266, relh=0.06)
        self.invoice_preview()
        #self.app.create_invoice()
        

    def display_customer(self):
        
        load_customer_button_text = ""
        
        if(self.app.selected_customer.is_defined):
            load_customer_button_text = self.app.selected_customer.name 
        else: 
            load_customer_button_text = "Choose customer"
        
        self.load_customer_button.config(text=load_customer_button_text)
    
    def display_product_rows(self):
        
        i=1
        for product_row in self.app.product_rows:
            self.product_list.insert(i, f"{product_row.qty}x {product_row.name}({product_row.uprice})")
            i+=1
    
    def invoice_preview(self):
        invoice_pdf = pymupdf.Document(".preview.pdf")
        page = invoice_pdf.load_page(0)
        pix = page.get_pixmap()
        invoice_pdf.close()
        screen_width = int(self.root.winfo_screenwidth()/2)
        screen_height = int(self.root.winfo_screenheight()/2)
        (w, h) = utils.scale_widget_relative_to_window(screen_width, screen_height, 0.3, 595 , 842 )
        
        new_width = int(screen_width*w)*2
        new_height = int(screen_height*h)*2
       
        self.preview_image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        self.preview_image = self.preview_image.resize((new_width, new_height))
        self.preview_image_tk = ImageTk.PhotoImage(self.preview_image)
        
        self.preview_canvas.config(width=new_width, height=new_height)
        self.preview_canvas.delete("all")
        self.preview_canvas.create_image(0, 0, image=self.preview_image_tk, anchor=tk.NW)
        self.preview_canvas.place(relx = 0.6, rely = 0.2, relw=w, relh=h)
        self.root.after(100, self.invoice_preview)
        
        
    
    def refresh(self):
        
        self.display_customer()
        self.product_list.delete(0, tk.END)
        self.display_product_rows()
        self.invoice_preview()
        
        self.app.create_preview()
        
        
    def stop(self):
        
        self.create_invoice.destroy()