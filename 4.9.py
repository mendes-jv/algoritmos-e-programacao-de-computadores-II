def meu_grep(txt, palavra):
    arquivo = open(txt)
    for linha in arquivo:
        if palavra in linha:
            print(linha, end='')


meu_grep('example.txt', 'lista')
