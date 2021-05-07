#Código criado no curso Jornada Faixa Preta - ByLearn

#Lista de Compras




frutas = ['Maça', 'Banana', 'Pera', 'Uva']
guloseimas = ['Biscoito', 'Batata', 'Fini', 'Chocolate' ]
comidas = ['Arroz', 'Feijão', 'Carne']
bebidas = ['Refrigerante', 'Suco de Laranja', 'Água']


categorias = ['Frutas', 'Guloseimas', 'Comidas', 'Bebidas']


compras = [frutas, guloseimas, comidas, bebidas]

for indice, categoria in enumerate(categorias):
  print('Você precisa comprar', len(compras[indice]), categoria+':')
  for compra in compras[indice]:
    print('-', compra)
