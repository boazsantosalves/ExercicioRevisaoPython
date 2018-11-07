l1 = []
l2 = []
l3 = []
print("Digite números para compor a sua primeira lista")
for i in range(0,10):
    n = int(input())
    l1.append(n)

print("Digite números para compor a sua segunda lista")
for i in range(0,10):
    n = int(input())
    l2.append(n)


for i in range(0,10):
    a = l1[i]
    b = l2[i]
    l3.append(a)
    l3.append(b)

print(l3)
    
    
