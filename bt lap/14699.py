a=int(input())
b=int(input())
c=int(input())
d=0
e=0
if b==1:
    e=c
elif b-2>6 and a%4==0:
    e=31*4+30*2+29+31*(b-8)-1*((b-8)//2)
elif b-2>6:
    e=31*4+30*2+28+31*(b-8)-1*((b-8)//2)
elif b==2:
    e=31*(b-1)-1*((b-1)//2)+c
elif a%4==0:
    e=31*(b-1)-1*((b-1)//2)-1+c
else:
    e=31*(b-1)-1*((b-1)//2)-2+c
if a<1970:
    print(0)
else:
    for i in range(1970,a):
        if i%4==0:
            d+=1
    print(d*366+(a-1970-d)*365+e)