import random

class StealingGame:
    def __init__(self):
        self.balance = 0
        self.is_running = True
        self.steal_tries = 3

    def deposit(self):
        try:
            amount = int(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT: "))
            if amount > 0:
                self.balance += amount
                print(f"${amount:.2f} has been deposited 💵")
            else:
                print("Invalid amount")
        except ValueError:
            print("Invalid input, please enter a number")

    def withdraw(self):
        try:
            amount = int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW: "))
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"${amount:.2f} has been withdrawn")
            else:
                print("INVALID: INSUFFICIENT FUNDS")
        except ValueError:
            print("Invalid input, please enter a number")

    def check_banks(self):
        input("CLICK ON ENTER TO CHECK BANKS FOR MONEY TO STEAL: ")
        amount_available = random.randint(100000, 300000)
        print(f"${amount_available} money is available to steal")

    def steal_bank(self):
        if self.steal_tries <= 0:
            print("You have no more attempts left. You got caught and lost.")
            self.balance -= 5000
            return

        input("TRY TO STEAL click on enter to steal: ")
        stolen_amount = random.randint(-7000, 15000)
        if stolen_amount < 0:
            print(f"You got caught and lost ${-stolen_amount}.")
        else:
            print(f"${stolen_amount} is stolen")
        self.balance += stolen_amount
        self.steal_tries -= 1

    def show_balance(self):
        print(f"${self.balance} YOUR BALANCE: ")

    def start_game(self):
        while self.is_running:
            print("\n1. DEPOSIT")
            print("2. WITHDRAW")
            print("3. CHECK BANKS")
            print("4. STEAL BANK")
            print("5. EXIT")
            print("6. SHOW BALANCE")
            choice = input("WELCOME, choose an option to start the game: ")

            if choice == "1":
                self.deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.check_banks()
            elif choice == "4":
                self.steal_bank()
            elif choice == "5":
                self.is_running = False
            elif choice == "6":
                self.show_balance()
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    game = StealingGame()
    game.start_game()