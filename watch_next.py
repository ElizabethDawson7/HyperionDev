'''SE T38 - Semantic Similarity (NLP)
Compulsory Task 2
'''
#=====Importing libraries===========
import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use. Remember to install this model by typing python -m spacy download en_core_web_md into your command line

#=====Reading in text file===========

movie_list = {} # making a dictionary
with open('movies.txt', 'r', encoding = 'utf-8') as movies_file: #reads the file
    for line in movies_file:
        (movie_title, description) = line.strip('\n').split(" :")
        movie_list[movie_title] = description


#=====The Movie to take as a parameter===========
just_watched = {'Planet Hulk': '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''}

#=====Function===========

def watch_next(desc):
    desc = nlp(desc)

    compare_similarity = 0
    highest_similarity = ''

    for key in movie_list:
        token = movie_list[key]
        token = nlp(token)
        if token.similarity(desc) > compare_similarity: # compare similarity syntax to previous highest similarity syntax
            compare_similarity = token.similarity(desc)
            highest_similarity = key # The name of the most similar film.

    return highest_similarity

just_watched_desc = just_watched['Planet Hulk'] # Get the description of Planet Hulk

most_similar = watch_next(just_watched_desc)
print(f"The most similar film to 'Plantet Hulk' is '{most_similar}'.")