import nltk
from nltk import word_tokenize

def pos_tagg(tx):
    wrd = word_tokenize(tx)
    ps_tg = nltk.pos_tag(wrd)
    return ps_tg
qn = "The clever fox escaped from the lion"
# for w,p in pos_tagg(qn):
#     print(f"{w} - {p}")
grmr = "NP: {<DT>?<JJ>*<NN>}"
chnk_parser = nltk.RegexpParser(grmr)
chnk = chnk_parser.parse(pos_tagg(qn))
print(chnk)
chnk.draw()