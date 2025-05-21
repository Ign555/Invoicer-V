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

import os
import locale
import json

import vendor as v

"""
*
* Settings class
*
"""

class Settings:
    
    settings_json = {}
    
    def __init__(self):
        
        self.__load_settings()
       
    ##############################-Settings file management-##############################
    
    def __load_settings(self):
         
         #Check if customer file exist
         if os.path.exists("../settings.json") == False:
             
             with open("../settings.json", "w", newline="") as settings_file:
                 self.__set_vendor()
                 self.__set_currency()
                 self.__set_lang()
                 self.settings_json = json.dump(self.settings_json, settings_file)
             
         #load customer csv here
         with open("../settings.json") as settings_file:
            self.settings_json = json.load(settings_file)
    
         self.__extract_vendor()
        
    def __extract_vendor(self):
        
        vname = self.settings_json["vendor"]["name"]
        vimmatriculation = self.settings_json["vendor"]["immatriculation"]
        vaddr = self.settings_json["vendor"]["address"]
        vphone = self.settings_json["vendor"]["phone"]
        vmail = self.settings_json["vendor"]["email"]
        
        self.vendor = v.Vendor(vname, vimmatriculation, vaddr, vphone, vmail)
        
    def __set_vendor(self, vname="", vimm="", vaddr="", vphone="", vmail=""):
        
        vendor_json = {"name" : vname, "immatriculation" : vimm, "address" : vaddr, "phone" : vphone, "email" : vmail}
        self.settings_json.update({"vendor" : vendor_json})
    
    def __set_lang(self, lang=locale.getdefaultlocale()[0]):
        
        self.settings_json.update({"lang" : lang})
    
    def __set_currency(self, currency="$"):
        
        self.settings_json.update({"currency" : currency})

    def import_settings():
        print("import here")
        
    def export_settings():
        print("export here")
    
    