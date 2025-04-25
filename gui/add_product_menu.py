


class AddProductMenu:
    
    def __init__(self, app):
        
        self.app = app
        
    def run(self):
        
        self.root = tk.Toplevel()
        self.root.title('Add new product')
        self.root.grab_set() #Locking the interraction only for the popup
        
        screen_width = int(self.root.winfo_screenwidth()/4)
        screen_height = int(self.root.winfo_screenheight()/4)
        self.root.geometry(f"{screen_width}x{screen_height}")
        
        #Define window setting
        self.root.title = "Select a customer"
        self.root.configure(bg='#ffe4e1')
        self.root.mainloop()