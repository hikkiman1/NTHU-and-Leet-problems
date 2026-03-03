h, v, a = map(int,input().split())
x = (v-(v**2-4*(-0.5*a)*(h-5500))**(1/2))//(2*(-0.5*a))
print(int(x))