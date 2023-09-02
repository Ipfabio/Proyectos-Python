import PySimpleGUI as sg
# Para añadir otro elemento en el mismo 'row' simplemente hay que añadirlo en la misma 'lista anidada'
layout = [
    [sg.Text('Text', enable_events=True, key='-TEXT-'),
    sg.Spin(['item 1', 'item 2'])],  # Top row
    [sg.Button('Button', key='-BUTTON1-')],  # Second row
    [sg.Input(key='-INPUT-')],  # Third row
    [sg.Text('Hello!'), sg.Button('Test Button', key='-BUTTON2-')]
]

window = sg.Window('Converter', layout)  # Title,Layout

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON1-':
        # Así actualizamos el texto ej: .update(['-INPUT-']) en este caso actualiza el texto por lo que escribimos al apretar el boton
        window['-TEXT-'].update(visible=False)
        # Si lo dejamos vacío recibimos todos los 'values', podemos pasarle la 'key' para indicar cual queremos
        # print(values['-INPUT-'])

    if event == '-BUTTON2-':
        print('Boton de pruebas')

    if event == '-TEXT-':
        print('text was pressed')

window.close()