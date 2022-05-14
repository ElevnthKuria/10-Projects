import string
import random
from graph import Graph
from graph import Vertex


#what do we do here?
def get_words_from_text(text_path):
    with open(text_path, 'rb') as file:
        text = file.read().decode("utf-8")

        text = ' '.join(text.split()) # turn whitespace into just spaces
        text = text.lower() # makes lowercase to compare

        #Remove all punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split() #split on spaces again

    words = words[:1000]

    return words

def make_graph(words):
    g = Graph()

    previous_word = None

    #for each word
    for word in words:
        #check that the word is in the graph, if not add it
        word_vertex = g.get_vertex(word)
    #if there was a previous word, then add an edge if it does not already exist
    #in the graph, otherwise increment weight by 1
        if previous_word:
            previous_word.increment_edge(word_vertex)
        
    #set our word to the previous word and iterate
        previous_word = word_vertex


    #now remember that we want to generate the probability mappings before composing
    #this is a great place to do it before we return the graph object
    g.generate_probability_mappings()

    return g
   
def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words)) # pick a random word to start!
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition

def main():
    #step1: get words from text
    words = get_words_from_text('texts/hp_sorcere_stone.txt')
    #step2: make graph using those words
    g = make_graph(words)
    #step3: get the next word for x number of words(defined by user)

    #step4: show the user!
    composition = compose(g, words, 100)
    print(' '.join(composition)) #returns a string, where all the words are separated by a space!

if __name__ == '__main__':
    main()