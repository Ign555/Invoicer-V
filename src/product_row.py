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
* ProductRow Class
*
"""

class ProductRow:
    
    #Class public attributes
    qty = 0
    name = ""
    uprice = 0.0
    
    def __init__(self, qty, name, uprice):
        
        #Set attributes values
        self.qty = qty
        self.name = name
        self.uprice = uprice #Price for one unit