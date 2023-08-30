from nltk import ngrams

sent = "This is a new message from the reptuted memer, laugh until you die"

n=6
wGram = ngrams(sent.split(),n)
for w in wGram:
    print(w)

sGram = ngrams(sent,n)
for c in sGram:
    print(c)
