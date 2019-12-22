from Desserts.Cookies.Cookies import *

class Choco(Cookies):
    def __init__(self, dessert_name='', dessert_price=0.0, cookies_unit=0, dessert_type=''):
        super().__init__(dessert_name, dessert_price, cookies_unit)
        self.dessert_type = dessert_type

    def disp(self):
        super().disp()
        print(self.dessert_type)

    def calculate_total(self):
        return self.dessert_name,self.cookies_unit, self.dessert_price * self.cookies_unit
