#Optimized one, adding full sentence before jump to the next row
def pun(sentences: list, queries: list)->None:
    #Write your code here
    for i in queries:
        DADJOKE=[]
        for k in range(len(sentences)):
            row=i[0]
            col=i[1]
            if row >= len(sentences):
                break
            if col < len(sentences[row]):
                DADJOKE.append(sentences[row][col])
            else:
                DADJOKE.append(sentences[row][-1])
            i[0]+=1
        print(' '.join(DADJOKE))
(line, query) = map(int, input().split())
sentences = []
queries = []
for i in range(line):
    sentences.append(input().split())
for i in range(query):
    queries.append(list(map(int, input().split())))
pun(sentences, queries)