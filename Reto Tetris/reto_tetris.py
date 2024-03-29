from enum import Enum
import keyboard


class Movement(Enum):
    """Movement
    Definimos el movimiento: Abajo, Derecha, Izquierda, Rotar
    """

    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4


def tetris():
    screen = [
        ["🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔳", "🔳", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
    ]

    print_screen(screen)

    rotation = 0

    while True:
        event = keyboard.read_event()

        if event.name == "esc":
            break
        elif event.event_type == keyboard.KEY_DOWN:
            # Movimientos de la pieza
            if event.name == "down":
                (screen, rotation) = move_piece(screen, Movement.DOWN, rotation)
            elif event.name == "right":
                (screen, rotation) = move_piece(screen, Movement.RIGHT, rotation)
            elif event.name == "left":
                (screen, rotation) = move_piece(screen, Movement.LEFT, rotation)
            elif event.name == "space":
                (screen, rotation) = move_piece(screen, Movement.ROTATE, rotation)


# Recibe pantalla (lista), movimiento(clase movimiento) y rotación indica el estado actual de la pieza
def move_piece(screen: list, movement: Movement, rotation: int) -> (list, int):
    # Con esto pintamos de blanco por 10, por cada elemento en la fila
    new_screen = [["🔲"] * 10 for _ in range(10)]

    # Esto cambia cada vez que lo rote
    rotation_item = 0
    # Definimos la rotación de la pieza, el primero es la Fila, segundo la Columna. Con 4 rotaciones distintas
    rotations = [
        [(1, 1), (0, 0), (-2, 0), (-1, -1)],
        [(0, 1), (-1, 0), (0, -1), (1, -2)],
        [(0, 2), (1, 1), (-1, 1), (-2, 0)],
        [(0, 1), (1, 0), (2, -1), (1, -2)],
    ]

    new_rotation = rotation

    # Controlamos cual es la ficha que hay que pintar dependiendo si roto por primera vez o no
    if movement is Movement.ROTATE:
        new_rotation = 0 if rotation == 3 else rotation + 1

    # Recorremos la lista, usamos enumerate en screen y row para que nos devuelva su valor e indice
    # en lugar de llamar column, llamanos item, porque referenciamos al elemento (cuadrado banco o negro)
    for row_index, row in enumerate(screen):
        for column_index, item in enumerate(row):
            # Si item es igual al cuadrado negro, podemos ejecutar los movimientos
            if item == "🔳":
                new_row_index = 0
                new_column_index = 0

                match movement:
                    case Movement.DOWN:
                        new_row_index = row_index + 1
                        new_column_index = column_index
                    case Movement.RIGHT:
                        new_row_index = row_index
                        new_column_index = column_index + 1
                    case Movement.LEFT:
                        new_row_index = row_index
                        new_column_index = column_index - 1
                    case Movement.ROTATE:
                        # indice actual + modificación[que elemento accedemeos][fila o columna]
                        new_row_index = (
                            row_index + rotations[new_rotation][rotation_item][0]
                        )
                        new_column_index = (
                            column_index + rotations[new_rotation][rotation_item][1]
                        )
                        # Actulizamos el item a mover
                        rotation_item += 1

                # Marcamos los limites de movimiento: Fila no puede ser mayor a 9, Columna ni menor a 0 ni mayor a 9
                if new_row_index > 9 or new_column_index > 9 or new_column_index < 0:
                    print("\nNo se puede realizar el movimiento")
                    # Si no se puede mover, se queda exactamente igual
                    return (screen, rotation)
                else:
                    # Le decimos donde pintar la ficha negra
                    new_screen[new_row_index][new_column_index] = "🔳"

    print_screen(new_screen)
    # Retornamos el valor de la nueva pantalla para poder almacenarla
    return (new_screen, new_rotation)


# Le pasamos la pantalla que es una lista, imprimimos para separar una pantalla de otra
def print_screen(screen: list):
    print("\nPantalla Tetris:\n")
    # Hacemos que recorra las filas en pantalla
    for row in screen:
        # Con join las unimos y con map le aplicamos a todos los elementos de cada fila str
        print("".join(map(str, row)))


tetris()
