import PySimpleGUI as sg


def create_window(theme):
    """create_window
    Nos 'cierra y vuelve a abrir' con el color que seleccionamos, por defaul le puse 'lightgrey1'
    """
    # Si ponemos cualquier cosa ej.: sg.theme('asdfa') nos indica en la terminal los distintos tipos de colores que podemos usar
    sg.theme(theme)
    # ElementSize se maneja por caracteres, no px.
    sg.set_options(font='Franklin 14', button_element_size=(6, 3))
    button_size = (6, 3)
    layout = [
        [sg.Text('0', font='Franklin 26', justification='right', expand_x=True, pad=(
            10, 20), right_click_menu=them_menu, key='-TEXT-')],  # V.1 para poner el texto en el extremo derecho
        # [sg.Push(), sg.Text('output', font='Franklin 26')], #V.2 Push ocupa todo el lado y empuja el texto
        [sg.Button('E', expand_x=True), sg.Button(
            'C', expand_x=True), sg.Button('/', size=button_size)],
        [sg.Button('7', size=button_size), sg.Button('8', size=button_size), sg.Button(
            '9', size=button_size), sg.Button('*', size=button_size)],
        [sg.Button('4', size=button_size), sg.Button('5', size=button_size), sg.Button(
            '6', size=button_size), sg.Button('+', size=button_size)],
        [sg.Button('1', size=button_size), sg.Button('2', size=button_size), sg.Button(
            '3', size=button_size), sg.Button('-', size=button_size)],
        [sg.Button('0', expand_x=True), sg.Button(
            '.', size=button_size), sg.Button('=', size=button_size)]
    ]
    return sg.Window('Calculator', layout)


''' En este caso, como todo el layout se crea antes, mantiene su tema por default
El orden importa, ya que al poner 'theme' después de 'layout', todos los elementos se crean con ese 'tema'
sg.theme('dark')'''
them_menu = ['menu', ['LightGrey1', 'dark', 'DarkGray8', 'random']]
window = create_window('dark')  # Por default

current_num = []  # Creamos una lista vacía para los números
full_operration = []  # Creamos una lista vacía para los símbolos

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in them_menu[1]:  # Menu
        window.close()
        window = create_window(event)

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        current_num.append(event)  # añadimos a la lista
        num_string = ''.join(current_num)  # Lo convertimos
        # Actualizamos la ventana en '-text-' con el num_string
        window['-TEXT-'].update(num_string)

    if event in ['+', '-', '/', '*',]:
        full_operration.append(''.join(current_num))  # Convertimos
        current_num = []  # Nuevo numero
        full_operration.append(event)  # le pasamos el evento seleccionado
        # Hacemos que se vacíe cuando le pasamos algún operador
        # Corregir, que aparezcan ambos numeros 'update(num_string + event)'
        window['-TEXT-'].update(event)

    if event == '=':
        full_operration.append(''.join(current_num))
        # Eval es de python, añade la lógica matemaática
        result = eval(' '.join(full_operration))
        window['-TEXT-'].update(result)
        full_operration = []  # Al final lo vacíamos para que evitar algunos errores

    if event == 'C':
        current_num = []
        full_operration = []
        window['-TEXT-'].update('0')

window.close()

'''
Customization:
    1. You can set a theme with sg.theme()
    2. You can set Options with sg.set_options() # Font, padding, etc.
    3. Each individual element as customization options
'''

# sg.set_options()  https://www.pysimplegui.org/en/latest/call%20reference/

# TODO el botón E no tiene razón de ser y al poner varios simbolos sin seguirle algún número da error
#  que todos los números sigan apareciendo en pantalla, y una
