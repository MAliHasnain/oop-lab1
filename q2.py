class Complex_number:
    def input(self,x,y):
        self.x=x
        self.y=y
    def print(self):
        print(f'{self.x}+{self.y}j')
num1=Complex_number()
num2=Complex_number()
num1.input(1,2)
num2.input(3,4)
num1.print()
num2.print()