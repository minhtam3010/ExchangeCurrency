from FileExtraction import MyFileHandling

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