import tkinter as tk

if __name__ == "__main__":
    import select_customer_menu as select_customer_gui
else:
    import gui.select_customer_menu as select_customer_gui

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
        
        self.create_invoice_button = tk.Button(self.root, text="Create invoice", command=self.app.create_invoice)
        self.create_invoice_button.pack(pady=10)
        self.create_invoice_button = tk.Button(self.root, text="Choose customer", command=self.app.choose_customer_menu.run)
        self.create_invoice_button.pack(pady=50)

    def stop(self):
        
        self.create_invoice.destroy()