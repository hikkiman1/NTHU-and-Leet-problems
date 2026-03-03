a=input()
x=0
e=0
for i in a:
    if e%2==0:
        x=x+int(i)
    e+=1
print(x)