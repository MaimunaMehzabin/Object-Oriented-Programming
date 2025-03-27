class Dog:
    
    species = "animal"
    
    def __init__(self, name, age, breed, energyLevel, sociability, color, earType, intelligence):
        self.name = name
        self.age = age
        self.breed = breed
        self.energylevel = energyLevel
        self.sociability = sociability
        self.color = color
        self.earType = earType
        self.intelligence = intelligence
        
nova = Dog ("Nova", 10, "pomeranian", "hyperactive", "friendly", "white", "pointed", "highly trained")


print(f"Nova is an {nova.species}")
print(f"She's {nova.age} years old\n")
print(f"She's a {nova.breed}")
print(f"She's very {nova.energylevel}\n")
print(f"But also very {nova.sociability}")
print(f"She's a beautiful {nova.color} color\n")
print(f"Her ears are {nova.earType}")
print(f"Nova is {nova.intelligence}") 
