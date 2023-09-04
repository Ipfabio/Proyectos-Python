from enum import Enum


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
    screen = move_piece(screen, Movement.ROTATE)


def move_piece(screen: list, movement: Movement) -> list:
    
    # Con esto pintamos de blanco por 10, por cada elemento en la fila
    new_screen = [["🔲"] * 10 for _ in range(10)]
    
    # Esto cambia cada vez que lo rote
    rotation_item = 0
    # Definimos la rotación de la pieza, el primero es la Fila, segundo la Columna. Con 4 rotaciones distintas
    rotation = [[(0, 0),(0, 0),(0, 0),(0, 0)],
                [(0, 1),(-1, 0),(0, -1),(1, -2)],
                [(0, 1),(-1, 0),(0, -1),(1, -2)],
                [(0, 1),(-1, 0),(0, -1),(1, -2)]]
    
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
                        new_column_index = column_index -1 
                    case Movement.ROTATE:
                        # indice actual + modificación[que elemento accedemeos][fila o columna]
                        new_row_index = row_index + rotation[rotation_item][0]
                        new_column_index = column_index + rotation[rotation_item][1]
                        # Actulizamos el item a mover
                        rotation_item += 1
                
                # Marcamos los limites de movimiento: Fila no puede ser mayor a 9, Columna ni menor a 0 ni mayor a 9
                if new_row_index > 9 or new_column_index > 9 or new_column_index < 0:
                    print("\nNo se puede realizar el movimiento")
                    # Si no se puede mover, se queda exactamente igual
                    return screen
                else:
                    # Le decimos donde pintar la ficha negra 
                    new_screen[new_row_index][new_column_index] = "🔳"
    
    print_screen(new_screen)
    # Retornamos el valor de la nueva pantalla para poder almacenarla
    return new_screen

# Le pasamos la pantalla que es una lista, imprimimos para separar una pantalla de otra
def print_screen(screen: list):
    print("\nPantalla Tetris:\n")
    # Hacemos que recorra las filas en pantalla
    for row in screen:
        # Con join las unimos y con map le aplicamos a todos los elementos de cada fila str
        print("".join(map(str, row)))


tetris()
