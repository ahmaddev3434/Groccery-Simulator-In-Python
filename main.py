cart = []
# Create a list of 5 plus fruits items
fruits = ['apple', 'banana', 'mango', 'orange', 'grapes']
fruits_price = [150, 50, 100, 80, 120]  
# Electronics
electronics = ['mobile charger', 'headphones', 'power bank', 'LED bulb', 'USB cable']
electronics_price = [300, 150, 500, 200, 100]
# Groccery
general_grocery = [
    'flour ', 'rice', 'sugar', 'salt', 'cooking oil',
    'tea', 'daal ', 'toilet paper', 'detergent', 'biscuits'
]
general_grocery_price = [40, 60, 30, 20, 150, 100, 80, 50, 70, 90]
# Makeup
makeup_beauty = ['face wash', 'lipstick', 'shampoo', 'nail polish', 'moisturizer']
makeup_beauty_price = [200, 300, 250, 150, 400]
# Food
food_items = ['burger', 'pizza', 'sandwich', 'fries', 'ice cream']
food_items_price = [200, 300, 150, 100, 250]
while (True) :
    print("<<<<<<<<<<<<<<<<<<<< Welcome to Mega Mart >>>>>>>>>>>>>>>>>>>>>>>>")
    print("1. Fruits")
    print("2. Electronics")
    print("3. Grocery")
    print("4. Makeup and Beauty")
    print("5. Food")
    print("6. Billing Center")
    print("7. Exit")
    c1 = int(input("Enter your choice: "))
    if (c1 == 1) :
        print("Fruits available in Mega Mart are : ")
        print(fruits)
        c2 = int(input("Enter the number of the fruit you want to buy (0-4) : "))
        cart.append(fruits[c2])
    elif (c1 == 2) :
        print("Electronics available in Mega Mart are :  ")
        print(electronics)
        c3 = int(input("Enter the number of the item you want to buy (0-4) :"))
        cart.append(electronics[c3])
    elif (c1 == 3) :
        print("Grocery Available in Mega Mart are : ")
        print(general_grocery)
        c4 = int(input("Enter the number of the item you want to buy (0-9) :"))
        cart.append(general_grocery[c4])
    elif (c1 == 4) :
        print("Makeup and Beauty Available in Mega Mart are : ")
        print(makeup_beauty)
        c5 = int(input("Enter the number of the item you want to buy (0-4) :"))
        cart.append(makeup_beauty[c5])
    elif (c1 == 5) :
        print("Food Available in Mega Mart is : ")
        print(food_items)
        c6 = int(input("Enter the number of the item you want to buy (0-4) :"))
        cart.append(food_items[c6])
    elif (c1 == 7) :
        print("Thankyou For Visting Mega Mart ")
        break
    elif (c1 == 6) :
        print("Welcome To The billing center ")
        print("The items in Your Cart are : ")
        print(cart)
        total = 0
        for item in cart :
            if item in fruits :
                total = total + fruits_price[fruits.index(item)]
            elif item in electronics :
                total = total + electronics_price[electronics.index(item)]
            elif item in general_grocery :
                total = total + general_grocery_price[general_grocery.index(item)]
            elif item in makeup_beauty :
                total = total + makeup_beauty_price[makeup_beauty.index(item)]
            elif item in food_items :
                total = total + food_items_price[food_items.index(item)]
                print(f"Your Total Bill is : {total}")
                if (total > 700) :
                    discount = total * 0.1
                    print(f"Congratulations! You got a discount of 10%: {discount}")
                    total = total - discount
                print(f"Your Final Bill is : {total}")
                
               
                
        
                
        

    
