def ordenar(numeros):
  """
  Ordena una lista de números enteros de menor a mayor.

  Args:
    numeros: La lista de números a ordenar.

  Returns:
    La lista de números ordenada.
  """

  for i in range(len(numeros) - 1):
    for j in range(i + 1, len(numeros)):
      if numeros[i] > numeros[j]:
        numeros[i], numeros[j] = numeros[j], numeros[i]

  return numeros


def main():
  """
  Programa principal.

  Lee tres números del usuario y los imprime ordenados de menor a mayor.
  """

  numeros = input("Ingrese tres números enteros separados por un espacio: ")
  numeros = numeros.split()
  numeros = list(map(int, numeros))

  numeros_ordenados = ordenar(numeros)

  print(*numeros_ordenados)


if __name__ == "__main__":
  main()