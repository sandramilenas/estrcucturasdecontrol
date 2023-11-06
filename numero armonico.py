def numero_armonico(n):
  """
  Calcula el n-esimo número armónico.

  Args:
    n: El número armónico a calcular.

  Returns:
    El valor del número armónico.
  """

  suma = 0
  for i in range(1, n + 1):
    suma += 1 / i

  return suma


def main():
  """
  Programa principal.

  Lee un número del usuario y calcula su número armónico.
  """

  n = int(input("Ingrese un número: "))

  numero_armonico = numero_armonico(n)

  print(f"El {n}-esimo número armónico es: {numero_armonico:.4f}")


if __name__ == "__main__":
  main()
  