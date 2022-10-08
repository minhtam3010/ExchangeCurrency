from BankingATM.FileExtraction import MyFileHandling

class Banking(MyFileHandling):

    def GetUnitOfMoneyInATM(self, filename):
        currency_file = open(filename, "a+")
        currency_file.seek(0)

        res = dict()
        for each in currency_file:
            if each == "\n":
                break
            split_arr = each[:-1].split(":")
            res[split_arr[0]] = int(split_arr[1])

        return currency_file, res

    def GetCurrentAmountATM(self, filename):
        amountATM_file = open(filename, "a+")
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
        

    def Pending(self, location, second_location):
        from time import sleep
        print("Step1: Moving to nearest location")
        sleep(2)
        print("---", end=" ", flush=True)
        sleep(2)
        print("---", end=" ", flush=True)
        sleep(2)
        print("---", end=" ", flush=True)
        sleep(2)
        print("---", end= " ", flush=True)
        print("---> Successfully found the nearest location in " + second_location + "\nStep2: Pulling money back to " + location)
        sleep(2)
        print("Transfering....")
        for _ in range(9):
            print("===", end=" ", flush=True)
            sleep(2)
        print("100%", flush=True)

    def AutomatedPullMoney(self, currency_file, amountAtm_file, currency_dict, numberBorrowed, location):
        second_atm_file, second_location = self.GetCurrentAmountATM("./BankingATM/AmountATM/ATM2.txt")
        second_currency_file, second_currency_dict = self.GetUnitOfMoneyInATM("./BankingATM/AmountATM/unitOfMoneyATM2.txt")
        second_currency_dict, res_currency = self.Calculation(numberBorrowed, second_currency_dict)
        self.ProcessAmountATM(second_currency_file, second_atm_file, numberBorrowed, second_currency_dict, second_location)
        for key, value in res_currency.items():
            currency_dict[key] += value
        self.ProcessAmountATM(currency_file, amountAtm_file, -numberBorrowed, currency_dict, location)
        return second_location[0]

    def Calculation(self, number, currency_dict):
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
        return currency_dict, res_currency

    def ExchangeCurrencyFunc(self, number):
        currency_file, currency_dict = self.GetUnitOfMoneyInATM("./BankingATM/AmountATM/unitOfMoneyATM1.txt")
        amountAtm_file, res = self.GetCurrentAmountATM("./BankingATM/AmountATM/ATM1.txt")
        currentAmountATM, _ = self.filterAmount(res[1], "")

        location = res[0]
        if currentAmountATM == 0:
            print("ATM Machine " + location + " is running out of money.")
        elif currentAmountATM < number:
            # TODO: Handle IF machine doesn't have adequate money
            print("This ATM machine " + location + " doesn't have adequate money for this transaction!!!")
            smartATM_service = input("Do you want to wait for the automated pulling money process from another location?: ")
            if smartATM_service.upper() == "Y":
                print("Process is loading.......")
                second_location = self.AutomatedPullMoney(currency_file, amountAtm_file, currency_dict, number - currentAmountATM, res)
                self.Pending(location, second_location)
                currency_file, currency_dict = self.GetUnitOfMoneyInATM("./BankingATM/AmountATM/unitOfMoneyATM1.txt")
                amountAtm_file, res = self.GetCurrentAmountATM("./BankingATM/AmountATM/ATM1.txt")
            else:
                return {}, number
        

        currency_dict, res_currency = self.Calculation(number, currency_dict)
        self.ProcessAmountATM(currency_file, amountAtm_file, number, currency_dict, res)
        return res_currency, location
    
    def HistoryTransaction(self, file, grant, usr, beforeAmount, afterAmount, money):
        # grant 0: ATM-admin 1: user
        current_time = self.today.strftime("%H:%M:%S")
        if grant == 0:
            file.write(current_time + ": " + usr + "\n\t+ " + "Money: " + "-" + str(money) + "\n")
        elif grant == 1:
            file.write(current_time + " (" + self.day + ")" + ": " + "\n\t+ " + "Money: " + str(money) + "\n\t+ " + "Before Money: " + str(beforeAmount) + "\n\t+ " + "After Amount: " + str(afterAmount) + "\n")
    
    def processHistory(self, usrExtension, currentAmount, remainderAmount, userInput):
        fileDay, currentDay = self.getCurrentDay()
        with open("./BankingATM/HistoryTransaction/historyATM.txt", "a") as history_atm:
            if self.day != currentDay:
                history_atm.write("----------------" + self.day + "----------------\n")
                fileDay.write(self.day + "\n")
            self.HistoryTransaction(history_atm, 0, usrExtension, currentAmount, remainderAmount, userInput)
        with open("./BankingATM/HistoryTransaction/" + usrExtension + "_History.txt", "a") as history_usr:
            self.HistoryTransaction(history_usr, 1, usrExtension, currentAmount, remainderAmount, userInput)
        fileDay.close()

    def printBillTransaction(self, date, time, location, receipt, card_no, fullname, amount, curent_amount):
        from pathlib import Path
        from docxtpl import DocxTemplate
        document_path = Path(__file__).parent / "Bill/bill_atm.docx"
        doc = DocxTemplate(document_path)
        context = {"DATE": date, "TIME": time, "LOCATION": location, "RECEIPT": receipt, "CARD": card_no, "FULLNAME": fullname, "AMOUNT": amount, "CURENTAMOUNT": curent_amount}
        doc.render(context)
        doc.save(Path(__file__).parent / "Bill/generated_bill_transaction.docx")

class ExchangeCurrency(object):
    
    def Running(self):
        import random
        pin = input("Enter your PIN: ")
        bankingTransaction = Banking()
        f, usrExtension, pin = bankingTransaction.openFile(pin)
        userName, currentAmount = bankingTransaction.getCurrentAmount(f)
        userInput = input("Please enter money: ")
        currentAmount, userInput = bankingTransaction.filterAmount(currentAmount, userInput)
        while not (bankingTransaction.Check(currentAmount, userInput)):
            userInput = input("Your amount value greater than the current value that u have: ")
            _, userInput = bankingTransaction.filterAmount(currentAmount, userInput)
        exchangeCurr, location = bankingTransaction.ExchangeCurrencyFunc(userInput)
        if len(exchangeCurr) == 0:
            print("Thanks for using the service. Have a great day!!!")
            return
        print(exchangeCurr)
        remainderAmount = currentAmount - userInput
        bankingTransaction.Loading()
        bankingTransaction.EditFile(f, userName, remainderAmount)
        bankingTransaction.printBillTransaction(bankingTransaction.day, bankingTransaction.today.strftime("%H:%M:%S"), location, random.randint(1, 1000), pin[:5], userName, bankingTransaction.filterNumber(userInput), bankingTransaction.filterNumber(remainderAmount))
        bankingTransaction.processHistory(usrExtension, currentAmount, remainderAmount, userInput)