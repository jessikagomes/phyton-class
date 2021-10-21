def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

somar = soma
subtrair=subtracao

print(somar(3,4))

def operacao_aritmetica(fn, op1,op2):
    return fn(op1,op2)

resultado = operacao_aritmetica(soma,13,48)
print(resultado)

resultado = operacao_aritmetica(subtracao,13,48)
print(resultado)
