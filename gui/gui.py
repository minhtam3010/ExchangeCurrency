# import PySimpleGUI as sg
# import sys
# sys.path.append("..")
# from BankingATM.BankingTracsaction import Banking

# class GUI:

#     def __init__(self):
#         self.hold = "0"
#         self.Bank = Banking()

#     def getUsersFile(self):
#         # users_file = open("./BankingATM/users/user.txt", "r+")
#         users_file = open("../BankingATM/users/user.txt", "r+")
#         users = {}
#         for user in users_file:
#             splitUser = user[:-1].split(":")
#             users[splitUser[1]] = splitUser[0]
#         return users_file, users 

#     def ValidateUser(self, users, username, pin):
#         for username_file, pin_file in users.items():
#             if pin == pin_file and username == username_file[:len(username_file)-4]:
#                 return True
#         return False

#     def BalanceAccount(self, file_extension):
#         account_file = open("../BankingATM/users/" + file_extension, "r")
#         fullName = ""
#         balanceAccount = ""
#         for each in account_file:
#             if "\n" in each:
#                 fullName = each[:-1]
#             else:
#                 balanceAccount = each[15:]
#         return fullName, balanceAccount

#     def CreateAccount(self, users_file, users, username, nameAccount, userAccount, deposit):
#         for user in users.keys():
#             print(user[:len(user)-4])
#             if username == user[:len(user)-4]:
#                 return False
#         fileExtension = username + ".txt"
#         f = open("../BankingATM/users/" + fileExtension, "w")
#         f.write("Full Name: " + nameAccount.upper() + "\n")
#         users_file.write(userAccount  + ":" + fileExtension + "\n")
#         f.write("CurrentAmount: " + deposit)
#         users[userAccount] = fileExtension
#         return True

#     def WithdrawFunc(self):
#         return

#     def addComma(self, event, values, window, length):
#         split_values = values.split(",")
#         length_values = len(split_values)
#         res = ""
#         if length == 4:
#             if length_values > 1:
#                 for i in range(length_values):
#                     res += split_values[i][0] + "," + split_values[i][1:]
#                 window[event].update(res)
#             else:
#                 window[event].update(values[0] + "," + values[1:])
#         elif length > 4 and length <= 6:
#             # print(length, values[:-5], values[-4], values[-5], values[-3:], values)
#             if length_values > 2:
#                 res = split_values[0]
#                 for i in range(1, length_values):
#                     res += split_values[i][0] + "," + split_values[i][1:]
#                 window[event].update(res)
#             else:
#                 window[event].update(values[:-5] + values[-4] + values[-5] + values[-3:])

#     def deleteComma(self, event, window, values):
#         split_values = values.split(",")
#         res_join = "".join(split_values)
#         count = 0
#         res = ""
#         for i in res_join[::-1]:
#             if count == 3:
#                 res += "," + i
#                 count = 1
#             else:
#                 count += 1
#                 res += i
#         window[event].update(res[::-1])


#     def ValidateNumber(self, event, values, window, key):
#         # 0: use non-numeric; 1: length > 8
#         if event == key and values[key] and values[key][-1] not in ('0123456789,'):
#             window[key].update(values[key][:-1])
#             return "0"
#         elif len(values[key]) > 8 and key == "PIN_PERSONAL":
#             window[key].update(values[key][:-1])
#             return "1"
#         return ""

#     def Window(self):
#         layout = [
#             [sg.Text("USERNAME:"), sg.Input(key="USERNAME")],
#             [sg.Text("PIN:"), sg.Input(key="PIN_PERSONAL", password_char="*", enable_events=True)],
#             [sg.Button("Enter", size=(27, 1.2))],
#             [sg.Button("Create Account", size=(12, 1.2), ), sg.Exit(size=(8, 1.2))],
#             [sg.Text(key="OUTPUT")]
#         ]
#         sg.set_options(font="Times", element_size=(100, 2), )
#         window = sg.Window("ATM", layout, element_justification="right")
#         while True:
#             users_file, users = self.getUsersFile()
#             event, values = window.read()
#             if self.ValidateNumber(event, values, window, "PIN_PERSONAL") == "0":
#                 window["OUTPUT"].update("Please enter validate number!!!")
#             elif self.ValidateNumber(event, values, window, "PIN_PERSONAL") == "1":
#                 window["OUTPUT"].update("The range of PIN is not acceptable more than 8 digits")
#             else:
#                 window["OUTPUT"].update("")

#             if event == sg.WIN_CLOSED or event == "Exit":
#                 isExited = sg.popup_ok_cancel("Do u want to exit?", title="Alert")
#                 if isExited == "OK":
#                     break
#             elif event == "Create Account":
#                 layout2 = [
#                     [sg.Text("FULL NAME:"), sg.Input(key="FULLNAME")],
#                     [sg.Text("USERNAME:"), sg.Input(key="USERNAME")],
#                     [sg.Text("PIN:"), sg.Input(key="PIN_PERSONAL", enable_events=True, password_char="*")],
#                     [sg.Text("DEPOSIT"), sg.Input(key="DEPOSIT")],
#                     [sg.Button("Create", size=(10, 1.2)), sg.Button("Back", size=(10, 1.2))],
#                     [sg.Text(key="OUTPUT")]
#                 ]
#                 window2 = sg.Window("Create an Account", layout2, element_justification="right")

#                 while True:
#                     window.hide()
#                     event2, values2 = window2.read()
#                     if self.ValidateNumber(event2, values2, window2, "PIN_PERSONAL") == "0":
#                         window2["OUTPUT"].update("Please enter validate number!!!")
#                     elif self.ValidateNumber(event2, values2, window2, "PIN_PERSONAL") == "1":
#                         window2["OUTPUT"].update("The range of PIN is not acceptable more than 8 digits")

#                     if event2 == sg.WIN_CLOSED or event2 == "Back":
#                         window["PIN_PERSONAL"].update("")
#                         break
#                     elif event2 == "Create":
#                         if (len(values2["PIN_PERSONAL"]) != 8):
#                             window2["OUTPUT"].update("Can't create. Your PIN must have 8 digits!!!")
#                             continue
#                         isCreated = self.CreateAccount(users_file, users, values2["USERNAME"], values2["FULLNAME"], values2["PIN_PERSONAL"], values2["DEPOSIT"])
#                         if isCreated:
#                             sg.popup("Create an account successfully", title="Congrats")
#                         else:
#                             window2["OUTPUT"].update("Can't create. The username is already exisited in our system!!!")
#                             window2["USERNAME"].SetFocus(True)
#                             continue
#                         users_file.close()
#                         break
#                 window.un_hide()
#                 window2.close()
#             elif event == "Enter":
#                 if (len(values["PIN_PERSONAL"]) != 8):
#                     window["OUTPUT"].update("Your PIN must have 8 digits!!!")
#                     continue
#                 isValidated = self.ValidateUser(users, values["USERNAME"], values["PIN_PERSONAL"])
#                 if isValidated:
#                     sg.popup("Login successfully", title="Congrats")
#                     layout_service = [
#                         [sg.Button("CHECK BALANCE", size=(15, 2)), sg.Button("TRANSFERING", size=(15, 2))],
#                         [sg.Button("DEPOSIT", size=(15, 2)), sg.Button("WITHDRAW", size=(15, 2))],
#                         [sg.Exit(size=(41, 2))]
#                     ]
#                     window_service = sg.Window("Services", layout_service, element_justification="left")
                    
#                     while True:
#                         window.hide()
#                         event_service, value_service = window_service.read()
#                         if event_service == "CHECK BALANCE":
#                             fullName, balance = self.BalanceAccount(values["USERNAME"] + ".txt")
#                             layout_balance = [
#                                 [sg.Text(fullName)],
#                                 [sg.Text("Balance: " + balance)],
#                                 [sg.Button("Back")]
#                             ]
#                             window_balance = sg.Window("Balance Account", layout_balance, element_justification="left")
#                             while True:
#                                 window_service.hide()
#                                 event_balance, _ = window_balance.read()
                                
#                                 if event_balance == "Back":
#                                     break
#                             window_service.un_hide()
#                             window_balance.close()
#                         elif event_service == "WITHDRAW":
#                             layout_withdraw = [
#                                 [sg.Text("Money:"), sg.Input(key="MONEY", enable_events=True), sg.Button("Enter", size=(10, 1))],
#                                 [sg.Button("Back", size=(35, 1))],
#                                 [sg.Text(key="OUTPUT")]
#                             ]
#                             window_withdraw = sg.Window("Withdraw", layout_withdraw, element_justification="center", finalize=True)
#                             isNotWritten = True
#                             canDelete = False
#                             window_withdraw["MONEY"].update("0")
#                             length = 0
#                             while True:
#                                 window_service.hide()
#                                 event_withdraw, values_withdraw = window_withdraw.read()

#                                 if event_withdraw == "Back":
#                                     break
#                                 if event_withdraw == "Enter":
#                                     import random
#                                     fileExtension = values["USERNAME"] + ".txt"
#                                     fullname, balance = self.BalanceAccount(fileExtension)
#                                     fullname = fullname[11:]
#                                     balanceAmount, withdrawAmount = self.Bank.filterAmount(balance, values_withdraw["MONEY"])
#                                     exchangeCurr, location = self.Bank.ExchangeCurrencyFunc(withdrawAmount)
#                                     if len(exchangeCurr) == 0:
#                                         print("Thanks for using the service. Have a great day!!!")
#                                     print(exchangeCurr)
#                                     remainderAmount = balanceAmount - withdrawAmount
#                                     self.Bank.Loading()
#                                     self.Bank.EditFile(open("./BankingATM/users/" + values["USERNAME"] + ".txt", "r+"), fullname, remainderAmount)
#                                     self.Bank.printBillTransaction(self.Bank.day, self.Bank.today.strftime("%H:%M:%S"), location, random.randint(1, 1000), values["PIN_PERSONAL"][:5], fullname[11:], self.Bank.filterNumber(withdrawAmount), self.Bank.filterNumber(remainderAmount))
#                                     self.Bank.processHistory(values["USERNAME"], balanceAmount, remainderAmount, withdrawAmount)

#                                 if self.ValidateNumber(event_withdraw, values_withdraw, window_withdraw, "MONEY") == "0":
#                                     window_withdraw["OUTPUT"].update("Using number only")
#                                     continue
#                                 if len(values_withdraw["MONEY"]) == 0:
#                                     canDelete = True
#                                 if canDelete and len(values_withdraw["MONEY"]) == 0:
#                                     isNotWritten = True
#                                     window_withdraw["MONEY"].update("0")
#                                     canDelete = False
#                                     length = 0
#                                     self.hold = ""
#                                     continue
#                                 elif isNotWritten:
#                                     window_withdraw["MONEY"].update(values_withdraw["MONEY"][1])
#                                     isNotWritten = False
#                                     canDelete = True

#                                 split_hold = self.hold.split(",")
#                                 split_values_withdraw = values_withdraw["MONEY"].split(",")
#                                 res_hold = "".join(split_hold)
#                                 res_values = "".join(split_values_withdraw)
#                                 if res_hold == res_values:
#                                     if length == 0:
#                                         length = 4
#                                     else:
#                                         length -= 1
#                                     self.deleteComma(event_withdraw, window_withdraw, values_withdraw["MONEY"])
#                                     self.hold = values_withdraw["MONEY"][:-1]
#                                     continue
#                                 else:
#                                     self.hold = values_withdraw["MONEY"][:-1]
#                                 if length == 6:
#                                     length = 4
#                                 else:
#                                     length += 1
#                                 self.addComma("MONEY", values_withdraw["MONEY"], window_withdraw, length)
                                


#                             window_service.un_hide()
#                             window_withdraw.close()
#                         elif event_service == "Exit":
#                             window["PIN_PERSONAL"].update("")
#                             window["USERNAME"].update("")
#                             isExited = sg.popup_ok_cancel("Do u want to exit?", title="Alert")
#                             if isExited == "OK":
#                                 break

#                     window.un_hide()
#                     window_service.close()
#                 else:
#                     sg.popup("Your pin doesn't exist or incorrect!!!", title="Alert")
#                     window["PIN_PERSONAL"].update("")
#                     window["USERNAME"].update("")
#         window.close()
#         users_file.close()

# app = GUI()
# app.Window()