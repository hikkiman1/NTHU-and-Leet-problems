a=input()
l=len(a)
if '.' in a and l>=6:
    print(a)
elif l>=5:
    print(a)
elif '.' in a:
    print(a+'0'*(6-l))
else:
    print('%05d'%int(a))