cpf = input("CPF: ")
numerosCpf = ''

# Deixando somente números
for i in range(len(cpf)):
    if cpf[i] != '-' and cpf[i] != '.':
      numerosCpf = numerosCpf + cpf[i]

def verificaDigito(inicial, final):
  cont = 0
  valor = 0
  for i in range(inicial, final):
    valor = valor + int(numerosCpf[cont]) * i
    cont = cont + 1

  return ((valor * 10) * -1) % 11

def validacao():
  if verificaDigito(-10, -1) == int(numerosCpf[9]) and verificaDigito(-11, -1) == int(numerosCpf[10]):
    print("CPF VÁLIDO!")
  else:
    print("CPF INVÁLIDO!")

validacao()
