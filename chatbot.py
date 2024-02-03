import nltk
nltk.data.path.append("/usr/nltk_data")  # Set the path to the NLTK data directory
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import streamlit as st


#les fonction sont les memes que dans le cours sauf au niveau de la fonction get_most_relevant_sentence()


with open('C:/Users/ass85/PycharmProjects/chatbot_checkpoint.py/.venv/Scripts/9782253168522.txt', 'r', encoding='utf-8') as f:
    data = f.read().replace('\n', ' ')
sentences=sent_tokenize(data)

# fonction pour faire le prétraitement des données
def preprocessing(sentence):
  words=word_tokenize(sentence)
  words=[word.lower() for word in words if word.lower() not in stopwords.words("french") and word not in string.punctuation]
  lemma=WordNetLemmatizer()
  words=[lemma.lemmatize(word) for word in words]
  return words
#corpus est une matrice qui contient les mots du texte ayant subi le preprocessing(lemmatisation, tokénisation et supression des stopwords)
corpus = [preprocessing(sentence) for sentence in sentences]

#sentences2 contient les mots du texte provenant de sentence sans modification
sentences2=[word_tokenize(sentence) for sentence in sentences]

# fonction pour choisir la réponse à la question en calculant la similarité
def get_most_relevant_sentence(query):

    # Preprocess the query
    query = preprocessing(query)

    # Compute the similarity between the query and each sentence in the text
    max_similarity = 0
    most_relevant_sentence = ""
    max_similarity2 = 0
    most_relevant_sentence2 = ""
    b=0
    ab=0
    for sentence in corpus:
        similarity = len(set(query).intersection(sentence)) / float(len(set(query).union(sentence)))
        if similarity > max_similarity:
            max_similarity = similarity
            ab=b
        b += 1
    g = "" # cette variable contiendra la phrase choisie

    # je prends les mots de sentences qui appartiennet à la meme phrase qu corpus et je les regroupe dans une phrase pour les mettre dans la variable g
    for a in sentences2[ab]:
        g += a + " "
    most_relevant_sentence = g
    return most_relevant_sentence


def chat(question):

    # Find the most relevant sentence
    most_relevant_sentence = get_most_relevant_sentence(question)

    # Return the answer
    return most_relevant_sentence








