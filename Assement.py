fruit_list = []  

def add(): # add function for the add new fruit in the list 
    count=0
    count = int(input("How many fruit you have enter = "))
    for i in range(count):
        fruit = {} 
        fruit['name'] = input(f"Enter {i+1} fruit name = ")      # add fruit name 
        fruit['qty'] = int(input("Enter the Qty(in kg) = "))    # add fruit Quanitity 
        fruit['price'] = int(input("Enter the price = "))      # ADD PRICE OF THE FRUIT
        fruit_list.append(fruit)        # append function for the add last fruit (name,price,quantity)
        more = input("do you have perform more operations press y for yes n for no: ")  # ask the operation one more time 
        if more.lower() != 'y':      # if the user enter n (NO) then break stat will be excuted
         break
                
def update():
    for i, fruit in enumerate(fruit_list, 1):
                        print(f"{i}. {fruit['name']}")    # this is print the present fruits
                    
    # Get user input for fruit selection 
choice = int(input("Enter fruit number to update: ")) - 1      
if 0 <= choice < len(fruit_list):
    # Update the fruit name - show current fruit name
    fruit_list[choice]['name'] = input(f"New name [{fruit_list[choice]['name']}]: ") or fruit_list[choice]['name'] 
    # Update the quantity 
    fruit_list[choice]['qty'] = int(input(f"New Qty [{fruit_list[choice]['qty']}]: ") or fruit_list[choice]['qty'])
    # Update the price 
    fruit_list[choice]['price'] = int(input(f"New Price [{fruit_list[choice]['price']}]: ") or fruit_list[choice]['price'])
    # Confirm the update was successful
    print("Updated successfully!")
    
def choice2():
    if 0 <= choice < len(fruit_list):
                # Get the quantity from user input, showing maximum available quantity
                qty = int(input(f"Enter quantity (max {fruit_list[choice]['qty']}kg): "))
                    # Inform user if requested quantity exceeds available stock
                if qty <= fruit_list[choice]['qty']:
                        # Display the purchase bill to the user
                    total = qty * fruit_list[choice]['price']
                        # Update the inventory by subtracting the purchased quantity
                    fruit_list[choice]['qty'] -= qty
                    print(f"\nBill: {qty}kg {fruit_list[choice]['name']} = ₹{total}")
                else:
                    print("Not enough stock!")
    else:
                print("Invalid choice")
    
while True:
    print("\t\tWelcome to fruit market")
    print("\t\t 1) Manger")
    print("\t\t 2) Customer")
    print("\t\t 3) Exit")
    num = int(input("select your role = "))
    
    match(num):
        case 1:
         while True:
            print("\t\tFruit Market Manger")
            print("\t\t 1) Add fruit stock")
            print("\t\t 2) View fruit stock")
            print("\t\t 3) Update fruit stock")
            print("\t\t 4) for Exit")
        
            num2 = int(input("Enter your choice = "))
            
            match(num2):
               case 1:
                  add()
               case 2:
                if not fruit_list:
                    print("No fruit is added")
                else:
                    for i, fruit in enumerate(fruit_list, 1):
                        print(f"\nFruit {i}:")
                        print("Name:", fruit['name'])
                        print("Quantity:", fruit['qty'], "kg")
                        print("Price: ₹", fruit['price'])
               case 3:
                if not fruit_list:
                    print("No fruit available to update")
                else:
                   update()
                       
               case 4:
                  break

        case 2:
         if not fruit_list:
            print("No fruits available")
         else:
            print("Available Fruits:")      # print the available fruits
            for i, fruit in enumerate(fruit_list, 1):
                print(f"{i}. {fruit['name']} ({fruit['qty']}kg)")
            
            choice = int(input("Enter fruit number to buy: ")) - 1
            choice2()
        case 3:
          print("Thanks for the Visiting")
        case _:
         print("You have entered wrong number.")