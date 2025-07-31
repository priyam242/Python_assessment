fruit_list = []  

while True:
    print("\t\tWelcome to fruit market")
    print("\t\t 1) Manger")
    print("\t\t 2) Customer")
    print("\t\t 3) Exit")
    num1 = int(input("select your role = "))

    if num1 == 1:
        while True:
            print("\t\tFruit Market Manger")
            print("\t\t 1) Add fruit stock")
            print("\t\t 2) View fruit stock")
            print("\t\t 3) Update fruit stock")
            print("\t\t 4) for Exit")
        
            num2 = int(input("Enter your choice = "))
            
            if num2 == 1:
                count = int(input("How many fruit you have enter = "))
                for i in range(count):
                    fruit = {} 
                    fruit['name'] = input(f"Enter {i+1} fruit name = ")
                    fruit['qty'] = int(input("Enter the Qty(in kg) = "))
                    fruit['price'] = int(input("Enter the price = "))
                    fruit_list.append(fruit)
                

                more = input("do you have perform more operations press y for yes n for no: ")
                if more.lower() != 'y':
                    break
                
            elif num2 == 2:
                if not fruit_list:
                    print("No fruit is added")
                else:
                    for i, fruit in enumerate(fruit_list, 1):
                        print(f"\nFruit {i}:")
                        print("Name:", fruit['name'])
                        print("Quantity:", fruit['qty'], "kg")
                        print("Price: ₹", fruit['price'])
            
            elif num2 == 3:
                if not fruit_list:
                    print("No fruit available to update")
                else:
                    for i, fruit in enumerate(fruit_list, 1):
                        print(f"{i}. {fruit['name']}")
                    
                    choice = int(input("Enter fruit number to update: ")) - 1
                    if 0 <= choice < len(fruit_list):
                        fruit_list[choice]['name'] = input(f"New name [{fruit_list[choice]['name']}]: ") or fruit_list[choice]['name']
                        fruit_list[choice]['qty'] = int(input(f"New Qty [{fruit_list[choice]['qty']}]: ") or fruit_list[choice]['qty'])
                        fruit_list[choice]['price'] = int(input(f"New Price [{fruit_list[choice]['price']}]: ") or fruit_list[choice]['price'])
                        print("Updated successfully!")
            
            elif num2 == 4:
                break

    elif num1 == 2:
        if not fruit_list:
            print("No fruits available")
        else:
            print("Available Fruits:")
            for i, fruit in enumerate(fruit_list, 1):
                print(f"{i}. {fruit['name']} ({fruit['qty']}kg)")
            
            choice = int(input("Enter fruit number to buy: ")) - 1
            if 0 <= choice < len(fruit_list):
                qty = int(input(f"Enter quantity (max {fruit_list[choice]['qty']}kg): "))
                if qty <= fruit_list[choice]['qty']:
                    total = qty * fruit_list[choice]['price']
                    fruit_list[choice]['qty'] -= qty
                    print(f"\nBill: {qty}kg {fruit_list[choice]['name']} = ₹{total}")
                else:
                    print("Not enough stock!")
            else:
                print("Invalid choice")

    elif num1 == 3:
     print("Thanks for visiting.")
     break