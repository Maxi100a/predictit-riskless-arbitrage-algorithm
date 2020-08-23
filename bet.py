class Bet:
    def __init__(self, id, yesSingle, noSingle, yesMax, noMax):
        self.id = id 
        self.yesSingle = yesSingle
        self.noSingle = noSingle
        
    def __str__(self):
        output = "market: " + id
        output += "\nYes profit"
        output += "\n\t single: " + str(self.yesSingle) + " \t max: " + str(self.yesMax)
        output += "\nNo profit"
        output += "\n\t single: " + str(self.noSingle) + " \t max: " + str(self.noMax)
        
        
        return output