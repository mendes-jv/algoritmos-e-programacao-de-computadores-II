def palavras(nomearq):
    arq_entrada = open(nomearq, 'r')
    conteudo = arq_entrada.read()
    arq_entrada.close()
    tabela = str.maketrans('!,.:;?', 6*' ')
    conteudo = conteudo.translate(tabela)
    conteudo = conteudo.lower()
    return conteudo.split()

print(palavras('example.txt'))