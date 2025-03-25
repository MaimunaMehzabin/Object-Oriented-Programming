class student:
    
    grade = 7
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
abir = student("Abir", 14, "5 Feet 5 Inches")
maimuna = student("Maimuna", 12, "5 Feet 0 Inches")

print(f"Abir's Grade : {abir.grade}")
print(f"Maimuna's Grade : {maimuna.grade}")
print()

print(f"Abir's Name : {abir.name} \nAbir's Age : {abir.age} \nand Abir's Height: {abir.height} ")
print()
print(f"Maimuna's Name : {maimuna.name} \nMaimuna's Age : {maimuna.age} \nand Maimuna's Height: {maimuna.height} ")