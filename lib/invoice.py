from fpdf import FPDF

if __name__ == "__main__":
    import item as it
else:
    import lib.item as it

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
    
    def __init__(self, number, date, companyName, companyImmatriculation, companyAddress, companyPhone, customer, customerAddress, customerImmatriculation=""):
        
        self.number = number
        self.date = date
        
        self.companyName = companyName
        self.companyImmatriculation = companyImmatriculation
        self.companyAddress = companyAddress
        self.companyPhone = companyPhone
       
        self.customer = customer
        self.customerAddress = customerAddress
        self.customerImmatriculation = customerImmatriculation
        
    def addItem(self, name, price, qty):
        
        self.items.append([qty, it.item(name, price)])
    
    def exportPDF(self):
        
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.add_font('DejaVu', '', 'assets/DejaVuSans.ttf', uni=True)
        
        pdf.set_font("Arial", "B", 16)
        pdf.cell(180, 10, "Facture", ln=True, align="C")
        pdf.ln(10)
        
        pdf.set_font("DejaVu", "", 10)
        pdf.cell(90, 5, self.companyName, 0, align="L")
        pdf.cell(90, 5, self.customer, 0, align="R")
        pdf.ln()
        pdf.cell(90, 5, f"{self.companyImmatriculation}", 0, align="L")
        pdf.cell(90, 5, f"{self.customerImmatriculation}", 0, align="R")
        pdf.ln()
        pdf.cell(90, 5, f"{self.companyAddress['street']}", 0, align="L")
        pdf.cell(90, 5, f"{self.customerAddress['street']}", 0, align="R")
        pdf.ln()
        pdf.cell(90, 5, f"{self.companyAddress['postcode']}, {self.companyAddress['city']}", 0, align="L")
        pdf.cell(90, 5, f"{self.customerAddress['postcode']}, {self.customerAddress['city']}", 0, align="R")
        pdf.ln()
        pdf.cell(90, 5, f"{self.companyPhone}", 0, align="L")
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
        
        pdf.output(f"factures-{self.number}.pdf")
        
        
       