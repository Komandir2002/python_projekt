class Transport:
    def __init__(self, model, year, color):
        self.year = year
        self.model = model
        self.color = color


class Rocet(Transport):
    def __init__(self,model,year,color):
       super().__init__(model,year,color)



class Car:
    wheels = 4
    def __init__(self,model,year,color,penalties = 0.0):
        self.year = year
        self.model = model
        self.color = color
        self.penalties = penalties

    def drive(self,city):
        print(f'Car: {self.model} is driving to {city}')


mazda_car = Car('Mazda RX - 7',2021,'Red',100.5)
BMV = Car('BMV M - 3',2019,'Red',)

print(mazda_car) # адресс объекта

print(f'{mazda_car.model} {mazda_car.color} {mazda_car.year} {mazda_car.penalties} {mazda_car.wheels}')
mazda_car.color = "blue"
print(f'{mazda_car.model} {mazda_car.color} {mazda_car.year} {mazda_car.penalties} {mazda_car.wheels}')

BMV.drive('Tokio')
mazda_car.drive('Bishkek')
Car.wheels = 6
gmc_car = Car('gmc - 6',2006,'yelow',2900.5)
print(f'{gmc_car.model} {gmc_car.color} {gmc_car.year} {gmc_car.penalties} {gmc_car.wheels}')


class Person:
    def run(self):
        print('running')

person = Person()
person.run()