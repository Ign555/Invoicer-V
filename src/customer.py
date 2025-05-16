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
* Customer Class
*
"""

class Customer:
    
    #Class public attributes
    name = ""
    immatriculation = ""
    address = {"street" : "", "city" : "", "postcode" : ""}
    phone = ""
    mail = ""
        
    def __init__(self, cname="", caddress="", cimmatriculation="", cphone="", cmail=""):
        
        #Set attributes values
        self.name = cname
        self.immatriculation = cimmatriculation
        if(type(caddress) == dict): self.address = caddress #Address should be a dictionary 
        self.phone = cphone
        self.mail = cmail
        
        #Determine if the vendor is defined in settings or not
        if self.name == "":
            self.is_defined = False
        else:
            self.is_defined = True
    
    