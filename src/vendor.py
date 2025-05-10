# -*- coding: utf-8 -*-
"""
Created on Sat May 10 13:49:33 2025

@author: netwo
"""
class Vendor:
    
    name = ""
    address = {"street" : "", "city" : "", "postcode" : ""}
    immatriculation = ""
    phone = ""
    mail = ""
        
    def __init__(self, vendor_name="", vendor_address="", vendor_immatriculation="", vendor_phone="", vendor_mail=""):
        
        self.name = vendor_name
        if(vendor_address != ""): self.address = vendor_address
        self.immatriculation = vendor_immatriculation
        self.phone = vendor_phone
        self.mail = vendor_mail
        
        if self.name == "":
            self.is_defined = False
        else:
            self.is_defined = True
    
    
