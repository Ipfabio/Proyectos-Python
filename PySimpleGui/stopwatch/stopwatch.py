import PySimpleGUI as sg
from time import time


def create_window():
    sg.theme('black')
    layout = [
        # Enable events, permite "Convertirlo en boton" para darle la función de cierre
        [sg.Push(), sg.Image('cross.png', pad=0, enable_events=True, key='-CLOSE-')],
        # Creamos ambos VPush para empujarlo primero hacia abajo y luego hacia arriba. Queda en el centro
        [sg.VPush()],
        # Este estilo de letra puede no estar instalado en todos los O.S.
        [sg.Text('Time', font='Young 50', key='-TIME-')],
        [
            sg.Button('Start', button_color=('#FFFFFF', '#FF0000'),
                      border_width=0, key='-STARTSTOP-'),
            sg.Button('Lap', button_color=('#FFFFFF', '#FF0000'),
                      border_width=0, key='-LAP-', visible=False)
        ],
        [sg.Column([[]], key='-LAPS-')],  # Necesita una lista anidada
        [sg.VPush()]
    ]

    return sg.Window(
        'StopWatch',
        layout,
        size=(300, 300),
        no_titlebar=True,
        element_justification='center'
    )


window = create_window()
start_time = 0
active = False
lap_amount = 1

while True:
    event, values = window.read(timeout=10)  # Miliseconds
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

    if event == '-STARTSTOP-':
        if active:
            # From active to Stop
            active = False
            window['-STARTSTOP-'].update('Reset')
            window['-LAP-'].update(visible=False)
        else:
            # From stop to resert
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
                lap_amount = 1
                # From start to Active
            else:
                start_time = time()
                active = True
                window['-STARTSTOP-'].update('Stop')
                window['-LAP-'].update(visible=True)

    if active:
        elapsed_time = round(time() - start_time, 1)
        window['-TIME-'].update(elapsed_time)

    if event == '-LAP-':
        # Need a container and a element
        window.extend_layout(
            window['-LAPS-'], [[sg.Text(lap_amount), sg.VSeparator(), sg.Text(elapsed_time)]])
        lap_amount += 1

window.close()
