class Bank:
    loan_take_previously=True
    def application_for_loan(self):
        if (self.loan_take_previously==False):
            print("The loan is granted!")
        else:
            print("Loan is not granted!")
A=Bank()
B=Bank()
A.loan_take_previously=True
B.loan_take_previously=False
A.application_for_loan()
B.application_for_loan()