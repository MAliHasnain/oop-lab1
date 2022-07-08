class Car:
    sells=False
    def __init__(self,wheels,miles,make,model,year):
        self.wheels=wheels
        self.miles=miles
        self.make=make
        self.model=model
        self.year=year
    def sales_price(self):
        if (self.sells==True):
            print("sells on!")
            self.purchase_price()
        else:
            print("Sold out!")
    def purchase_price(self):
        print("30,000,000")
civic=Car("18 inches",200,"aluminium","2019","2020")
carola=Car("16 inches",120,"aluminim","2015","2018")
civic.sells=True
civic.sales_price()
carola.sales_price()
