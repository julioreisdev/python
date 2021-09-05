def retornaSoma ():
  a = int(input("Digite um número:"))
  b = int(input("Digite um número:"))

  print(a+b)
  return a + b

def precoProduto():
  preco = int(input("Digite o preço do produto:"))
  taxa = int(input("Digite a taxa do produto:"))

  print(preco + (taxa/100*preco))

def listaOrdenada():
  lista = []
  for i in range(3):
    lista.append(int(input("Digite um número:")))

  listaEmOrdem = sorted(lista)
  if listaEmOrdem == lista:
    print("Lista ordenada!")
    return True
  else:
    print("Lista não ordenada!")
    return False

def notasAlunos():
  notas = []

  while True:
    escolha = int(input("Digite a nota do aluno:"))
    if escolha == -1:
      break
    notas.append(escolha)

  print(len(notas))
  print(notas)

  for i in range(len(notas)):
    print(notas[i])

  somaNotas = 0
  for i in notas:
    somaNotas += i
  print(somaNotas)

  print(somaNotas/len(notas))

  for i in range(len(notas)):
    if notas[i] > somaNotas/len(notas):
      print(notas[i])

  for i in range(len(notas)):
    if notas[i] < somaNotas/len(notas):
      print(notas[i])


while (True):
  escolha = input("\n1 - Retorna soma\n2 - Preço produto\n3 - Lista ordenada?\n4 - Notas alunos\n0 - Sair\nDigite: ")

  if (escolha == '1'):
    retornaSoma()
  elif (escolha == '2'):
    precoProduto();
  elif (escolha == '3'):
    listaOrdenada()
  elif (escolha == '4'):
    notasAlunos()
  elif (escolha == '0'):
    print("____________")
    print("|Encerrando!|")
    print("____________")
    break
