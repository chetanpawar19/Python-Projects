"""
Shopping cart - Main file shows menu options like product items, cart, exit.
Author - Chetan Pawar
"""

from Desserts.Cookies.Choco import *
from Desserts.Cookies.MixedCookies import *
from Utilities.Cart import *
from Desserts.IceCream.Sundae import *
from Desserts.IceCream.Chocobar import *
from Desserts.IceCream.CandyBar import *
from Toppings.Cherry import *
from Toppings.Caramel import *
from Toppings.PeanuteButter import *
from Toppings.Strawberry import *

cart=Cart()
cart_objects=[]

while True:
    print('------------  Menu  -------------------')
    print(' 1. Desserts 2. Toppings 3. Cart 4. Exit ')
    choice=int(input('Select your choice:'))

    if choice==1:
        print('Desserts: 1. Cookies 2. Ice Cream')
        dessert_choice=int(input('Which dessert do you want?'))

        if dessert_choice==1:
            print('Cookies: 1. Mixed Cookies 2. Choco Cookies')
            cookies_choice = int(input('Which cookes do you want?'))
            if cookies_choice==1:
                price=10
                unit=int(input('How many units(10 cookies pack) do you want? '))
                mixed_cookies_obj = MixedCookies('Mixed Cookies', price, unit, 'Cookies')
                cart_objects.append(mixed_cookies_obj)
            if cookies_choice==2:
                price=20
                unit = int(input('How many units(10 cookies pack) do you want?'))
                choco_cookies_obj = Choco('Choco Cookies', price, unit, 'Cookies')
                cart_objects.append(choco_cookies_obj)
        if dessert_choice==2:
            print('Ice-Cream 1. Chocobar 2. Sundae 3. Candybar')
            ice_cream_choice = int(input('Which ice-cream do you want?'))
            if ice_cream_choice==1:
                price=30
                unit = int(input('How many units do you want? '))
                chocobar_obj = Chocobar('Chocobar', price, unit, 'Ice-Cream')
                cart_objects.append(chocobar_obj)
            if ice_cream_choice==2:
                price = 20
                unit = int(input('How many units do you want?'))
                sundae_obj = Sundae('Sundae', price, unit, 'Ice-Cream')
                cart_objects.append(sundae_obj)
            if ice_cream_choice == 3:
                price = 40
                unit = int(input('How many units do you want?'))
                candybar_obj = CandyBar('Candybar', price, unit, 'Ice-Cream')
                cart_objects.append(candybar_obj)
    elif choice==2:
        print('Toppings 1. Cherry 2. Caramel 3. Peanute Butter 4. Strawberry')
        toppings_choice = int(input('Which toppings do you want?'))
        if toppings_choice == 1:
            price = 0.5 #per grams
            unit = int(input('How many grams do you want?'))
            cherry_obj = Cherry('Cherry', price, unit, 'Toppings')
            cart_objects.append(cherry_obj)
        if toppings_choice == 2:
            price = 0.5 #per grams
            unit = int(input('How many grams do you want?'))
            caramel_obj = Caramel('Caramel', price, unit, 'Toppings')
            cart_objects.append(caramel_obj)
        if toppings_choice == 3:
            price = 0.5 #per grams
            unit = int(input('How many grams do you want?'))
            peanutebutter_obj = PeanuteButter('Peanute Butter', price, unit, 'Toppings')
            cart_objects.append(peanutebutter_obj)
        if toppings_choice == 4:
            price = 0.5 #per grams
            unit = int(input('How many grams do you want?'))
            strawberry_obj = Strawberry('Strawberry', price, unit, 'Toppings')
            cart_objects.append(strawberry_obj)

    elif choice==3:
        print('------------------Cart--------------------')
        print('1. Show cart value 2. Clear Cart')
        cart_choice=int(input('Select Cart choice:'))
        if cart_choice==1:
            cart.cart_value(cart_objects)
        if cart_choice==2:
            cart_objects=cart.clear_cart(cart_objects)
            print('Cart Cleared!',cart_objects)
    elif choice==4:
        break

    else:
        print('Select at least one choice!')
