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

"""
*
* Vendor Class
*
"""

class Vendor:
    
    #Class public attributes 
    name = ""
    immatriculation = ""
    address = {"street" : "", "city" : "", "postcode" : ""}
    phone = ""
    mail = ""
        
    def __init__(self, vname="", vaddress="", vimmatriculation="", vphone="", vmail=""):
        
        #Set attributes values
        self.name = vname
        self.immatriculation = vimmatriculation
        if(type(vaddress) == dict): self.address = vaddress #Address should be a dictionary 
        self.phone = vphone
        self.mail = vmail
        
        #Determine if the vendor is defined in settings or not
        if self.name == "":
            self.is_defined = False
        else:
            self.is_defined = True
    
    
