from collections import defaultdict
from nltk import ngrams

def cal(cor):
    ngrams = defaultdict(int) # Stores the count of each n-gram
    context = defaultdict(int) # Stores the count of each n-gram context
   
    # Iterate over each sentence in the corpus
    for s in cor:
        words = s.split()

        #Iterate over each n-gram in the sentence
        for i in range(len(words) - 2):
            trigram = tuple(words[i:i+3]) # Create a trigram tuple
            ngrams[trigram] +=1 # Increment the count of the trigram
            context[trigram[:2]] +=1 # Increment the count of the context
    print(ngrams)
    print("----------------------------------------------------------")
    print(context)
    probabilities = defaultdict(float)

    # Calculate probabilities for each trigram using add-one smoothing (count+1)
    for trigram, count in ngrams.items():
        context_count = context[trigram[:2]] # Count of the context
        probabilities[trigram] = (count + 1) / (context_count + len(ngrams))

    return probabilities

# Sample input corpus
corpus=[
"I love to code",
"Python is a popular programming language",
"Coding is fun",
"I enjoy coding in Python",
"I love to dance"
]
# Calculate trigram probabilities using n-gram smoothing
tri_pro = cal(corpus)
# Print the probabilities
for t, p in tri_pro.items():
    print(f"Trigram: {t}, Probability: {p:.4f}")