""""""""
# Karen Mayerli 202103058
# problema 4
# Possible GCD
""""""""
from math import gcd                      # aqui se importo el maximo comun divisor de la biblioteca math
t = int(input())                          # el numero de casos de prueba
for _ in range(t):                        # la iteración sobre cada caso de prueba
  a, b = map(int, input().split())        # en esta linea se leen los numeros A y B de los casos de prueba
  d = abs(a - b)                          # aqui se calcula el valor absoluto de A y B
  if d == 0:                              # si la diferencia es 0 es resultado es infinito
    print("Infinito")                     # así que si se da ese caso se imprime infinito
  else:                                   # si lo anterior no pasa
    divisores = 0                         # se inicializa el contador del numero de divisores en 0
    for i in range(1, int(d**0.5) + 1):   # se itera sobre todos los posibles divisores desde el 1 hasta la raiz cuadrada de la diferencia
      if d % i == 0:                      # si i divide a la diferencia entonces
        divisores += 1                    # se agrega ese divisor al contador
        if i != d // i:                   # Si i no fuese igual a la diferencia dividida por i
          divisores += 1                  # el contador aumeta en un divisor mas
    print(divisores)                      # se imprime el resultado.....
