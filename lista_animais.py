#Lista de animais de estimação:
    
animais = []
animal = input('Digite o nome do(s) seu(s) animal(is) de estimação ou digite 0 se não tiver nenhum: ')

while animal != '0':
        especie = input('Digite a espécie desse animal: ')
        animais.append([animal, especie])
        animal = input('Se tiver mais animais de estimação, digite o nome dele, ou digite 0 se não tiver: ')
    
    
if len(animais) == 0:
    print('\n\nVocê não tem animais de estimação.')
    
else:
    print('\n\nVocê tem os seguintes animais: ')
    for animal in animais:
        print('- Nome:', animal[0], '| Espécie:', animal[1])
