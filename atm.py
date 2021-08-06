class Atm(object):
    def __init__(self,name,pin,):
        self.name=name
        self.pin=pin
        
    def info(self):
        print("Account name is : "+self.name)
        print("card pin is  : "+self.pin)
       
Atm1=Atm("Avaneesh Sawant","2364")
Atm2=Atm("Sanjana Sawant","3018")
Atm1.info()


    