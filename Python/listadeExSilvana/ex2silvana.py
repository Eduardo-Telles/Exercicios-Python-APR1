'''Quatro amigos combinaram de jogar tênis em duplas. Cada um dos amigos tem um 
nível de jogo, que é representado por um número inteiro: quanto maior o número, 
melhor o nível do jogador.
Os quatro amigos querem formar as duplas para iniciar o jogo. De forma a tornar o 
jogo mais interessante, eles querem que os níveis dos dois times formados sejam o mais 
próximo possível. O nível de um time é a soma dos níveis dos jogadores do time.
Embora eles sejam muito bons jogadores de tênis, os quatro amigos não são muito bons 
em algumas outras coisas, como lógica ou matemática. Você pode ajudá-los e encontrar 
a menor diferença possível entre os níveis dos times que podem ser formados?
Entrada
A entrada contém quatro linhas, cada linha contendo um inteiro A, B, C e D, indicando 
o nível de jogo dos quatro amigos.
Saída
Seu programa deve produzir uma única linha, contendo um único inteiro, a menor 
diferença entre os níveis dos dois times formados.
Restrições
 0 ≤ A ≤ B ≤ C ≤ D ≤ 10**4'''
A = int(input("Digite o nível do jgr A"))
B = int(input("Digite o nível do jgr B"))
C = int(input("Digite o nível do jgr C"))
D = int(input("Digite o nível do jgr D"))
if D > 10 ** 4 or A < 0:
    print(f"Não será possível realizar a operação")
elif D < C or C < B or B < A:
    print(f"Não será possivel realizar a operação")
elif A <= B and D > C or B == C:
    print(f"A menor difr será: {(A+D) - (B+C)}")
elif A < B and D == C:
    print(f"A menor difr será: {(B+C) - (A+D)}")
else:
    print(f"A menor difr será: {(A+B)/2}")
    



 
