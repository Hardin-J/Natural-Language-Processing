import nltk
nltk.download('stopswords')
nltk.download('punkt')

from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords

# dt = "Everyone is a good of their own"
dt = input()

stp = set(stopwords.words('english'))
wrds = word_tokenize(dt.lower())
wrdFltr = []
for wrd in wrds:
    if wrd not in stp:
        wrdFltr.append(wrd)
print("Words=",wrds)
print("Stopwords=",stopwords)
print("Filtered words=",wrdFltr)
 