class Vehicles:
  def __init__(self,brand,price):
    self.brand = brand
    self.price = price
  def show_details(self):
    print(self.brand)
    print(self.price)
class Bike(Vehicles):
  def __init__(self,brand,price,engine_cc):
    super().__init__(brand,price)
    self.engine_cc = engine_cc
  def show_details(self):
    print(self.brand)
    print(self.price)
    print(self.engine_cc)
class ElectricBike(Bike):
  def __init__(self,brand,price,engine_cc,battery_range):
    super().__init__(brand,price,engine_cc)
    self.battery_range = battery_range
  def show_details(self):
    print(self.brand)
    print(self.price)
    print(self.engine_cc)
    print(self.battery_range)
b1 = Bike("Bajaj", 95000, 250 )
e1 = ElectricBike("Aether", 85000, 0, 120)
print("Bike Details:")
b1.show_details()
print("Electric details")
e1.show_details()




