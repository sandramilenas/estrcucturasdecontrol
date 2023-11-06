def es_minuscula(letra):
  """
  Determina si una letra es minúscula.

  Args:
    letra: La letra a evaluar.

  Returns:
    True si la letra es minúscula, False en caso contrario.
  """

  return letra >= "a" and letra <= "z"


def es_mayuscula(letra):
  """
  Determina si una letra es mayúscula.

  Args:
    letra: La letra a evaluar.

  Returns:
    True si la letra es mayúscula, False en caso contrario.
  """

  return letra >= "A" and letra <= "Z"


def es_vocal(letra):
  """
  Determina si una letra es vocal.

  Args:
    letra: La letra a evaluar.

  Returns:
    True si la letra es vocal, False en caso contrario.
  """

  return letra in "aeiouAEIOU"


def main():
  """
  Programa principal.

  Lee una letra del usuario y determina si es minúscula, mayúscula, vocal o consonante.
  """

  letra = input("Ingrese una letra: ")

  if es_minuscula(letra):
    print("minuscula")
    if es_vocal(letra):
      print("vocal")
    else:
      print("consonante")
  else:
    print("mayuscula")
    if es_vocal(letra):
      print("vocal")
    else:
      print("consonante")


if __name__ == "__main__":
  main()