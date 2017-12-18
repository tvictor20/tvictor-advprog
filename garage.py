class Garage():
    def __init__(self):
        self.carsParked = 0
        self.carList = []

    def park(self, car):
        self.carList.append(car)

class Car():
    def __init__(self, owner, num):
        self.info = [num, owner]


garage = Garage()
num = 1
while True:
    owner = raw_input("Who owns the car?")
    car = Car(owner, num)
    parkyn = raw_input("Do you want to park the car? yes or no")
    if parkyn.lower() == "yes":
        garage.park(car.info)

    print garage.carList
    num += 1
