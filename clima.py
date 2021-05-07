#Sugestões para o Clima:

horario = 'Manhã'
clima = 'Ensolarado'
temperatura = 'Quente'
    
if horario == 'Manhã' or horario == 'Tarde':
    if clima == "Ensolarado" and temperatura == 'Quente':
        print("Uma piscina cairia bem.")
            
    if(clima == 'Ensolarado' or clima == 'Nublado') and (temperatura == 'Amena' or temperatura == 'Frio'):
        print('Seria legal praticar algum esporte.')
            
    if clima == 'Chuvoso':
        print('Aproveite para treinar seu Python.')
else:
    if clima == 'Chuvoso':
        print('Que tal um filme, série ou jogatina?')
    else:
        print('Um jantar fora cairia bem...')
