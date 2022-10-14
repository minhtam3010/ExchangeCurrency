import PySimpleGUI as sg
from gui.processLoading import ProcessLoading3
from BankingATM.greedy import ShortestPath

layout = [
    [sg.Text("Finding the shortest path\nChoosing the location that u want to go....", size=(40, 2), justification="center")],
    [sg.Combo(values=["ATM", "BookStore"], size=(40, 2), background_color="black", text_color="white", button_background_color="red", button_arrow_color="black", key="PLACE")],
    [sg.Button("OK")]
]

window = sg.Window("FINDING PLACE", layout, element_justification="center")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "OK":
        window.hide()
        sp = ShortestPath(values["PLACE"])
        res = sp.FindShortestPathAtm(0)
        location = [sp.label[i] for i in res[:-1]]
        _, window_p = ProcessLoading3(sg, location)
    window.un_hide()
    window_p.close()

window.close()