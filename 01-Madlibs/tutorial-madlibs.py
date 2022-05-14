# Mad Libs is a phrasal template word game. That you fill in blank spaces with appropriate word which can be an adjective, noun, etc.
# It is considered a word play game

#none: This is a small program that only includes one player. Other madlibs may include multiple players.

adj = input("Adjective: ")
verb = input("Verb: ")
noun = input("Noun: ")
noun2 = input("Plural Noun: ")

madlib = (f'If you want to get {adj} code. You must first keep {verb} and practicing computer programs. A {noun} is a set of instructions that are used to perform operations in a {noun2}')

print(madlib)


import random

if __name__ == "__main__":
    m = random.choice()
    m.madlib()
    