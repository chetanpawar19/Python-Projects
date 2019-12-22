
class Desserts:
	"""Desserts class provides dessert attribute like name, price"""
    def __init__(self,dessert_name,dessert_price):
        self.dessert_name=dessert_name
        self.dessert_price=dessert_price
    def disp(self):
        print(self.dessert_name)
        print(self.dessert_price)

