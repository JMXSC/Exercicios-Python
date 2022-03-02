''' Exercício 73 – Tuplas com Times de Futebol

A) Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
B) Os 5 primeiros times;
C) Os últimos 4 colocados;
D) Times em ordem alfabética;
E) Em que posição está o time da Chapecoense.'''

times = ('Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
         'Fluminense', 'America-MG', 'Atletico-GO', 'Santos','Ceara', 'Internacional', 'São Paulo',
         'Atletico-PR', 'Cuiaba','Juventude', 'Gremio', 'Bahia', 'Sport', 'Chapecoense')

print(f' Os 5 primeiros colocados da tabela são: {times[0:6]}.\n',
      f'Os 4 últimos colocados da tabela são: {times[16:20]}.\n',
      f'O time da Chapecoense está na {times.index("Chapecoense")+1}° posição.')
