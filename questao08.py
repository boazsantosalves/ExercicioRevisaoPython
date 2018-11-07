notas = 0
l_notas = []
l_contraria = []






while True:
  notaX= int(input("Digite uma nota: "))

  if notaX == -1:
    break
  
  notas += 1
  l_notas.append(notaX)
  l_contraria = l_notas[::-1]

print("")
print("A) Valores lidos: %d\n"%(notas))

print("B) Os valores na ordem que foram informados:")
for i in range(len(l_notas)):
  print(l_notas[i], end = " ")

print("")

print("")
print("C) Os valores na ordem inversa que foram informados um abaixo do outro:")
for j in range(len(l_contraria)):
  print(l_contraria[j], end = " ",)
  print("")

print("")
somaVetor = 0
for k in range(len(l_notas)):
  somaVetor += l_notas[k]

print("D) Soma dos valores dos elementos: %d\n" %(somaVetor))
print("E) Média dos valores do elementos: %d\n"%(somaVetor/len(l_notas)))

acimaMedia = 0
for l in range(len(l_notas)):
  if l_notas[l] > somaVetor/len(l_notas):
    acimaMedia +=1

print("F) Quantidade de valores acima da media: %d\n"%(acimaMedia))

abaixoSete = 0
for m in range(len(l_notas)):
  if l_notas[m] < 7:
    abaixoSete+=1

print("G) Quantidade de valores abaixo de sete: %d\n"%(abaixoSete))

print("H) Programa encerrado ☺")
