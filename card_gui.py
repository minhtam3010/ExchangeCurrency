import PySimpleGUI as sg

def CardGUI(sg):
    layout = [
    [sg.FileBrowse(button_text="Card", size=(40, 3), key="CARD", enable_events=True)]
    ]
    res = ""
    window = sg.Window("Card", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        split_arr = values["CARD"].split("/")
        if split_arr[-1] == "VIB.png":
            layout_img = [
                [sg.Image(filename="gui/img/VIB.png")],
                [sg.Button("Back", size=(25, 1.2), enable_events=True), sg.Button("Ok", size=(25, 1.2), enable_events=True)]
            ]
            window_img = sg.Window("Img", layout_img, element_justification="center")
            while True:
                window.hide()
                event_img, _ = window_img.read()
                if event_img == "Back":
                    break
            window.un_hide()
            window_img.close()
            res = "OK"
        else:
            layout_img = [
                [sg.Image(filename="gui/img/TPBANK.png")],
                [sg.Button("Back", size=(25, 1.2)), sg.Button("Ok", key="OK", enable_events=True)]
            ]
            window_img = sg.Window("Img", layout_img)
            while True:
                window.hide()
                event_img, _ = window_img.read()
                if event_img == "Back":
                    break
            window.un_hide()
            window_img.close()
            res = "INVALID"

    return window, res


if __name__ == "__main__":
    window = CardGUI(sg)
    window.close()