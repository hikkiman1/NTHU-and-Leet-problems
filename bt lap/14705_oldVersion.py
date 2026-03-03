#Old code, this one add the each word one by one to all row from first collumn to last collumn

def pun(sentences: list, queries: list)->None:
    #Write your code here
    DADJOKE=[]
    for i in range(len(queries)):
            DADJOKE.append([])
    for k in range(len(sentences)):
        for i in range(len(queries)):
            
            if queries[i-1][0]==len(sentences):
                break
            elif queries[i-1][1]>=len(sentences[queries[i-1][0]]):
                DADJOKE[i-1].append(sentences[queries[i-1][0]][-1])
            else:
                DADJOKE[i-1].append(sentences[queries[i-1][0]][queries[i-1][1]])
        for i in range(len(queries)):
            queries[i-1][0]+=1
    for i in range(len(DADJOKE)):
        print(' '.join(DADJOKE[i]))

(line, query) = map(int, input().split())
sentences = []
queries = []
for i in range(line):
    sentences.append(input().split())
for i in range(query):
    queries.append(list(map(int, input().split())))
pun(sentences, queries)
