class Bank:
    bank_name = "World Bank"
    
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(name)
        
b1 = Bank()
b1.change_bank_name("State Bank")