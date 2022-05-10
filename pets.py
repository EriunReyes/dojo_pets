class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 0
        self.health = 0
        self.sound = 'Hoou'
        
    def sleep(self, energy): 
        self.energy = energy + 25
        return self
    
    def play(self,health):
        self.health = health + 5
        return self
    
    def eat(self, health, energy):
        self.energy = energy + 5
        self.health = health + 10
        return self
    
    def noise(self):
        print(self.sound)
        return self
        


# This is my result based on what I thought. If anything should be correct. please let me know so I can improve my coding responsabilities.



