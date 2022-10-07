class MyFileHandling(object):

    def __init__(self):
        from datetime import datetime
        self.today = datetime.today()
        self.day = self.today.strftime("%d/%m/%Y")

    def openFile(self, pin):
        users_file = open("./users/user.txt", "a+")
        users_file.seek(0)
        users = {}
        for user in users_file:
            splitUser = user[:-1].split(":")
            users[splitUser[0]] = splitUser[1]
        try:
            return open("./users/" + users[pin], "r+"), users[pin].split(".")[0]
        except:
            print("Doesn't have this User, Please check again")
            isCreated = input("Or you can create an account (Y/N): ")
            if isCreated.upper() == "Y":
                userAccount = input("Input new PIN or keep the old ones (N/O): ") # N is new, O is old
                if userAccount.upper() == "N":
                    userAccount = input("Input new PIN: ")
                    pin = userAccount
                else:
                    userAccount = pin

                nameAccount = input("Enter your full name: ")
                moneyAccount = input("Money which u deposit: ")
                fileExtension = "user" + str(len(users))  + ".txt"
                f = open("./users/" + fileExtension, "w")
                f.write("Full Name: " + nameAccount.upper() + "\n")
                users_file.write(userAccount  + ":" + fileExtension + "\n")
                f.write("CurrentAmount: " + moneyAccount)
                users[userAccount] = fileExtension
                f.close()
                print("Created successfully!!!")
                return open("./users/" + users[pin], "r+"), users[pin].split(".")[0]
        finally:
            users_file.close()
    
    # Get userName, currentAmount
    def getCurrentAmount(self, file):
        currentAmount = ""
        userName = ""
        for each in file:
            if "\n" in each:
                print(each[:-1])
                userName = each[10:len(userName) - 1]
            else:
                print(each)
                currentAmount = each[15:]
        return userName, currentAmount
    
    # This function have fewer constrant range from 0 to 1 billiion & integer value 
    def EditFile(self, file, userName, value):
        str_value = str(value)
        res = []
        count = 0
        for i in str_value[::-1]:
            if count == 3:
                res.append(",")
                res.append(i)
                count = 1
            else:
                res.append(i)
                count += 1
        resStr = "".join(res[::-1])
        file.seek(0)
        file.write("Full Name:" + userName + "\n")
        file.write("CurrentAmount: " + resStr)
        file.truncate()
        file.close()
    
    def filterAmount(self, currentAmount, userInput):
        return int(currentAmount.replace(",", "")), int(userInput.replace(",", ""))
    
    def Check(self, currentAmount, userInput):
        if currentAmount < userInput:
            return False
        return True

    def Loading(self):
        from time import sleep
        print("----------------------------- Working -----------------------------")
        sleep(0.5)
        for i in range(9):
            print("Process loading: ", str((i + 1) * 10) + "%")
            sleep(0.5)
        print("Done")
        print("Successfully, please take the money beside u")
    
    def getCurrentDay(self):
        days = open("day.txt", "a+")
        days.seek(0)
        dayList = []
        for day in days:
            dayList.append(day[:-1])
        return days, dayList[-1] if len(dayList) > 0 else ""

class Banking(MyFileHandling):

    def ExchangeCurrencyFunc(self, number):
        currencyList = ["500000", "200000", "100000", "50000", "20000", "10000", "5000", "2000", "1000"]
        copy_number = number
        resCurrency = {}
        while copy_number != 0:
            if int(currencyList[0]) <= copy_number:
                if currencyList[0] not in resCurrency:
                    resCurrency[currencyList[0]] = 1
                else:
                    resCurrency[currencyList[0]] += 1
                copy_number -= int(currencyList[0])
            else:
                currencyList.pop(0)
        return resCurrency, number
    
    def HistoryTransaction(self, file, grant, usr, beforeAmount, afterAmount, money):
        # grant 0: ATM-admin 1: user
        current_time = self.today.strftime("%H:%M:%S")
        if grant == 0:
            file.write(current_time + ": " + usr + "\n\t+ " + "Money: " + "-" + str(money) + "\n")
        elif grant == 1:
            file.write(current_time + " (" + self.day + ")" + ": " + "\n\t+ " + "Money: " + str(money) + "\n\t+ " + "Before Money: " + str(beforeAmount) + "\n\t+ " + "After Amount: " + str(afterAmount) + "\n")
    
    def processHistory(self, usrExtension, currentAmount, remainderAmount, userInput):
        fileDay, currentDay = self.getCurrentDay()
        with open("./HistoryTransaction/historyATM.txt", "a") as history_atm:
            if self.day != currentDay:
                history_atm.write("----------------" + self.day + "----------------\n")
                fileDay.write(self.day + "\n")
            self.HistoryTransaction(history_atm, 0, usrExtension, currentAmount, remainderAmount, userInput)
        with open("./HistoryTransaction/" + usrExtension + "_History.txt", "a") as history_usr:
            self.HistoryTransaction(history_usr, 1, usrExtension, currentAmount, remainderAmount, userInput)
        fileDay.close()
    
class ExchangeCurrency(object):
    
    def Running(self):
        pin = input("Enter your PIN: ")
        extract_file = MyFileHandling()
        bankingTransaction = Banking()
        f, usrExtension = extract_file.openFile(pin)
        userName, currentAmount = extract_file.getCurrentAmount(f)
        userInput = input("Please enter money: ")
        currentAmount, userInput = extract_file.filterAmount(currentAmount, userInput)
        while not (extract_file.Check(currentAmount, userInput)):
            userInput = input("Your amount value greater than the current value that u have: ")
            _, userInput = extract_file.filterAmount(currentAmount, userInput)
        exchangeCurr, _ = bankingTransaction.ExchangeCurrencyFunc(userInput)
        print(exchangeCurr)
        remainderAmount = currentAmount - userInput
        extract_file.Loading()
        extract_file.EditFile(f, userName, remainderAmount)
        bankingTransaction.processHistory(usrExtension, currentAmount, remainderAmount, userInput)
    
def main():
    exchange_currency = ExchangeCurrency()
    exchange_currency.Running()

if __name__ == "__main__":
    main()