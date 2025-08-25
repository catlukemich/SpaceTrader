import assets
import random

MAN, WOMAN = "man", "woman"

names_man = assets.loadNames("assets/names_man.txt")
names_woman = assets.loadNames("assets/names_woman.txt")

def pickRandomName(gender = MAN):
    names = names_man
    if gender == WOMAN:
        names = names_woman
    choice_results = random.choices(names[0], weights = names[1], k = 1)
    return choice_results[0]
        

class AITrader:
    ''' Trader is a computer controlled player that works on beside of the player '''    
    
    def __init__(self):
        self.gender = random.choice([MAN, WOMAN])
        self.name = pickRandomName(self.gender)
        self.carrier = None
        
        self.inteligence = 90 # In range 0 - 100 - defines how well related to the knowledge the trader will perform right decisions regarding the foreseen profit
        self.dynamic = 50 # In range 0 - 100 - defines how good of a pilot the trader is
        self.communicativity = 50 # In range 0 - 100 - defines how often the pilot will provide (initiate) a feedback related to his duties
        self.experience = 50 # In range 0 - 100 - a global factor related to how often the trader will perform randomnly inaccurate decisions, fail withon dynamics consistency and forget to report his actions (above 3 factors)
        
        
        
        
