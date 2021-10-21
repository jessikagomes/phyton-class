
#notas = [6.4,7.2,5.8,8.4]

# quero acrescentar 1.5 nas notas dos alunos

# for i, nota in enumerate(notas):
#     notas[i] = nota + 1.5
# print(notas)

# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5
# print(notas)

def soma_nota_bonus(nota):
    return nota + 1.5

notas = [6.4,7.2,5.8,8.4]

notas_finais = map(soma_nota_bonus, notas)
print(notas_finais)