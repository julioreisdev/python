listaUsers = []

def inserirFinal(listaUsers):
  nome = input("\nNome de usuário: ")
  listaUsers.append(nome)
  print(nome + " adicionado(a)\n")

def inserirInicio(listaUsers):
  nome = input("\nNome de usuário: ")
  listaUsers.insert(0,nome)
  print(nome + " adicionado(a)\n")

def deletar(listaUsers):
  if (listaVazia(listaUsers)):
    print()
  else:

    id = input("\nID do usuário: ")
    print(listaUsers[int(id)] + " deletado(a)")
    listaUsers.pop(int(id))

def buscaNome(listaUsers):
  nome = input("\nDigite o nome p/ busca:")
  if (nome in listaUsers):
    print(" _______________________________")
    print("|" + nome + " está na lista.    |")
    print(" _______________________________")
  else:
    print(" _______________________________")
    print("|" + nome + " não está na lista.|")
    print(" _______________________________")

def consultarId(listaUsers):
  if (listaVazia(listaUsers)):
    print()
  else:

    print('___________________________________')
    for i in range(len(listaUsers)):
      print(listaUsers[i] + ", ID - " + str(i))
    print('___________________________________')

def imprimirUsers(listaUsers):
  if (listaVazia(listaUsers)):
    print()
  else:

    listaUsers.sort(key=str.lower)

    print('___________________________________')
    for i in range(len(listaUsers)):
      print(listaUsers[i])
    print('___________________________________')

def listaVazia(listaUsers):
  if (len(listaUsers) == 0):
    print("_____________________________")
    print("|Não há usuários cadastrados.|")
    print("_____________________________\n")
    return True

while (True):
  escolha = input("\n1 - Inserir usuário no início\n2 - Inserir usuário no fim\n3 - Consultar id do usuário\n4 - Deletar usuário(id)\n5 - Imprimir lista de usuários\n6 - Buscar nome\n0 - Sair\nDigite: ")

  if (escolha == '1'):
    inserirInicio(listaUsers)
  elif (escolha == '2'):
    inserirFinal(listaUsers)
  elif (escolha == '3'):
    consultarId(listaUsers)
  elif (escolha == '4'):
    deletar(listaUsers)
  elif (escolha == '5'):
    imprimirUsers(listaUsers)
  elif(escolha == '6'):
    buscaNome(listaUsers)
  elif (escolha == '0'):
    print("____________")
    print("|Encerrando!|")
    print("____________")
    break
