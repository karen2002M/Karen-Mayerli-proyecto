""""""""
# Karen Mayerli 202103058
# problema 2
# Logical operators & conditional statements CODECHEF
# Este prolema pedia Actualizar  código para resolver el problema a continucación esta el codigo arreglado
""""""""

t = int(input())
for i in range(t):
    N, A, B = map(int, input().split())
    if N%A == 0 and N%B == 0:
        print('N is divisible by A and B')
    elif N%A == 0:
        print('N is divisible by only A')
    elif N%B == 0:
        print('N is divisible by only B')
    elif N%A != 0 and N%B != 0:
        print('N is divisible by neither A nor B')
