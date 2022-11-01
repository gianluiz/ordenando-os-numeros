#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
#correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
valores = []
for c in range(0,5):
    while True:
        try:
            n = int(input("número:"))
            break
        except ValueError:
            print("ERRO.\nDIGITE UM NÚMERO INTEIRO.")
    if c == 0:
        valores.append(n)
    if n > valores[-1]:
        valores.append(n)
    posicao = 0
    while posicao < len(valores):
        if n < valores[posicao]:
            valores.insert(posicao, n)
            break
        posicao += 1
print(valores)

#existe a opção de realizar este código com apenas uma linha, leia o README