def display_available_items(dct):
    print("Available Items".center(50))
    print(f"{'S.No.':<10}{'Item':<15}{'Quantity':<15}{'Cost/Item':<15}")
    for index, product in dct.items():
        print(f"{index:<10}{product['Item']:<15}{product['Quantity']:<15}{product['Cost/Item']:<15}")

availableItems = {1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5}, 
2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35}, 
3: {'Item': 'Coffee', 'Quantity': 25, 'Cost/Item': 55},
4: {'Item': 'Chips', 'Quantity': 10, 'Cost/Item': 50},
5: {'Item': 'Cream', 'Quantity': 5, 'Cost/Item': 30}}

display_available_items(availableItems)

# User demand

customerName = input("Enter customer name : ")
address = input("Enter address : ")

userDemand = {}

while 1:
    item_name = input("Enter the item : ")
    if item_name == "":
        break
    else:
        quantity = int(input("Enter the quantity : "))
        userDemand[item_name] = quantity

bill = 0
usercart = availableItems.copy()

for user_p in userDemand:
    for index, product in availableItems.items():
        if user_p == product['Item']:
            if userDemand[user_p] <= product['Quantity']:
                tt = userDemand[user_p] * product['Cost/Item']
                bill += tt
                usercart['Quantity'] = userDemand[user_p]
                availableItems[index]['Quantity'] -= userDemand[user_p]
                usercart['Total Cost'] = tt
            else:
                print("Sorry, not enough quantity ! (You can enter again with lower amount)")
                usercart.pop(index)

# Generating Bill
            
print("Total Amount : ",bill)