from fpdf import FPDF

import customer as cr
import vendor as v
import item as it

class Invoice:
    
    number = ""
    date = ""
    
    companyName = ""
    companyImmatriculation = ""
    companyAddress = {"street" : "", "city" : "", "postcode" : ""}
    
    companyPhone = "";
    
    customer = ""
    customerAddress = {"street" : "", "city" : "", "postcode" : ""}
    companyImmatriculation = ""
    
    items = []
    
    paidDate = "" 
    
    info = ""
    
    def __init__(self, number, date, vendor, customer):
        
        self.vendor = vendor
        self.customer = customer
        
    def add_item(self, name, price, qty):
        
        self.items.append([qty, it.item(name, price)])
    
    def export_PDF(self, name):

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        pdf.add_font("DejaVu", "", "../assets/DejaVuSans.ttf", uni=True)
        
        pdf.set_font("DejaVu", "", 16)
        pdf.cell(180, 10, "Facture", ln=True, align="C")
        pdf.ln(10)
        
        pdf.set_font("DejaVu", "", 10)
        pdf.cell(90, 5, self.vendor.name, 0, align="L")
        pdf.cell(90, 5, self.customer.name, 0, align="R")
        pdf.ln()
        pdf.cell(90, 5, f"{self.vendor.immatriculation}", 0, align="L")
        pdf.cell(90, 5, f"{self.customer.immatriculation}", 0, align="R")
        pdf.ln()
        pdf.cell(90, 5, f"{self.vendor.address['street']}", 0, align="L")
        pdf.cell(90, 5, f"{self.customer.address['street']}", 0, align="R")
        pdf.ln()
        pdf.cell(90, 5, f"{self.vendor.address['postcode']}, {self.vendor.address['city']}", 0, align="L")
        pdf.cell(90, 5, f"{self.customer.address['postcode']}, {self.vendor.address['city']}", 0, align="R")
        pdf.ln()
        pdf.cell(90, 5, f"{self.vendor.phone}", 0, align="L")
        pdf.ln(10)
        
        pdf.cell(180, 5, f"Facture n°{self.number}", ln=True, align="L")
        pdf.cell(180, 5, f"Date : {self.date}", ln=True, align="L")
        pdf.ln(10)
        
        pdf.set_font("DejaVu", "", 12)
        pdf.cell(10, 10, "Qty", 1, align="C")
        pdf.cell(100, 10, "Désignation", 1, align="L")
        pdf.cell(30, 10, "Prix", 1, align="C")
        pdf.cell(50, 10, "Total", 1, align="C")
        pdf.ln()
        
        for item in self.items:
            
            pdf.cell(10, 10, f"{item[0]}", 1, align="C")
            pdf.cell(100, 10, item[1].name, 1, align="L")
            pdf.cell(30, 10, f"{item[1].price} €", 1, align="R")
            pdf.cell(50, 10, f"{item[1].price*item[0]} €", 1, align="R")
            
        pdf.ln(20)
        
        total = 0
        for item in self.items:
            
            total += item[1].price*item[0]
            
        pdf.cell(190, 10, f"Total : {total} €", ln=True, align="R")
        
        if self.paidDate != "":
            
            pdf.cell(190, 10, f"Payé le: {self.paidDate}", ln=True, align="L")
        
        
        pdf.set_font("DejaVu", "", 8)
        pdf.cell(190, 10, self.info, ln=True, align="C")
        
        pdf.output(name)
        #pdf.output(f"factures-{self.number}.pdf")
        
    def __PDF_set_information():
        
        print("test")
       