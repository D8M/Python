# 1 -The Import
from pickle import TRUE
import PySimpleGUI as sg

# 2 -The layout Definition
layout = [  # List of 4 Lists
    # Currently, each column doesn't align
    [sg.Text("TempText", enable_events=TRUE, key="-TEXT-", size=(20, 1), font='Courier 15'),  # each list in the layout represents a row in the window
     sg.Spin(["item1", "item2"])],
    [sg.Button("Button", key="-BUTTON1-")],
    [sg.Input(key="-INPUT-")],
    [sg.Text("Hello"), sg.Button("Button", key="-BUTTON2-")]
]

# 3 - Create the Window
window = sg.Window("Converter", layout)

# 4 - The Event Loop
while True:
    event, values = window.read()  # read() = read Method looks for event or return value
    if event == sg.WIN_CLOSED:  # Clicking on the x in window corner
        break

    if event == "-BUTTON1-":
        print(values)

    if event == "-BUTTON2-":
        print("Something else!")

    if event == "-TEXT-":
        print("Text was pressed!")

# 5 - Close Window
window.close()
