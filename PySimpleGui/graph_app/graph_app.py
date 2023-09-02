import PySimpleGUI as sg
import matplotlib.pyplot as plt  # Graphic
# back end functionality that connect matplotlib to Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_figure(data):
    axes = fig.axes
    x = [i[0] for i in data] # Esto nos devuelve el primer elemento de cada lista anidada
    y = [int(i[1]) for i in data]
    axes[0].plot(x,y, 'r-') # (x,y,style) r- == red, podemos cambiar la letra ej.: g- == green
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()

sg.theme('DarkTeal6')
table_content = []
layout = [
    [sg.Table(headings=['Observation', 'Result'], values=table_content,
              expand_x=True, hide_vertical_scroll=True, key='-TABLE-')],
    [sg.Input(key='-INPUT-', expand_x=True), sg.Button('Submit')],
    [sg.Canvas(key='-CANVAS-')]
]

window = sg.Window('Graph App', layout, finalize=True)

# Matplotlib  matplotlib.figure.Figure(figsize=(5, 4)) # Empty field
fig = plt.figure(figsize=(5, 4))
fig.add_subplot(111).plot([], [])  # Default postion ([x],[y])
figure_canvas_agg = FigureCanvasTkAgg(fig, window['-CANVAS-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Submit':
        new_value = values['-INPUT-']
        if new_value.isnumeric():
            # Observation & result
            table_content.append([len(table_content) + 1, float(new_value)])
            window['-TABLE-'].update(table_content)
            window['-INPUT-'].update('')  # Vaciamos el contenido del input
            
            update_figure(table_content)

window.close()


''' En el ejercicio se utiliza solamente matplotlib y haces:
matplotlib.figure.Figure(figsize=(5, 4)) # Empty field
Pero me generaba error. En la documentación encontre para generarlo de la siguiente manera.

En lugar de solo importar matplotlib, importe import matplotlib.pyplot as plt
y de plt utilice la propiedad figure.

Entiendo que realiza algo similar a lo que pedía el ejercicio

'''
