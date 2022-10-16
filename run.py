from curses import wrapper
from BankingATM.BankingTracsaction import ExchangeCurrency
from window import GUI
from Greeting.greeting import Greeting

def Running():
    exchange_currency = ExchangeCurrency()
    app = GUI()
    wrapper(Greeting)
    userOptionList = ["CONSOLE", "GUI", "FLASK"]
    while len(userOptionList) != 0:
        print("Welcome to SMART BANKING ATM")
        for i in range(len(userOptionList)):
            print(f"\t{i + 1}. {userOptionList[i]}")
        userOption = input("Please choose one option above:\n")
        while int(userOption) < 0 or int(userOption) > len(userOptionList):
            userOption = input("Oh no, u picked incorrectly or u already picked this option before, Please choose again:\n")
        option = userOptionList.pop(int(userOption) - 1)
        if option == "CONSOLE":
            exchange_currency.Console()
            print("Console")
        elif option == "GUI":
            app.Window()
            print("Gui")
        elif option == "FLASK":
            print("Flask")

        if len(userOptionList) == 0:
            break
        ask = input("Do it again?: ")
        if ask.lower() == "n":
            break