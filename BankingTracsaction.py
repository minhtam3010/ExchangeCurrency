from FileExtraction import MyFileHandling

class Banking(MyFileHandling):

    def GetUnitOfMoneyInATM(self):
        currency_file = open("./AmountATM/unitOfMoneyATM1.txt", "a+")
        currency_file.seek(0)

        res = dict()
        for each in currency_file:
            if each == "\n":
                break
            split_arr = each[:-1].split(":")
            res[split_arr[0]] = int(split_arr[1])

        return currency_file, res

    def GetCurrentAmountATM(self):
        amountATM_file = open("./AmountATM/ATM1.txt", "a+")
        amountATM_file.seek(0)

        res = []
        for each in amountATM_file:
            if "\n" in each:
                res.append(each[:len(each) - 1])
            else:
                res.append(each[15:])
        return amountATM_file, res

    def ProcessAmountATM(self, currency_file, amountATM_file, amountATM, currency_dict, res):
        currency_file.seek(0)
        amountATM_file.seek(0)
        currency_file.truncate()
        amountATM_file.truncate()
        for key, value in currency_dict.items():
            currency_file.write(key + ": " + str(value) + "\n")
        amountATM_file.write(res[0] + "\n")
        filter_amountATM, _ = self.filterAmount(res[1], "")
        amountATM = filter_amountATM - amountATM
        amountATM_file.write("CurrentAmount: " + self.filterNumber(amountATM))
        currency_file.close()
        amountATM_file.close()

    def ExchangeCurrencyFunc(self, number):
        currency_file, currency_dict = self.GetUnitOfMoneyInATM()
        amountAtm_file, res = self.GetCurrentAmountATM()
        currentAmountATM, _ = self.filterAmount(res[1], "")
        if currentAmountATM < number:
            # TODO: Handle IF machine doesn't have adequate money 
            return

        currencyList = ["500000", "200000", "100000", "50000", "20000", "10000", "5000", "2000", "1000"]
        copy_number = number
        res_currency = {}
        while copy_number != 0:
            if int(currencyList[0]) <= copy_number:
                if currency_dict[currencyList[0]] > 0:
                    currency_dict[currencyList[0]] -= 1
                    res_currency[currencyList[0]] = 1 if currencyList[0] not in res_currency else res_currency[currencyList[0]] + 1
                else:
                    currencyList.pop(0)
                    continue
                copy_number -= int(currencyList[0])
            else:
                currencyList.pop(0)
        
        self.ProcessAmountATM(currency_file, amountAtm_file, number, currency_dict, res)
        return res_currency, currency_dict
    
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
        res, exchangeCurr = bankingTransaction.ExchangeCurrencyFunc(userInput)
        print(res)
        remainderAmount = currentAmount - userInput
        extract_file.Loading()
        extract_file.EditFile(f, userName, remainderAmount)
        bankingTransaction.processHistory(usrExtension, currentAmount, remainderAmount, userInput)