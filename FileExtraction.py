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