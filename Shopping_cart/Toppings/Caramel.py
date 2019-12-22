from Toppings.Toppings import *

class Caramel(Toppings):
    def __init__(self, topping_name='', topping_price=0.0, topping_unit=0, topping_type=''):
        super().__init__(topping_name, topping_price)
        self.topping_type = topping_type
        self.topping_unit=topping_unit

    def disp(self):
        super().disp()
        print(self.topping_type)
        print(self.topping_unit)

    def calculate_total(self):
        return self.topping_name,self.topping_unit, self.topping_price * self.topping_unit

