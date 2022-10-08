import PySimpleGUI as sg

class GUI:

    def ValidateUser(self, pin):
        users_file = open("./BankingATM/users/user.txt", "r+")
        users = {}
        for user in users_file:
            splitUser = user[:-1].split(":")
            users[splitUser[0]] = splitUser[1]

        for user in users.keys():
            if pin == user:
                return True
        users_file.close()
        return False

    def Window(self):
        layout = [
            [sg.Text("PIN:"), sg.Input(key="PIN_PERSONAL", password_char="", enable_events=True), sg.Button("Enter")],
            [sg.Button("Create Account"), sg.Exit()],
            [sg.Text(key="OUTPUT")]
        ]

        window = sg.Window("ATM", layout, element_justification="right")

        while True:
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
                    [sg.Text("DEPOSIT")],
                    [sg.Button("Create"), sg.Button("Back")],
                ]
                window2 = sg.Window("Create an Account", layout2, element_justification="right")

                while True:
                    window.hide()
                    event2, values2 = window2.read()
                    if event2 == 'PIN_PERSONAL' and values2['PIN_PERSONAL'] and values2['PIN_PERSONAL'][-1] not in ('0123456789.') or len(values2["PIN_PERSONAL"]) > 6:
                        window2['PIN_PERSONAL'].update(values2['PIN_PERSONAL'][:-1])
                    if event2 == sg.WIN_CLOSED or event2 == "Back":
                        break
                    elif event2 == "Create":
                        print(values2)
                        sg.popup("Create account successfully", title="Congrats")
                        break
                window.un_hide()
                window2.close()
            elif event == "Enter":
                if (len(values["PIN_PERSONAL"]) != 8):
                    window["OUTPUT"].update("Your PIN must have 8 digits!!!")
                    continue
                isValidated = self.ValidateUser(values["PIN_PERSONAL"])
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
        window.close()

app = GUI()
app.Window()