cont = 0

a = input("Telefonou para a v�tima?")
a = a.lower()
if a=="sim":
    cont = cont+1

b = input("Esteve no local do crime?")
b = b.lower()
if b=="sim"
    cont = cont+1

c = input("Mora perto da v�tima?")
c = c.lower()
if c=="sim":
    cont = cont+1

d = input("Devia para a v�tima?")
d = d.lower()
if d=="sim":
    cont = cont+1

e = input("J� trabalhou com a v�tima?")
e = e.lower()
if e=="sim":
    cont = cont+1

if cont==2:
    print("Suspeita")

if cont==3 or cont==4:
    print("C�mplice")

if cont==5:
    print("Assasino")

else:
    print("Inocente")
