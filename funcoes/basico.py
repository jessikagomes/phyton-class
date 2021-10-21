# def saudacao():
#     print("Bom dia!")

# def saudacao(nome):
#     print(f'Bom dia!{nome}')    

# def saudacao(nome='Pessoa'):
#     print(f'Bom dia!{nome}') 

def saudacao(nome='Pessoa', idade=20):
    print(f'Bom dia {nome} você nem parece ter {idade} anos!') 

def soma_e_multi(a,b,x):
    return a + b * x    

if __name__ == '__main__':
    saudacao('Ana', idade=30)
