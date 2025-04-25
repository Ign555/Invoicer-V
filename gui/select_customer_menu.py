import tkinter as tk


class SelectCustomerWindow: 
    
    def __init__(self, app):
        print("creating")
      
        
    def run(self):

        self.root = tk.Toplevel()
        self.root.title('Select your customer')
        self.root.grab_set() #Locking the interraction only for the popup
        
        screen_width = int(self.root.winfo_screenwidth()/4)
        screen_height = int(self.root.winfo_screenheight()/4)
        self.root.geometry(f"{screen_width}x{screen_height}")
        
        #Define window setting
        self.root.title = "Select a customer"
        self.root.configure(bg='#ffe4e1')
        self.root.mainloop()
        
        #GUI
        
    
    def stop(self):
        
        self.root.destroy()