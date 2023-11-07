def maze_to_matrix_v2(maze):
  """Convertir el laberinto de cadena a matriz.

  Args:
    maze: Laberinto en cadena.

  Returns:
    Laberinto en matriz.
  """

  # Obtener las coordenadas del laberinto.
  rows, cols = maze.split(" ")[:2]
  rows = int(rows)
  cols = int(cols)

  # Crear una matriz vacía.
  matrix = [[None] * cols for _ in range(rows)]

  # Convertir el laberinto de cadena a matriz.
  matrix = map(lambda c: c, maze[2:])

  # Convertir la secuencia de caracteres a matriz.
  matrix = list(matrix)

  # Agregar las filas vacías al principio de la matriz.
  for _ in range(rows - 1):
    matrix.insert(0, [None] * cols)

  return matrix

def read_maze_v2(filename):
  """Leer el mapa.

  Args:
    filename: Nombre del archivo del mapa.

  Returns:
    Laberinto en cadena.
  """

  # Leer el mapa en una sola operación.
  with open(filename, "r") as f:
    map_lines = f.readlines()

  # Obtener las coordenadas del laberinto.
  rows, cols = map_lines[0].split(" ")[:2]
  rows = int(rows)
  cols = int(cols)

  # Concatenar las filas del mapa en una sola cadena.
  map_string = reduce(lambda a, b: a + b, map_lines[1:])

  return map_string, rows, cols

# Leer el mapa.
map_string, rows, cols = read_maze_v2("maze.txt")

# Convertir el laberinto a matriz.
matrix = maze_to_matrix_v2(map_string)

# Imprimir el laberinto.
for row in matrix:
  print("".join(row))