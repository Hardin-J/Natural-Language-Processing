import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

Sent = "Gaming is one the best entertainment that entertains players when they plays the game play very much"
words = word_tokenize(Sent)
for word in words:
    print(word + ":",ps.stem(word))