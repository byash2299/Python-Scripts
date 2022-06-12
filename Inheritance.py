
# Parent class Fighters taking email as argument in __init__ constructor

class Fighters():
    def __init__(self,email):
        self.email = email
        
    def sign_in(self):
        print(f'{self} logged in')

# Sub-Class Witch inheriting User
class Witch(Fighters):

    # One way to access Parent Class email field in sub-class

    def __init__(self, name, spell, email):

        # Call init method of Parent class in child class
        Fighters.__init__(self,email)
        self.name = name
        self.spell = spell
    
    def attack(self):
        print(f'Witch {self.name} has attacked with spell: {self.spell}')

# Sub-Class Wizard inheriting User
class Wizard(Fighters):

    def __init__(self, name, power,email):  
        
        # Use super keyword 
        super().__init__(email)                 # super refers to parent class
        self.name = name                        # there is no need to pass parent class object "self" while using super keyword
        self.power = power     
                                            
                                            
    def attack(self):
        print(f'Wizard {self.name} is about to attack with power: {self.power}')

# Multiple Inheritance
class HybridBorg(Wizard,Witch):
    def __init__(self, name, power,email):
        super().__init__(name, power,email)

hb1 = HybridBorg('Sumo','Pehalwan','123@email.com')
hb1.attack()

wizard1 = Wizard("Kaka", "Bad force")
witch1 = Witch('Sara','Magic Eye',"sara@gmail.com")


witch1.attack()
wizard1.attack()