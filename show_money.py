import PySimpleGUI as sg

def Money():
    layout = [
    [sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd500k2.png"), sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd200k2.png"), sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd100k2.png")],
    [sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd50k2.png"), sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd20k.png"), sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd10k2.png")],
    [sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd5k.png"), sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd2k2.png"), sg.Text("1", text_color="red", background_color="black", font=35), sg.Image(filename="./gui/img/vnd1k2.png")],
    [sg.Button("Take", size=(15, 1.2))]
]

    window = sg.Window("MONEY", layout, text_justification="center", element_justification="center")

    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED or event == "Take":
            break

    return window

window = Money()
window.close()