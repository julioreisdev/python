# r - leitura no início do arquivo
# r+ - leitura e escrita no começo do arquivo(sobreescreve o arquivo)
# w - escrita no começo(usado para criação de arquivos)
# a - escrita no fim do arquivo

def criaArquivo():
    try:
        arquivo = open('funcionarios.txt', 'w')
        arquivo.close()
    except:
        print("Erro ao criar arquivo.")
    else:
        print("Arquivo criado com sucesso.")

def escreveDados(lista):
    try:
        arquivo = open('funcionarios.txt', 'a')
        arquivo.write('\n'.join(lista))
    except:
        print("Não foi possível escrever no arquivo.")
    else:
        print("Escrita feita com sucesso.")

def lerDados():
    try:
        arquivo = open('funcionarios.txt', 'r')
        while True:
            palavra = arquivo.readline()
            print(palavra, end='')

            if palavra == '':
                break
        arquivo.close()
    except:
        print("Falha ao abrir arquivo.")
    print()


#criaArquivo()

#funcionarios = ["João Barbosa", "Alice Dias", "Miguel Freitas"]
#escreveDados(funcionarios)

lerDados()