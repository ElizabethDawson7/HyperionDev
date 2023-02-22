'''SE T38 - Semantic Similarity (NLP)
Compulsory Task 1
'''

#!pip install spacy
# python3 -m spacy download en_core_web_md  
# OR
#python -m spacy download en_core_web_md
#!pip install "https://github.com/explosion/spacy-models/releases/download/en_core_web_md-2.2.5/en_core_web_md-2.2.5.tar.gz"

#=====importing libraries===========
import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use. Remember to install this model by typing python -m spacy download en_core_web_md into your command line


import spacy
nlp = spacy.load('en_core_web_md')

print('''Example 1''')
word1 = nlp('cat')
word2 = nlp('monkey')
word3 = nlp('banana')

print('Similarity between words')
print(f'{word1} and {word2}: {word1.similarity(word2)}') # 0.5929930274321619
print(f'{word3} and {word2}: {word3.similarity(word2)}') # 0.40415016164997786
print(f'{word3} and {word1}: {word3.similarity(word1)}') # 0.22358825939615987

print('''My Example''')
word1 = nlp('cat')
word2 = nlp('mouse')
word3 = nlp('cheese')

print('Similarity between words')
print(f'{word1} and {word2}: {word1.similarity(word2)}') # 0.5929930274321619
print(f'{word3} and {word2}: {word3.similarity(word2)}') # 0.40415016164997786
print(f'{word3} and {word1}: {word3.similarity(word1)}') # 0.22358825939615987


print('''Example 2''')
tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print('''Example 3''')
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
