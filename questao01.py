nota1 = float(input("Digite a primeira nota"))    
nota2 = float(input("Digite a segunda nota"))
nota3 = float(input("Digite a terceira nota"))
media = (nota1 + nota2 + nota3)/3

if media>=7:
    print("Aprovado, sua m�dia foi: %d" %(media))

if media<7:
    print("Reprovado, sua m�dia foi: %d" %(media))

if media==10:
    print("Aprovado com Distin��o")