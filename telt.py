class Car:
    def __init__(self, id, color, price, fuel):
        self.fuel = fuel
        self.id = id
        self.color = color
        self.price = price
    def run(self):
        print('car goes')
        while self.fuel:
            self.fuel -= 1
            print(self.fuel)
            if self.fuel == 0:
                self.throttle()
    def throttle(self):
        print('mbrrap (fuel empty)')
    def drive(self):
        if self.fuel != 0:
            self.run()
        else:
            self.throttle()


truck = Car(0, 'red.', 10000, 100)

truck.drive()