import spacy
nlp = spacy.load('en_core_web_md')

#Examples of using spacy to find similarities between words 
#Example: 1
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print("Example1 : ")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# Cat and monkey seem to be similar because they are both animals;
# banana and monkey seem to be similar as the model puts together that bananas can be eaten by monkeys
# banana and cat does not have any significant similarity as they belong to different categories and there is 
# no significant relationship with one another


# Example: 2
word1 = nlp("fish")
word2 = nlp("water")
word3 = nlp("bottle")
print("\nExample2 : ")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# fish and water seems to be similar as fish lives in the water
# bottle and water seems to be similar as the bottle can be filled with water
# bottle and fish does not have any significant similarity as they significant relationship with one another


# Example to compare series of words with one another 
print("\nExample to compare series of words with one another: ")
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Example to ascertain similarities between longer sentences
print("\nExample to ascertain similarities between longer sentences: ")
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

'''If the file was run using 'en_core_web_sm' then any of the vector words would not be loaded and it would only use 
context-sensitive tensors so the result of the Token.similarity method will  not give useful similarity judgements. 
Therefore more advanced language model such as 'en_core_web_md' can be used to find better similarities and differences '''


