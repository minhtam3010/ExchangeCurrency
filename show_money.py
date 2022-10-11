import PySimpleGUI as sg

class ShowMoney(object):

    def __init__(self, amount):
        self.layout = [[sg.Text("Amount of Money: " + amount, font=50, background_color="black", text_color="#00ffff")]]
        self.currency_dict = {"500000": "./gui/img/vnd500k2.png", "200000": "./gui/img/vnd200k2.png", "100000": "./gui/img/vnd100k2.png", "50000": "./gui/img/vnd50k2.png", "20000": "./gui/img/vnd20k.png", "10000": "./gui/img/vnd10k2.png", "5000": "./gui/img/vnd5k.png", "2000": "./gui/img/vnd2k2.png", "1000": "./gui/img/vnd1k2.png"}

    def Money(self, currency_dict):
        # layout = [
        # [sg.Text("1", text_color="red", background_color="white", font=35), sg.Image(filename="./gui/img/vnd500k2.png"), sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd200k2.png"), sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd100k2.png")],
        # [sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd50k2.png"), sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd20k.png"), sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd10k2.png")],
        # [sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd5k.png"), sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd2k2.png"), sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd1k2.png")],
        # [sg.Button("Take", size=(15, 1.2))]
        # ]
        count = 0
        res = []
        for key, values in currency_dict.items():
            if count == 3:
                self.layout += [res]
                res = [sg.Text(str(values), text_color="#E0115F", background_color="black", font=35), sg.Image(filename=self.currency_dict[key])]
                count = 1
            else:
                res += [sg.Text(str(values), text_color="#E0115F", background_color="black", font=35), sg.Image(filename=self.currency_dict[key])]
                count += 1
        self.layout += [res]
        self.layout[-1] += [sg.Button("Take", size=(30, 1.2))]
        window = sg.Window("MONEY", self.layout, text_justification="center", element_justification="center")
        while True:
            event, _ = window.read()
            if event == sg.WIN_CLOSED or event == "Take":
                break
        return window

if __name__ == "__main__":
    currency_dict = {"500000": 3, "200000": 2, "100000": 5, "50000": 3}
    sm = ShowMoney("2550000")
    window = sm.Money(currency_dict)
    window.close()