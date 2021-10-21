total=0
nota=0
qtde=0


while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair: '))
    if nota != -1:
        qtde += 1
        total += nota
print(f'A media da nota é {total / qtde}')

x=10

while x:
    print(x)
    x -=1
print('Fim!')    

