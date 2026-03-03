def count(inStr: str)->dict:
    #Write your code here
    statement=inStr.split()
    counted={}
    for i in range(len(statement)-1):
        repeat=0
        if counted.get(statement[i])==None:
            for k in range(i,len(statement)):
                if statement[i]==statement[k]:
                    repeat+=1
            counted[statement[i]]=repeat   

    return counted


print(sorted(count(input().lower()).items()))