""""""""
# Karen Mayerli 202103058
# problema 3
# chef diet
""""""""
T=int(input())                              # T es el número de casos
for _ in range(T):                          # aca se inicia el bucle usando for el cual se repetira segun el número de casos
    n, k = map(int, input().split())        # lee los numeros separados por espacios, n es el numero de dias y k la cantidad de proteina
    lista = list(map(int, input().split())) # esta lista almacena la cantidad de proteínas disponibles para cada día
    p = True                                # variable definida como p la cual va a indicar si chef siguio su plan de dieta  o no
    a = 0                                   # variable que almacena la cantidad de proteina que chef compra y consume cada dia
    b = 0                                   # variable que almacena la cantidad de proteina que chef guardara para consumir otros dias
    for i in range(n):                      # aca el bucle para los dias
        if lista[i]+b >= k:                 # si la suma de proteinas de el dia y las que chef guarda es mayor o igual a las que requiere
            a = lista[i]+b                  # suma de las proteinas del dia y las almacenadas
            b -= b                          # esto es si chef ocupara todas sus proteinas de ese dia
            if list(str(a-k))[0] != '-':    # esta linea es para comprobar  si la resta de las proteínas compradas y consumidas ese día y la cantidad de proteínas requeridas es un número positivo o no
                b += a-k                    # esta otra linea es la resta de las proteínas compradas y consumidas ese día y la cantidad de proteínas requeridas
        else:
            print("NO", i+1)                # se imprime NO y el numero de dia
            p = False                       # se le asigno a p un valor el cual es false lo indicara que chef no puede seguir su plan de dieta
            break                           # aqui se cierra el bucle
    if p == True:                           # aqui se compueba si p tiene el valor true si lo tiene chef cumplio con su dieta
        print("YES")                        # aqui se imprime YES si chef cumplio con su dieta
