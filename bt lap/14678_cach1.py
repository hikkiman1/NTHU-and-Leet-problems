a=input()
x=0
y=len(a)-1
while x<y:
    if a[x]==a[y]:
        x+=1
        y-=1
    else:
        print("No")
        break
if x>=y:
    print("Yes")