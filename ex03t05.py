Bank = "---The best Bank---"
total = 1000
name = "Not set yet"
phone_number = "N\A"
balance = total
while True:
    print(Bank)
    print("1. Create an Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account")
    print("9. Exit") 
    choice = int(input("Enter a number:"))

    if choice == 1:
        name = input("Name: ")
        phone_number = int(input("Phone Number: "))
        balance = 0
        print(f"Name          :{name:>10}\n"
            f"Phone Number  :{phone_number:>10}\n"
            "Balance       :00")
        

    elif choice == 2:
        print(Bank)
        deposit = int(input("how much do you want to deposit "))
        balance += deposit
        print(f"Balance         :{balance:>10}")
        

    elif choice == 3:
        print(Bank)
        withdraw = int(input("how much do you want to withdraw"))
        balance -= withdraw
        print(f"Banlace.        :{balance:>10}\n")
        

    elif choice == 4:
        print(Bank)
        print(f"Name          :{name if name else 'N/A':>10}")
        print(f"Phone Number  :{phone_number if phone_number else 'N/A':>10}")
        print(f"Balance       :{balance:>10}")
        
    
    else:
        if choice == 9:
            break