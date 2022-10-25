"""create two shopping cart for two friends
compare their cart and see what they have in common
add 1 item to one cart
remove item from the other cart"""
import functools
print("Cart #1 products:")
cart_1 = ["chicken", "chocolate", "sausages", "milk","cookies"]
print(cart_1)
print("Cart #2 products:")
cart_2 = ["milk", "sausages", "chocolate", "chicken","cookies", "wine"]
print(cart_2)
if cart_1 == cart_2:
    print("This carts have same products")
    common_products = set(cart_1) & set(cart_2)
    print(f"Common items:", common_products)
else:
    print("This carts have different products")
    print("-"*30)
    common_products = set(cart_1) & set(cart_2)
    print(f"Common items:", common_products)
cart_1.sort()
cart_2.sort()
print("Sorting Cart #1 and Cart #2 items in  alphabetical order")
print(cart_1)
print(cart_2)
print("-"*30)
add_items=input("Do you want add new product to any of this cart's yes/no? ")
if add_items == "yes":
    what_cart = input("To what cart do you want add new product. Please enter number '1' = Cart #1 or '2' = Cart #2 ?")
    if what_cart == "1":
        new_item1 = input("Please enter new product for cart 1:")
        cart_1.append(new_item1)
        print(cart_1)
    else:
        what_cart == "no"
        new_item2 = input("Please enter new product for cart 2: ")
        cart_2.append(new_item2)
        print(cart_2)
else:
    add_items == "no"
    print("-"*30)
delete_item=input("Do you want remove any product from Cart #1 or Cart #2, yes/no? ")
if delete_item == "yes":
    delete_cart=input("Choose from what cart you want delete product. Please enter number '1' or '2'? ")
    if delete_cart == "1":
        print("Current Cart #1 products")
        print(cart_1)
        delete_cart1=input("What product do you want remove from cart1? ")
        print("-" * 30)
        cart_1.remove(delete_cart1)
        print("Cart #1 after removing product")
        print(cart_1)
    else:
        delete_cart == "2"
        print("Current Cart #2 products")
        print(cart_2)
        delete_cart2 = input("What product do you want remove from cart2? ")
        print("-" * 30)
        cart_2.remove(delete_cart2)
        print("Cart #2 after removing product")
        print(cart_2)
else:
    print("Ok, have a good day!")