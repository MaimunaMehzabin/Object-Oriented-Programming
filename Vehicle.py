class Vehicle:
    
    def __init__(self, maxSpeed, mileage):
        self.maxSpeed = maxSpeed
        self.mileage = mileage
        
ferrari = Vehicle(260, 18)
lamborghini = Vehicle(285, 28)
tataNano = Vehicle(110, 80)

print(f"Ferrari max speed: {ferrari.maxSpeed}")
print(f"Ferrari mileage: {ferrari.mileage}\n")

print(f"Lamborghini max speed: {lamborghini.maxSpeed}")
print(f"Lamborghini mileage: {lamborghini.mileage}\n")

print(f"Tata Nano max speed: {tataNano.maxSpeed}")
print(f"Tata Nano mileage: {tataNano.mileage}")