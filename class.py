class Account:
    def __init__(self,id,name,amount):
        self.account_id=id
        self.account_name=name
        self.account_amount=amount
    def get_email(self,email):
        self.email=email
        
        
a1=Account(101,'rahul',5000)
a2=Account(102,'soniya',6000)

print(a1.__dict__)
print(a2.__dict__)