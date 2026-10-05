
def show_Balance(balance):
    print("**********************")
    print(f"your balance is ${balance: .2f}")
    print("**********************")

def deposit():
    print("*********************")
    amount=float(input("Enter an amount to be deposited:" ))
    print("**********************")
    if amount < 0:
        print("*******************")
        print("thats not a valid amount ")
        print("*******************")
        return 0
    else:
        return amount


def withdraw(balance):
    amount=float(input("Enter an amount to be withdraw: "))
    
    if amount > balance:
        print("insufficient balance! ")
        return 0
    elif amount < 0:
        print("amount must be greater than 0")
        return 0
    else:
        return amount
def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking program: ")
        print("1. Show Balance ")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("********************")
        choice=input("Enter your choice (1-4): ")



        if choice == '1':
            show_Balance(balance)
        elif choice == '2':
            balance+=deposit()
        elif choice == '3':
            balance-=withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*************")
            print("thats not a valid choice")
            print("*************")


    print("Have a nice day!")

if __name__ == '__main__':
    main()


    