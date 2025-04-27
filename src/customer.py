class Customer:
    
    name = ""
    address = ""
    immatriculation = ""
    phone = ""
    mail = ""
        
    def __init__(self, customer_name="", customer_address="", customer_immatriculation=""):
        
        self.name = customer_name
        self.address = customer_address
        self.immatriculation = customer_immatriculation
        
        if self.name == "":
            self.is_defined = False
        else:
            self.is_defined = True
    
    