print('Bem vindos ao site da autoescola')

def validar_idade(idade):
    if idade< 18:
        print('Desculpe, você não tem idade para prosseguir,', nome)
        return False
    else:
        print('Ótimo, podemos prosseguir,', nome)
        return True

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

def escolher_cnh():
    print('Digite uma das opções abaixo: ')
    print('1 - Carro\n2 - Moto\n3 - Carro e moto')
    
    return int(input())

def calcular_preco(escolha):
    valor_carro = 1500
    valor_moto= 1000
    
    if escolha == 1:
        return valor_carro
    elif escolha == 2:
        return valor_moto
    else:
        return valor_carro + valor_moto
    
def desconto(valor):
    return valor - (valor * 0.1)

if validar_idade(idade):
    escolha = escolher_cnh()
    
    print('\nPerfeito! Vou calcular o valor.\n')
    valor = calcular_preco(escolha)
    
    print (nome+',', 'o valor total é de', valor, 'reais.')
    print('Mas vou ver com meu gerente se posso dar um desconto...')
    valor = desconto(valor)
    
    print('\nCom desconto eu consigo fazer por', valor, 'reais')
    
    print('Te interessa?\n 1 - Sim\n 2 - Não')

interesse = int(input())
if interesse == 1:
            print('\nPerfeito! Começaremos amanhã!')
else:
            print('\nTudo bem:(\nMe avise se mudar de ideia.')