import readchar


def leer_tecla():
  """
  Lee una tecla del teclado.

  Returns:
    La tecla presionada.
  """

  return readchar.readkey()


def main():
  """
  Programa principal.

  Corre un bucle infinito leyendo e imprimiendo las teclas.
  El bucle termina cuando se presiona la tecla ↑ indicada como UP.
  """

  while True:
    tecla = leer_tecla()
    print(tecla)
    if tecla == "↑":
      break


if __name__ == "__main__":
  main()