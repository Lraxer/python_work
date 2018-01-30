class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        "''返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        # 打印汽车里程数
        print("The car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        直接修改里程表读数
        禁止减少里程表读数
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表增加指定的量"""
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


my_new_car = Car('Audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
my_used_car = Car('subaru', 'outback', 2013)

print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(203)
my_used_car.increment_odometer(7)
my_used_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())