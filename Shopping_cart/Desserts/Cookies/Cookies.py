from Desserts.Desserts import *

class Cookies(Desserts):
    def __init__(self,dessert_name,dessert_price,cookies_unit):
        super().__init__(dessert_name,dessert_price)
        self.cookies_unit=cookies_unit
    def disp(self):
        super().disp()
        print(self.cookies_unit)
