'''
Kenneth Eze

Dictionary:

Attributes of Database: Word, Definition, POS

'''
import sqlite3
from time import sleep
import tkinter as tk

# adding word function (takes in a string)
def add_word(word):
    with sqlite3.connect('dictionary.db') as conn:
        cursor = conn.cursor()
        
        print("----------------------------------------------------------------------")
        print(f"Please enter the definition of {word}: ")
        print("----------------------------------------------------------------------")
        definition = input()
        if definition == "exit":
            return
        print("----------------------------------------------------------------------")
        print("What part of speech is this word?")
        print("----------------------------------------------------------------------")
        POS = input()
        if POS == "exit":
            return
        
        print("\n")
        confirmation = input(f"Are you sure you'd like to add \033[1m{word}\033[0m to the \033[1mDICTIONARY OF LIFE?\033[0m y/n --> ")
        if confirmation == "y":
            cursor.execute('''
                        INSERT INTO words (
                            word,
                            POS,
                            definition)
                        VALUES (?, ?, ?);
                            ''', (word, POS, definition))
            print("\n")
            sleep(1.5)
            print(f'*** \033[1m{word}\033[0m has successfully been added to the dictionary! ***')
            conn.commit()
            cursor.close()
        else:
            return
        
# deleting word function
def delete_word(): 
    # print("Hello!")
    with sqlite3.connect('dictionary.db') as conn:
        cursor = conn.cursor()
        
        while True:
            print("What word would you like to delete?  ")
            print("\n")
            delete = input("Please type a word or type 'exit' to quit: ")
            
            if delete == 'exit':
                break
            
            delete = delete.lower()
            delete = delete[0].upper() + delete[1:]
            
            definition = cursor.execute(f"SELECT word FROM words WHERE word = '{delete}'").fetchall()
            
            # check to see if word exists
            if (len(definition) < 1):
                print("----------------------------------------------------------------------")
                print(f"{delete} is not in the \033[1mTHE DICTIONARY OF LIFE\033[0m!")
                print("----------------------------------------------------------------------")
            else:
                print(f"Are you sure you want to remove {delete} from \033[1mTHE DICTIONARY OF LIFE\033[0m? y/n ---> ")
                idk = input()
                if (idk == 'y'):
                    cursor.execute(f'''
                                    DELETE FROM words WHERE word = '{delete}';
                                        ''')
                    print("----------------------------------------------------------------------")
                    print(f'{delete} has been deleted!')
                    print("----------------------------------------------------------------------")
                else:
                    return
        
        conn.commit()
        cursor.close()

# takes in word, returns definition from database
def dictionary_app(word):
    with sqlite3.connect('dictionary.db') as conn:
        cursor = conn.cursor()
        
        word = word.lower()
        word = word[0].upper() + word[1:] # since the dataset is case sensitive, capitalize the word
        
        definition = cursor.execute(f"SELECT definition FROM words WHERE word = '{word}';").fetchall()
        
        # definition
        print(f"\033[1m{word}\033[0m") # looked up ANSI codes for making font bold
        if len(definition) < 1: # if the word is not in the database
            print(f"\033[1m{word} is not in the dictionary!\033[0m")
            print("----------------------------------------------------------------------")
            adding = input(f"Would you like to add \033[1m{word}\033[0m to the dictionary? y/n ---> ")
            print("----------------------------------------------------------------------")
            while (adding != "n"):
                if (adding == "y"):
                    add_word(f"{word}")
                    adding == "n"
                print("----------------------------------------------------------------------")
                return
            print(f"Updating ... ")
            sleep(2)
            print("Updated.")
        
        # print remaining definitions
        if len(definition) >= 1:        
            print("--→ ", definition[0][0])
            print("----------------------------------------------------------------------")
            
            if len(definition) > 1:
                print("\033[1mSome other definitions include:\033[0m")
                for words in definition[1:]:
                    print("○", words[0])
                print("----------------------------------------------------------------------")
            
        cursor.close()
    return

# main program
print("----------------------------------------------------------------------")
print("\033[1mTHE DICTIONARY OF LIFE\033[0m")
print("\n")
print("***Tip: to exit any function, please type 'exit'! Enjoy!")
print("\n")

print("----------------------------------------------------------------------")

while True:
    print("What would you like to do? \n\n 1. Search for Word \n 2. Delete Word ")
    print("\n")
    init = input("Please select 1, 2, or type 'exit' to quit: ")
    print("----------------------------------------------------------------------")
    
    if init == "exit":
        print("+++ Come back anytime, Goodbye! +++")
        print("----------------------------------------------------------------------")
        break 
    
    if init == "1":
        while True:
            user = input("What word would you like to look for? (type 'exit' to return to the main menu): ")
            if user == 'exit':
                break  
            dictionary_app(user)
            print("loading ...")
            sleep(2)
            print("----------------------------------------------------------------------")
        print("Loading main menu...")
        sleep(1.5)
        print("----------------------------------------------------------------------")
    elif init == "2":
        delete_word()
        print("Loading main menu...")
        sleep(1.5)
        print("----------------------------------------------------------------------")
    else:
        print("Invalid selection, please try again.")
        print("----------------------------------------------------------------------")