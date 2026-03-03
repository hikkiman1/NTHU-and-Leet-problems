a=input()
i,b=map(int,input().split())
str_list=list(a)
del str_list[i:(b+1)]
print("".join(str_list),a[i:(b+1)],sep='')