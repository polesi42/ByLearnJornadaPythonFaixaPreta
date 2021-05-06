#Código para verificação da aprovação de um aluno usando função

nota1 = 7.5
nota2 = 4.8

#Definimos aqui o que é a função verificar uma aprovação

def verificar_aprovacao() :
    media = calcular_media([nota1, nota2)]
    
    if media >=6:
       print("O aluno foi aprovado!")
    else:
       print("O aluno foi reprovado!)
       
#definimos aqui a função calcular a média

def calcular_media(notas):
    quantidade = len(notas)
    
    soma=0
    for nota in notas
        soma = soma + nota
    media = soma / quantidade
    
    return media
    
# Agora basta chamar a função verificar aprovação


verificar_aprovação()
