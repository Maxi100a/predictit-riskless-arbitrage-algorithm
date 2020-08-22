class Bet:
    def __init__(self, name, yes, no):
        self.name = name 
        self.yes = yes
        self.no = no
        
    def __str__(self):
        return self.name + " best yes: " + str(self.yes) + " best no: " + str(self.no) 