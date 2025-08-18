'''
algoritmo necessário: primeiro, detectar o pino de origem, o trabalho e o seu destino
depois, para resolver uma torre de hanoi com n pinos,é preciso primeiro mover todos os discos de forma recursiva, exceto o maior, para o trabalho
para isso, é preciso resolver uma torre de Hanói com n-1 discos, mas agora o destino é o pino que antes era o trabalho 
e o novo trabalho é o pino que antes era o destino, então, nesse processo, é preciso trocar o destino e o trabalho.
Depois, é preciso mover o maior disco para o destino
O último passo é mover os outros discos para o destino, só que agora a origem é trocada com o trabalho

Assim, o algoritmo de forma simplificada tem três passos: 
para mover n discos do pino 1 ao pino 3:
1: mover n-1 discos (todos menos o maior) de 1 a 2
2: mover o maior de 1 a 3
3: mover n-1 discos de 2 a 3
'''

n = int(input("Número de discos:"))
A = "A"
B = "B"
C = "C"
i = 0
def hanoi (n, A,B,C):
    if n > 0:      #verifica se ainda é preciso fazer o processo de novo
        x = hanoi (n-1,A,C,B) #move os outros discos
        print(f'Mover disco {n} da pilha {A} para a pilha {C}') #digita o seguinte: mover "disco" de "origem" para "destino"
        y = hanoi (n-1,B,A,C) #move os outros discos para o destino
        return (x+1+y+i) # retorna o número de jogadas
    else:
        return(0) # se todos os discos já foram movidos, não faz nada


h =  hanoi (n,A,B,C)
print("O número mínimo de jogadas com %d pinos é"%(n),h)