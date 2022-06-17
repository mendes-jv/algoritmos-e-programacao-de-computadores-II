def troca_pu(lista):
    lista[0], lista[-1] = lista[-1], lista[0]


ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']

troca_pu(ingredientes)
print(ingredientes)
