import PySimpleGUI as sg
# Para añadir otro elemento en el mismo 'row' simplemente hay que añadirlo en la misma 'lista anidada'
layout = [
    [sg.Input(key='-INPUT-'),
     sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key='-UNITS-'),
     sg.Button('Convert', key='-CONVERT-')
     ],
    [sg.Text('Output', key='-OUTPUT-')]]

window = sg.Window('Converter', layout)  # Title,Layout

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km to mile':
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f'{input_value} km are {output} miles.'
                case 'kg to pound':
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f'{input_value} kg are {output} pounds.'
                case 'sec to min':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} seconds are {output} minutes.'

            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Please enter a number')

window.close()

'''
Events:
an event is triggered by a certain action:
    Closing the window triggers the sg.WIN_CLOSED event
    In SimpleGUI, every element can trigger an event.

Example: A button click triggers another event.
The name o that event will be the name, or rather the key, of that button

Our button is calle 'button' and that would be the key and the event name

Podemos llamarlos if event == nombre o utilizando la 'key'
Se recomienda usar el sistema de nombrar las 'key' = '-BUTTON1-' En mayuscula y con guiones

Values:
Are kind  of similar to events, except, they return more information (In PySimpleGUI)
There are several elements that can contain values, like Input.
These values are stored in one dictionary, called values.
You can access that one with the name of the input element.
If an input element does not have a key it gets a number assigned

Updating elements:
Every element has an update method.
It can be used to change text, visibility, etc.

Concepts to understand
1. Elements & Layout
2. Events & Values
3. Update
'''
