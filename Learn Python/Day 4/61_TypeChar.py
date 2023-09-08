import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [[sg.Text('Your typed chars apprear here: '), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Pattern 28', layout)

while True: #Event loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        #Update the "Output" text element tobe the value of "Input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()