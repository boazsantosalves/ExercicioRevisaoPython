#Cardápio
print("CARNES DISPONÍVEIS\n")
print("File Duplo       Alcatra       Picanha\n")

#Valores a serem lidos
tipo = input("Qual tipo de carne você dejesa?\n")
tipo = tipo.lower()
quant = float(input("Qual quantidade(em kg) você deseja?\n"))
pagamento = input("Qual o tipo de pagamento?\n")
pagamento = pagamento.lower()
total = 0
desconto = 0


#Condições para cada tipo de carne

if tipo=="file duplo":
    if quant<=5:
        total = quant*4.90
    else:
        total = quant*5.80
    



if tipo=="alcatra":
    if quant<=5:
        total = quant*5.90
    else:
        total = quant*6.80




if tipo=="picanha":
    if quant<=5:
        total = quant*6.90
    else:
        total = quant*7.80

#Verificar se o cliente utilizou o cartão Tabajara

if pagamento=="cartao tabajara":
    desconto = total*0.05
    valor_pagar = total-desconto

if pagamento!="cartao tabajara":
    valor_pagar = total



#Cuidado do cumpom fiscal

print("O tipo de carne foi: %s"%(tipo))
print("A quantidade de carne foi: %.1f"%(quant))
print("O preço total foi: R$ %.2f"%(total))
print("O valor do desconto foi: R$ %.2f"%(desconto))
print("O valor a pagar é: R$ %.2f"%(valor_pagar))

    
    
