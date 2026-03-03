a=input().split()
synonyms = {
    "big": "large",
    "small": "tiny",
    "fast": "quick",
    "slow": "sluggish",
    "happy": "joyful",
    "sad": "unhappy",
    "angry": "furious",
    "good": "great",
    "bad": "awful",
    "hot": "warm",
    "cold": "chilly",
    "smart": "clever",
    "stupid": "dumb",
    "easy": "simple",
    "hard": "difficult",
    "friend": "buddy",
    "enemy": "foe",
    "child": "kid",
    "dog": "puppy",
    "cat": "kitten"
}
b=[]
for i in range(len(a)):
    if a[i] in synonyms:
        b.append(synonyms[a[i]])
    else:
        b.append(a[i])
print(' '.join(b))