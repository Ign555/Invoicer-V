import os
import json

import vendor as v

class Settings:
    
    def __init__(self):
        
        self.__load_settings()
       
    ##############################-Settings file management-##############################
    
    def __load_settings(self):
         
         #Check if customer file exist
         if os.path.exists("../settings.json") == False:
             
             with open("../settings.json", "w", newline="") as settings_file:
                 self.__set_vendor("", "", "", "", "")
                 self.settings_json = json.dump(self.settings_json, settings_file)
             
         else:
             
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
        
    def __set_vendor(self, vname, vimm, vaddr, vphone, vmail):
        
        vendor_json = {"name" : vname, "immatriculation" : vimm, "address" : vaddr, "phone" : vphone, "email" : vmail}
        self.settings_json = {"vendor" : vendor_json}

    def import_settings():
        print("import here")
        
    def export_settings():
        print("export here")
    
    