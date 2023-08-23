import nltk
nltk.download('punkt')

def tok_txt(txt):
    tk = nltk.word_tokenize(txt)
    return tk

sm = ["I am a student","I play Cricket","I love playing music"]
print("-------------------------")
for i in sm:
    print("Sample text=",i)
    tk = tok_txt(i)
    print("The tokens are:",tk)
    print("-------------------------")