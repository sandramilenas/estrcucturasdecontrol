def es_bisiesto(anio):
  """
  Determina si un año es bisiesto.

  Args:
    anio: El año a evaluar.

  Returns:
    True si el año es bisiesto, False en caso contrario.
  """

  if anio % 4 != 0:
    return False

  if anio % 100 == 0:
    if anio % 400 == 0:
      return True
    else:
      return False

  return True


def main():
  """
  Programa principal.

  Lee un año del usuario y determina si es bisiesto.
  """

  anio = int(input("Ingrese un año: "))

  if es_bisiesto(anio):
    print("si")
  else:
    print("no")


if __name__ == "__main__":
  main()