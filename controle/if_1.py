nota =float(input('Informe a nota do aluno'))
comportado = True if input('Comportado (y/n): ') == 'Y' or 'y ' else False

print(nota)

if nota >= 9 and comportado:
    print('Duas palavras: para bens! :P')
    print('Quadro de Honra')
elif nota >=7:
    print('Aprovado')
elif nota >=5:
    print('Recuperação')    
else:
    print('Reprovado')        
