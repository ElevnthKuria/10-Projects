from words import words
import random 
import string


def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  #letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed    


    lives = 26
    
    while len(word_letters) > 0 and lives > 0:
        #letters used
        #' '.join(['a', 'b', 'cd']) --> 'a b cd' 
        print("You have", lives, "lives left and You have used these letters: ", ' '.join(used_letters))
        
        #what current is (ie W - R D)

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet  - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print("Letter is not found")

        elif user_letter in used_letters:
            print("You have already used that character. Please Try again. ")
        else: 
            print("Invalid character. Please try again.")

#gets here when len(word_letter) == 0 OR when livves == 0

    if lives == 0:
        print("You died, sorry, the word was", word)
    print("The guessed word was", word, "!!")
hangman()
