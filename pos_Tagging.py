import nltk
from nltk import word_tokenize

def pos_tagg(tx):
    wrd = word_tokenize(tx)
    ps_tg = nltk.pos_tag(wrd)
    return ps_tg

qn = "I love to read Books"
for w,p in pos_tagg(qn):
    print(f"{w} - {p}")