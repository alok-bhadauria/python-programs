class car:
    def __init__(self, maker, name, model, year, price):
        self.maker = maker
        self.name = name
        self.model = model
        self.year = year
        self.price = price
        self.available = True

    def display_car(self):
        return (f'''
Maker : {self.maker}
Car name : {self.name}
Model : {self.model}
Year : {self.year}
Price : {self.price}
''')

class dealership:
    def __init__(self, dealer_name):
        self.dealer_name = dealer_name
        self.inventory = []
    
    def add_car_to_inventory(self,car):
        self.inventory.append(car)
    
    def display_available_car(self):
        count = 1
        for car in self.inventory:
            if car.available:
                print(count,'>>>',end="")
                print(car.display_car())
                print('----------\n')
                count += 1

    def sell_car(self,c,index):
        if 0 < index < len(self.inventory) and self.inventory[index-1].available:
            c.purchase(self.inventory[index-1])
            return self.inventory[index-1]

class customer:
    def __init__(self, name):
        self.name = name
        self.purchased_car = []
    
    def purchase(self, car):
        self.purchased_car.append(car)
        car.available = False

# Main code
car1 = car('Koenigsegg','Gemera',50,2023,200000000)
car2 = car('Porsche','992 GT3 RS',200,2023,60000000)
car3 = car('BMW','M8',250,2019,30000000)
car4 = car('Mercedes Benz','Maybach GLS 600',280,2017,50000000)
car5 = car('Land Rover','Defender 110',240,2018,20000000)

d1 = dealership('AB MOTORS')
d1.add_car_to_inventory(car1)
d1.add_car_to_inventory(car2)
d1.add_car_to_inventory(car3)
d1.add_car_to_inventory(car4)
d1.add_car_to_inventory(car5)

d1.display_available_car()

c1 = customer(input("Enter customer name : "))
car_num = int(input("Enter car number : "))
ret = d1.sell_car(c1,car_num)
if ret:
    print(f' {c1.name} purchased car \n Details of purchased car : {ret.display_car()}')
else:
    print('Not available for selling')

print('\n After selling ... Available cars :')
d1.display_available_car()