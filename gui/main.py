from ctypes import sizeof
import PySimpleGUI as sg

class GUI:

    def getUsersFile(self):
        users_file = open("./BankingATM/users/user.txt", "r+")
        users = {}
        for user in users_file:
            splitUser = user[:-1].split(":")
            users[splitUser[0]] = splitUser[1]
        return users_file, users 

    def ValidateUser(self, users, username, pin):
        for pin_file, username_file in users.items():
            if pin == pin_file and username == username_file[:len(username_file)-4]:
                return True
        return False

    def BalanceAccount(self, file_extension):
        account_file = open("./BankingATM/users/" + file_extension, "r")
        fullName = ""
        balanceAccount = ""
        for each in account_file:
            if "\n" in each:
                fullName = each[:-1]
            else:
                balanceAccount = each[15:]
        return fullName, balanceAccount

    def CreateAccount(self, users_file, users, username, nameAccount, userAccount, deposit):
        for user in users.values():
            if username == user[:len(user)-4]:
                return False
        fileExtension = username + ".txt"
        f = open("./BankingATM/users/" + fileExtension, "w")
        f.write("Full Name: " + nameAccount.upper() + "\n")
        users_file.write(userAccount  + ":" + fileExtension + "\n")
        f.write("CurrentAmount: " + deposit)
        users[userAccount] = fileExtension
        return True

    def Window(self):
        layout = [
            [sg.Text("USERNAME:"), sg.Input(key="USERNAME")],
            [sg.Text("PIN:"), sg.Input(key="PIN_PERSONAL", password_char="*", enable_events=True)],
            [sg.Button("Enter", size=(27, 1.2))],
            [sg.Button("Create Account", size=(12, 1.2), ), sg.Exit(size=(8, 1.2))],
            [sg.Text(key="OUTPUT")]
        ]
        sg.set_options(font="Times", element_size=(100, 2), )
        window = sg.Window("ATM", layout, element_justification="right")
        while True:
            users_file, users = self.getUsersFile()
            event, values = window.read()
            if event == 'PIN_PERSONAL' and values['PIN_PERSONAL'] and values['PIN_PERSONAL'][-1] not in ('0123456789.'):
                window['PIN_PERSONAL'].update(values['PIN_PERSONAL'][:-1])
                window["OUTPUT"].update("Please enter validate number!!!")
            elif len(values["PIN_PERSONAL"]) > 8:
                window['PIN_PERSONAL'].update(values['PIN_PERSONAL'][:-1])
                window["OUTPUT"].update("The range of PIN is not acceptable more than 8 digits")
            else:
                window["OUTPUT"].update("")

            if event == sg.WIN_CLOSED or event == "Exit":
                isExited = sg.popup_ok_cancel("Do u want to exit?", title="Alert")
                if isExited == "OK":
                    break
            elif event == "Create Account":
                layout2 = [
                    [sg.Text("FULL NAME:"), sg.Input(key="FULLNAME")],
                    [sg.Text("USERNAME:"), sg.Input(key="USERNAME")],
                    [sg.Text("PIN:"), sg.Input(key="PIN_PERSONAL", enable_events=True, password_char="*")],
                    [sg.Text("DEPOSIT"), sg.Input(key="DEPOSIT")],
                    [sg.Button("Create", size=(10, 1.2)), sg.Button("Back", size=(10, 1.2))],
                    [sg.Text(key="OUTPUT")]
                ]
                window2 = sg.Window("Create an Account", layout2, element_justification="right")

                while True:
                    window.hide()
                    event2, values2 = window2.read()
                    if event2 == 'PIN_PERSONAL' and values2['PIN_PERSONAL'] and values2['PIN_PERSONAL'][-1] not in ('0123456789.'):
                        window2['PIN_PERSONAL'].update(values2['PIN_PERSONAL'][:-1])
                        window2["OUTPUT"].update("Please enter validate number!!!")
                    elif len(values2["PIN_PERSONAL"]) > 8:
                        window2['PIN_PERSONAL'].update(values2['PIN_PERSONAL'][:-1])
                        window2["OUTPUT"].update("The range of PIN is not acceptable more than 8 digits")

                    if event2 == sg.WIN_CLOSED or event2 == "Back":
                        window["PIN_PERSONAL"].update("")
                        break
                    elif event2 == "Create":
                        if (len(values2["PIN_PERSONAL"]) != 8):
                            window2["OUTPUT"].update("Can't create. Your PIN must have 8 digits!!!")
                            continue
                        isCreated = self.CreateAccount(users_file, users, values2["USERNAME"], values2["FULLNAME"], values2["PIN_PERSONAL"], values2["DEPOSIT"])
                        if isCreated:
                            sg.popup("Create an account successfully", title="Congrats")
                        else:
                            window2["OUTPUT"].update("Can't create. The username is already exisited in our system!!!")
                            window2["USERNAME"].SetFocus(True)
                            continue
                        users_file.close()
                        break
                window.un_hide()
                window2.close()
            elif event == "Enter":
                if (len(values["PIN_PERSONAL"]) != 8):
                    window["OUTPUT"].update("Your PIN must have 8 digits!!!")
                    continue
                isValidated = self.ValidateUser(users, values["USERNAME"], values["PIN_PERSONAL"])
                if isValidated:
                    sg.popup("Login successfully", title="Congrats")
                    layout_service = [
                        [sg.Button("CHECK BALANCE", size=(15, 2)), sg.Button("TRANSFERING", size=(15, 2))],
                        [sg.Button("DEPOSIT", size=(15, 2)), sg.Button("WITHDRAW", size=(15, 2))],
                        [sg.Exit(size=(41, 2))]
                    ]
                    window_service = sg.Window("Services", layout_service, element_justification="left")
                    
                    while True:
                        window.hide()
                        event_service, value_service = window_service.read()
                        if event_service == "CHECK BALANCE":
                            fullName, balance = self.BalanceAccount(users[values["PIN_PERSONAL"]])
                            layout_balance = [
                                [sg.Text(fullName)],
                                [sg.Text("Balance: " + balance)],
                                [sg.Button("Back")]
                            ]
                            window_balance = sg.Window("Balance Account", layout_balance, element_justification="left")
                            while True:
                                window_service.hide()
                                event_balance, _ = window_balance.read()
                                
                                if event_balance == "Back":
                                    break
                            window_service.un_hide()
                            window_balance.close()

                        elif event_service == "Exit":
                            window["PIN_PERSONAL"].update("")
                            window["USERNAME"].update("")
                            isExited = sg.popup_ok_cancel("Do u want to exit?", title="Alert")
                            if isExited == "OK":
                                break

                    window.un_hide()
                    window_service.close()
                else:
                    sg.popup("Your pin doesn't exist or incorrect!!!", title="Alert")
                    window["PIN_PERSONAL"].update("")
                    window["USERNAME"].update("")
        window.close()
        users_file.close()

app = GUI()
app.Window()