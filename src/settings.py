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
                 settings_json = json.dump("", settings_file)
             
         else:
             
             #load customer csv here
             with open("../settings.json") as settings_file:
                 settings_json = json.load(settings_file)
                 self.__extract_vendor(settings_json)
        
    def __extract_vendor(self, settings_json):
        
        vname = settings_json["vendor"]["name"];
        vimmatriculation = settings_json["vendor"]["immatriculation"];
        vaddr = settings_json["vendor"]["address"];
        vphone = settings_json["vendor"]["phone"];
        vmail = settings_json["vendor"]["email"];
        
        self.vendor = v.Vendor(vname, vimmatriculation, vaddr, vphone, vmail)
        
            
    def import_settings():
        print("import here")
        
    def export_settings():
        print("export here")
    
    