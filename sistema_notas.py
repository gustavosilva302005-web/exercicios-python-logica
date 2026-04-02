notas = []

while True:
    nota = float(input("Digite uma nota (-1 para sair): "))
    if nota == -1:
        break
    notas.append(nota)

if len(notas) > 0:
        media = sum(notas) / len(notas)
        maior = max(notas)
        menor = min(notas)

        print(f'A média da lista é: {media: 2f}')
        print(f'A maior nota é:  {maior}')
        print(f'A menor nota é: {menor}')
else:
        print('Nenhuma nota foi digitada.')    