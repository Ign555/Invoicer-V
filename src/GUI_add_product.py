import tkinter as tk
import product_row as pr

class AddProductMenu:
    
    def __init__(self, app):
        
        self.app = app
        
    def run(self):
        
        #Define window setting
        self.root = tk.Toplevel()
        self.root.title('Add new product')
        self.root.configure(bg='#ffe4e1')
        self.root.grab_set() #Locking the interraction only for the popup
        
        screen_width = int(self.root.winfo_screenwidth()/4)
        screen_height = int(self.root.winfo_screenheight()/4)
        self.root.geometry(f"{screen_width}x{screen_height}")
        
        #Product name
        self.product_name_input = tk.Entry(self.root, bg="white")
        self.product_name_input.place(relx=0.05, rely=0.2, relw=0.9, relh=0.10)
        
        #Product Price
        self.product_price_input = tk.Entry(self.root, bg="white")
        self.product_price_input.place(relx=0.05, rely=0.4, relw=0.9, relh=0.10)
        
        #Product Quantity
        self.product_quantity_input = tk.Entry(self.root, bg="white")
        self.product_quantity_input.place(relx=0.05, rely=0.60, relw=0.9, relh=0.10)
        
        #Add button
        self.add_product_button = tk.Button(self.root, text="Add", command=self.app.add_product)
        self.add_product_button.place(relx=0.05, rely=0.8, relw=0.9, relh=0.15)
        
        self.root.mainloop()
     
    def close(self):
        
        self.root.destroy()
        self.root.update()