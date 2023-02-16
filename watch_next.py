import spacy # importing spacy
nlp = spacy.load('en_core_web_md')

def similar_movie(description,movie_list):
    '''
    Function to find what to watch next based on the word
        vector similarity of the description of movies

    Args: description : description of the last seen movie(str)
          movie_list  : List of movies from the text file\database (str)

    Returns: highest_similarity : Value caluculated by .similarity() (float)
             most_similarmovie : movie corresponding to highest_similarity (str)

    '''
    model_movie = nlp(description)
    highest_similarity = 0
    most_similarmovie = ''

    for sentence in movie_list:
        doc_sentence = nlp(sentence)
        similarity = doc_sentence.similarity(model_movie)
        print(sentence + " - ", similarity)
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similarmovie = sentence
    return(highest_similarity,most_similarmovie)


with open('movies.txt', 'r', encoding='utf-8') as f:
    ''' Reads from the movies.txt and creates a list of movies'''
    temp = f.readlines()
    movie_list = []
    for string in temp:
        movie_list.append(string.strip()) 

'''The description of the last movie watched'''
description = "\n".join(['''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''])

highest_similarity,most_similarmovie = similar_movie(description,movie_list)
print(f"\nThe most similar movie is {most_similarmovie}") 
'''Prints the most similar movie based on the description the movie last watched'''