import PySimpleGUI as sg


layout = [  # list of lists
    [sg.Text("Text", enable_events=True, key="-TEXT-"),
     sg.Spin(["item 1", "Item 2"])],
    [sg.Button("Button", key="-BUTTON1-")],
    [sg.Input(key="-INPUT-")],
    [sg.Text("Test"), sg.Button("Button", key="-BUTTON2-")]
]

# .read()  Read Waits & Reads Input or return value
window = sg.Window("Converter", layout)
# Events
while True:
    event, values = window.read()  # Returns events, values

    if event == sg.WIN_CLOSED:
        break
    if event == "-BUTTON1-":
        print(values)
    if event == "-BUTTON2-":
        print("Button is been pressed!")
    if event == "-TEXT-":
        print("Text is been pressed!")

window.close()
# Values
