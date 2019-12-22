class Cart:
	"""Cart class allow to track cart item, subtotal and grandtotal"""
	
    @staticmethod
    def cart_value(cart_objects):
        cart_value = 0
        print('=================Cart Value==============')
        for obj in cart_objects:
            item_name,units, temp = obj.calculate_total()
            print('Item name: %-20s Units: %-5d Item subtotal: %-10f'%(item_name,units,temp))
            cart_value = cart_value + temp
        print('----------------------------------------')
        print('Total cart value=', cart_value)
        print('========================================')
    @staticmethod
    def clear_cart(cart_objects):
        cart_objects=list(cart_objects)
        return cart_objects.clear()