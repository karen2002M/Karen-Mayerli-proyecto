""""""""
# Karen Mayerli 202103058
# problema 5
# Counting Bits

class Solution(object):
    def countBits(self, n):                       # aca esta funcion dada por el problema llamada countBits
        lista= []                                 # esta lista vacia es para guardar los bits
        for i in range(n + 1):                    # el bucle que en este caso es para convertir cada número i en binario
             lista.append(bin(i)[2:].count('1'))  # añade los bits a la lista
        return lista                              # termina la ejecución de la función y da como resulto lo que esta almacenado en la lista

# Estas 3 ultimas lineas de acontinuación son solo para ingresar algun numero para probar la solución......
numero = int(input("Ingrese el numero: "))
respuesta = Solution()
print(respuesta.countBits(numero))

