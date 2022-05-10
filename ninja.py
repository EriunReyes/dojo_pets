from pets import Pet

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        
        
    def walk(self):
        self.pet.play()
        print(f'{self.first_name} Walking {self.pet.name}')
        return self
    
    def feed(self):
        self.pet.eat()
        print(f'{self.first_name} Feeding {self.pet.name}')
        return self
    
    def bathe(self):
        self.pet.noise()
        print(f'{self.first_name} Bathing {self.pet.name}')
        return self
    
    # John methods
    def walk(self):
        print(f'{self.first_name} Walking {self.pet.name}')
        return self
    
    def feed(self):
        print(f'{self.first_name} Feeding {self.pet.name}')
        return self
    
    def bathe(self):
        print(f'{self.first_name} Bathing {self.pet.name}')
        return self


pet2 = Pet('jinx', 'bulldog', 'backflip')
pet3 = Pet('ramos', 'pastor aleman', 'lie')
eriun = Ninja('eriun', 'Reyes', pet2, 'canies', 'Pedigree')
john = Ninja('John', 'jose', pet3, 'meat', 'cookies')
eriun.walk().feed().bathe()
pet2.play(health=10).sleep(energy=10).eat(health=5, energy=10)
eriun.pet.noise()
john.walk().feed().bathe()
john.pet.noise()


class Petss(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 5
        self.health = 10
        self.sound = 'hooou'
        
    def sleep(self, energy): 
        self.energy = energy + 25
        return self
    
    def play(self,health, energy):
        self.health = health + 50
        self.energy = energy - 5
        return self
    
    def eat(self, health, energy):
        self.energy = energy + 5
        self.health = health + 10
        return self
    
    def noise(self):
        print(self.sound)
        return self