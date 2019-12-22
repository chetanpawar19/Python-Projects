from Desserts.Desserts import *

class IceCream(Desserts):
    def __init__(self,dessert_name,dessert_price,icecream_unit):
        super().__init__(dessert_name,dessert_price)
        self.icecream_unit=icecream_unit
    def disp(self):
        super().disp()
        print(self.icecream_unit)
