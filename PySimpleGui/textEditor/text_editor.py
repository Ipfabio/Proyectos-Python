import PySimpleGUI as sg
from pathlib import Path

smileys = [
    'happy', [':)', 'xD', ':D', '<3'],
    'sad', [':(', 'T_T'],
    'other', [':3'],
]
smiley_events = smileys[1] + smileys[3] + smileys[5]  # Cada lista

menu_layout = [
    ['File', ['Open', 'Save', '---', 'Exit']],
    ['Tools', ['Word Count']],
    ['Add', smileys]
]

sg.theme('GrayGrayGray')
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Untitled', key='-DOCNAME-')],
    [sg.Multiline(no_scrollbar=True, size=(70, 30), key='-TEXTBOX-')],
]

window = sg.Window('Text Editor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Open':
        # no_window, nos quita una ventana intermedia que viene por default
        file_path = sg.popup_get_file('Open', no_window=True)
        if file_path:  # Importar libreria Path de pathlib
            file = Path(file_path)
            window['-TEXTBOX-'].update(file.read_text())
            # Split y [-1] para que el nombre solo sea del archivo y no la ruta completa
            window['-DOCNAME-'].update(file_path.split('/')[-1])
        pass

    if event == 'Save':
        file_path = sg.popup_get_file('Save as', no_window=True, save_as=True) + '.txt'
        file = Path(file_path)
        file.write_text(values['-TEXTBOX-'])
        window['-DOCNAME-'].update(file_path.split('/')[-1])
        

    if event == 'Word Count':
        full_text = values['-TEXTBOX-']
        clean_text = full_text.replace('\n', ' ').split(' ')
        word_count = len(clean_text)
        char_count = len(''.join(clean_text))
        sg.popup(f'Words: {word_count}\nCharacters: {char_count}')

    if event in smiley_events:
        current_text = values['-TEXTBOX-']  # Adquirimos el texto actual
        # creamo una variable que tome el texto actual, sume un espacio y el evento seleccionado
        new_text = current_text + ' ' + event
        # Actualizamos la ventana con la variable creada
        window['-TEXTBOX-'].update(new_text)
window.close()
