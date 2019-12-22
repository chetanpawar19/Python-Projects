from Desserts.IceCream.IceCream import *

class CandyBar(IceCream):
    def __init__(self, dessert_name='', dessert_price=0.0, icecream_unit=0, dessert_type=''):
        super().__init__(dessert_name, dessert_price, icecream_unit)
        self.dessert_type = dessert_type

    def disp(self):
        super().disp()
        print(self.dessert_type)

    def calculate_total(self):
        return self.dessert_name,self.icecream_unit, self.dessert_price * self.icecream_unit
