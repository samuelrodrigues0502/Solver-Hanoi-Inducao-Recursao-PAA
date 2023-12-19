def geraMatriz(qtd):

  matrizTorre = [[],[],[]]
  for i in range(qtd, 0, -1):
    matrizTorre[0].append(i)

  return matrizTorre

def moveDisco(ori, dest, matTorre):

  #remove o que está no topo da lista
  discoMovido = matTorre[ori].pop()
  #adiciona o disco movido no pino de destino
  matTorre[dest].append(discoMovido)
  if dest == 0:
    pino ='A'
  elif dest == 1:
    pino = 'B'
  else:
    pino = 'C'
  print(f'\nMove disco {discoMovido} para pino {pino}')
  print(matTorre)

def resolve(qtd, pinOri, pinAux, pinDest, matTorre):

  #Quando há somente um disco(Caso base) no pino,
  #simplesmente o movemos do disco origem para seu destino
  if qtd == 1:
    moveDisco(pinOri, pinDest, matTorre)
  else:
    #Caso haja mais de um disco no pino,
    #utilizamos de recursão para dividir
    #a torre em subtorres e resolver de forma indutiva

    #Move qtd-1 discos(subtorre) do pino origem para o
    #pino auxiliar ao fim da recursão
    resolve(qtd - 1, pinOri, pinDest, pinAux, matTorre)

    #Move o disco da base da subtorre atual para o pino destino atual
    moveDisco(pinOri, pinDest, matTorre)

    #Move o restante de discos da subtorre atual para o
    #pino destino ao fim da recursão
    resolve(qtd - 1, pinAux, pinOri, pinDest, matTorre)

def torre(qtdDisco, pinOri, pinAux, pinDest):

  matTorre = geraMatriz(qtdDisco)
  print(matTorre)
  resolve(qtdDisco, pinOri, pinAux, pinDest, matTorre)

qtdDisco = int(input('Qtd de discos: '))
torre(qtdDisco, 0, 1, 2)