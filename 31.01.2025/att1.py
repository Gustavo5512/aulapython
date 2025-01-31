n= []
s=0
i=0
while True:
    n.append(int(input('Digite um numero ')))
    if n[s]==0:
        break
    s+=1
for  i in range(0,s):
    print(n[s])