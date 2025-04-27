import tkinter as tk

if __name__ == "__main__":
    import select_customer_menu as select_customer_gui
else:
    import GUI_select_customer as select_customer_gui

class InvoiceMenu:
    
    def __init__(self, app):
        
        self.root = app.root
        self.app = app
        
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
        
        #Invoice text feild
        self.invoice_number_text_input = tk.Entry(self.root, bg="white")
        self.invoice_number_text_input.place(relx=0.066, rely=0.177, relw=0.266, relh=0.06)
        
        self.invoice_mention_text_input = tk.Entry(self.root, bg="white")
        self.invoice_mention_text_input.place(relx=0.066, rely=0.295, relw=0.266, relh=0.06)

        #Invoice button 
        self.load_customer_button = tk.Button(self.root, command=self.app.gui_choose_customer.run)
        self.load_customer_button.place(relx=0.066, rely=0.414, relw=0.266, relh=0.06)
        
        self.display_customer()
        
        self.create_invoice_button = tk.Button(self.root, text="Create invoice", command=self.app.create_invoice)
        self.create_invoice_button.place(relx=0.066, rely=0.80, relw=0.266, relh=0.06)
        
        #Product list
        self.product_list = tk.Listbox(self.root)
        self.product_list.place(relx=0.066, rely=0.532, relw=0.266, relh=0.237)
        
        #Product button
        self.product_add_button = tk.Button(self.root, text="+", command=self.app.gui_add_product_row.run)
        self.product_add_button.place(relx=0.066+0.25, rely=0.502, relw=0.016, relh=0.03)
        self.product_del_button = tk.Button(self.root, text="-", command=self.app.create_invoice)
        self.product_del_button.place(relx=0.066+0.23, rely=0.502, relw=0.016, relh=0.03)

        #GUI Label
        self.customer_label = tk.Label(self.root, text="Customers")
    
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
    
    def refresh(self):
        
        self.display_customer()
        self.display_product_rows()
        
        
    def stop(self):
        
        self.create_invoice.destroy()