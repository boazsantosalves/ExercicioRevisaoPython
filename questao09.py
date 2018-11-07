#Definindo as variáveis que auxiliarão no nosso programa
veiculos = []
consumos = []
litros_10km = []
consumo10km = 0
precos = []
preco_Gasolina = 0



#Lendo os dados
for i in range(1,6):
  veiculoX = str(input("Informe o veiculo %d: "%(i)))
  consumoX = float(input("Informe o consumo do veiculo %d: "%(i)))
  print("")

  veiculos.append(veiculoX)
  consumos.append(consumoX)

  consumo10km = float(1000/consumoX)
  litros_10km.append(consumo10km)

  precoGasolina = float(consumo10km*3.5)
  precos.append(precoGasolina)

#Cuidando do relatório
print("Relatorio:\n")
print("Modelo        KM/L         1000KM         PREÇO")
for i in range(5):
  print("%s ------ %.1f ------ %.1f litros ----- R$ %.2f" %(veiculos[i], consumos[i], litros_10km[i], precos[i]))

print("")

menorConsumo = min(litros_10km)
consumoCarro = 0
melhorConsumo = 0

for j in range(len(litros_10km)):
  consumoCarro = litros_10km[i] 

  if consumoCarro == menorConsumo:
    melhorConsumo = i

print("O menor consumo é do %s"%(veiculos[melhorConsumo]))
