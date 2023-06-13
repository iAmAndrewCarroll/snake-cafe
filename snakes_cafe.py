# Task 1: Print an intro message and the restaurant menu
print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **

** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

""")

x = 0
old_order = {}

# Prompt the user for an order
while True:
    order = input("""
***********************************
** What would you like to order? **
***********************************
>
""")
    if order == "quit":
        break
    if order not in old_order:
        old_order[order] = 1
        print(f"1 order of {order} has been added to your meal")
    else:
        old_order[order] += 1
        print(f"{old_order[order]} orders of {order} have been added to your meal")
