#   Com as tuplas dos 20 primeiros colocados da Liga Juvenil de Futebol Amador,
#   ordenados de acordo com sua colocação, escreva na tela:
#       a) Os 5 primeiros times.
#       b) Os últimos 4 colocados.
#       c) Times em ordem alfabética.
#       d) Em que posição está o time da Chapecoense.

times = ('Palmeiras', 'Santos', 'Flamengo', 'Atlético', 'Internacional',
         'Atlético-PR', 'Botafogo', 'Goias', 'Corinthians', 'Grêmio',
         'Bahia', 'São Paulo', 'Ceará SC', 'Fortaleza', 'Vasco da Gama',
         'Cruzeiro', 'Fluminense', 'Chapecoense', 'CSA', 'Avaí')

print("\n",times[0:5])
print("\n",times[16:20])
print("\n", sorted(times))
print("\n", times.index('Chapecoense'))