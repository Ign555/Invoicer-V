import tkinter as tk


class SelectCustomerWindow: 
    
    def __init__(self, app):
        print("creating")
      
        
    def run(self):
        self.root = tk.Tk()
        self.root.title('Select your customer')
        
        #Define window setting
        self.root.title = "Select a customer"
        self.root.configure(bg='white')
        self.root.mainloop()
    
    def stop(self):
        
        self.root.destroy()