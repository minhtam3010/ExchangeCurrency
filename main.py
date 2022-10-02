from time import sleep

def openFile(filename):
    return open(filename, "r+")

# Get userName, currentAmount
def getCurrentAmount(file):
    currentAmount = ""
    userName = ""
    for each in file:
        if "\n" in each:
            print(each[:-1])
            userName = each[10:len(userName) - 1]
        else:
            print(each)
            currentAmount = each[-9:]
    return userName, currentAmount

# This function have fewer constrant range from 0 to 1 billiion & integer value 
def EditFile(file, userName, value):
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

def filterAmount(currentAmount, userInput):
    return int(currentAmount.replace(",", "")), int(userInput.replace(",", ""))

def Check(currentAmount, userInput):
    if currentAmount < userInput:
        return False
    return True

def Loading():
    print("----------------------------- Working -----------------------------")
    sleep(0.5)
    for i in range(9):
        print("Process loading: ", str((i + 1) * 10) + "%")
        sleep(0.5)
    print("Done")
    print("Successfully, please take the money beside u")

def ExchangeCurrency(number):
    currencyList = ["500000", "200000", "100000", "50000", "20000", "10000", "5000", "2000", "1000"]
    copy_number = number
    resCurrency = []
    while copy_number != 0:
        if int(currencyList[0]) <= copy_number:
            resCurrency.append(currencyList[0])
            copy_number -= int(currencyList[0])
        else:
            currencyList.pop(0)
    return resCurrency, number

def main():
    f = openFile("user1.txt")
    userName, currentAmount = getCurrentAmount(f)
    userInput = input("Please enter: ")
    currentAmount, userInput = filterAmount(currentAmount, userInput)
    while not (Check(currentAmount, userInput)):
        userInput = input("Your amount value greater than the current value that u have: ")
        currentAmount, userInput = filterAmount(currentAmount, userInput)
    remainderAmount = currentAmount - userInput
    Loading()
    EditFile(f, userName, remainderAmount)

if __name__ == "__main__":
    main()