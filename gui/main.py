import PySimpleGUI as sg

class GUI:

    def getUsersFile(self):
        users_file = open("./BankingATM/users/user.txt", "r+")
        users = {}
        for user in users_file:
            splitUser = user[:-1].split(":")
            users[splitUser[0]] = splitUser[1]
        return users_file, users 

    def ValidateUser(self, users, pin):
        for user in users.keys():
            if pin == user:
                return True
        return False

    def CreateAccount(self, users_file, users, nameAccount, userAccount, deposit):
        fileExtension = "user" + str(len(users) + 1)  + ".txt"
        f = open("./BankingATM/users/" + fileExtension, "w")
        f.write("Full Name: " + nameAccount.upper() + "\n")
        users_file.write(userAccount  + ":" + fileExtension + "\n")
        f.write("CurrentAmount: " + deposit)
        users[userAccount] = fileExtension

    def Window(self):
        layout = [
            [sg.Text("PIN:"), sg.Input(key="PIN_PERSONAL", password_char="", enable_events=True), sg.Button("Enter")],
            [sg.Button("Create Account"), sg.Exit()],
            [sg.Text(key="OUTPUT")]
        ]

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
                break
            elif event == "Create Account":
                layout2 = [
                    [sg.Text("Full Name:"), sg.Input(key="FULLNAME")],
                    [sg.Text("PIN:"), sg.Input(key="PIN_PERSONAL", enable_events=True)],
                    [sg.Text("DEPOSIT"), sg.Input(key="DEPOSIT")],
                    [sg.Button("Create"), sg.Button("Back")],
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
                        print(values2)
                        self.CreateAccount(users_file, users, values2["FULLNAME"], values2["PIN_PERSONAL"], values2["DEPOSIT"])
                        sg.popup("Create an account successfully", title="Congrats")
                        users_file.close()
                        break
                window.un_hide()
                window2.close()
            elif event == "Enter":
                if (len(values["PIN_PERSONAL"]) != 8):
                    window["OUTPUT"].update("Your PIN must have 8 digits!!!")
                    continue
                isValidated = self.ValidateUser(users, values["PIN_PERSONAL"])
                if isValidated:
                    sg.popup("Login successfully", title="Congrats")
                    layout_service = [
                        [sg.Button("BANK BALANCE"), sg.Button("TRANSFERING")],
                        [sg.Button("DEPOSIT"), sg.Button("WITHDRAW")],
                        [sg.Exit()]
                    ]
                    window_service = sg.Window("Services", layout_service, element_justification="Center")
                    
                    while True:
                        window.hide()
                        event_service, value_service = window_service.read()
                        if event_service == "Exit":
                            window["PIN_PERSONAL"].update("")
                            break
                    window.un_hide()
                    window_service.close()
                else:
                    sg.popup("Your pin doesn't exist or incorrect!!!", title="Alert")
                    window["PIN_PERSONAL"].update("")
        window.close()
        users_file.close()

app = GUI()
app.Window()