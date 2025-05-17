from fpdf import FPDF

import customer as cr
import vendor as v
import product_row as it
#import item as it

class Invoice(FPDF):
    
    number = ""
    date = ""
    
    items = []
    
    paidDate = "" 
    
    info = ""
    
    def __init__(self, number, date, vendor, customer, product_rows=[]):
        
        ##############################-PDF init-##############################
        
        super().__init__()
        
        ##############################-Set Class Attributes-##############################
        
        self.vendor = vendor
        self.customer = customer
        self.number = number
        self.date = date
        self.product_rows = product_rows
        
    ##############################-Edit Invoice information-##############################
    
    def add_item(self, product_row):
        
        self.items.append([product_row.qty, product_row.name, product_row.uprice])
    
    ##############################-Exporting invoice into a pdf-##############################
    
    def format_PDF(self):
        
        ##############################-PDF page configuration-##############################
        
        #Configure pdf page
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        
        #Load font
        self.add_font("DejaVu", "", "../assets/DejaVuSans.ttf", uni=True)
        
        ##############################-Invoice title-##############################
        
        #Invoice title
        self.set_font("DejaVu", "", 16)
        self.cell(180, 10, "Facture", ln=True, align="C")
        
        self.ln(10)
        
        ##############################-Vendor and customer informations-##############################
        
        #Vendor and customer name
        self.set_font("DejaVu", "", 10)
        self.cell(90, 5, self.vendor.name, 0, align="L")
        self.cell(90, 5, self.customer.name, 0, align="R")
        
        self.ln()
        
        #Vendor and customer immatriculation
        self.cell(90, 5, f"{self.vendor.immatriculation}", 0, align="L")
        self.cell(90, 5, f"{self.customer.immatriculation}", 0, align="R")
        
        self.ln()
        
        #Vendor and customer street
        self.cell(90, 5, f"{self.vendor.address['street']}", 0, align="L")
        self.cell(90, 5, f"{self.customer.address['street']}", 0, align="R")
        
        self.ln()
        
        #Vendor and customer post code and city
        self.cell(90, 5, f"{self.vendor.address['postcode']}, {self.vendor.address['city']}", 0, align="L")
        self.cell(90, 5, f"{self.customer.address['postcode']}, {self.customer.address['city']}", 0, align="R")
        
        self.ln()
        
        #Vendor and customer Pphone
        self.cell(90, 5, f"{self.vendor.phone}", 0, align="L")
        
        self.ln(10)
        
        ##############################-Invoice identificater-##############################
        
        self.cell(180, 5, f"Facture n°{self.number}", ln=True, align="L")
        self.cell(180, 5, f"Date : {self.date}", ln=True, align="L")
        
        self.ln(h=10)
        
        ##############################-Item tab header-##############################
        
        self.set_font("DejaVu", "", 12)
        self.cell(10, 10, "Qty", 1, align="C")
        self.cell(100, 10, "Désignation", 1, align="L")
        self.cell(30, 10, "Prix", 1, align="C")
        self.cell(50, 10, "Total", 1, align="C")
        
        self.ln()
        
        ##############################-Add items to tab-##############################
        
        for row in self.product_rows:
            
            self.cell(10, 10, f"{row.qty}", 1, align="C")
            self.cell(100, 10, row.name, 1, align="L")
            self.cell(30, 10, f"{row.uprice} €", 1, align="R")
            self.cell(50, 10, f"{row.uprice*row.qty} €", 1, align="R")
        
            self.ln()
            
        self.ln(20)
        
        total = 0
        
        for row in self.product_rows:
            
            total += row.uprice*row.qty
            
        self.cell(190, 10, f"Total : {total} €", ln=True, align="R")
        
        if self.paidDate != "":
            
            self.cell(190, 10, f"Payé le: {self.paidDate}", ln=True, align="L")
        
        self.set_font("DejaVu", "", 8)
        self.cell(190, 10, self.info, ln=True, align="C")
        
    def export_PDF(self, name=""):

        self.format_PDF()
        
        if name == "":
            self.output(f"factures-{self.number}.pdf")
        else:
            self.output(name)
        
       