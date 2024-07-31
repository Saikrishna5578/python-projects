
import random 
# library that we use in order to choose 
# on random words from a list of words 

name = input("Please enter your name to play the game: ") 
# Here the user is asked to enter the name first 

print("-------------------------------------\n***RULES***\n1. You have total of 12 chances to guess the charecters of the word\n2. The length of the word is displayed on the top of the game after you enter the game.\n--------------------------\nBEST OF LUCK!", name) 

words = ['rainbow', 'computer', 'science', 'programming', 
        'python', 'mathematics', 'player', 'condition', 
        'reverse', 'water', 'board', 'geeks'] 

# Function will choose one random 
# word from this list of words 
word = random.choice(words)
print("----------------------------")
print("LET'S BEGIN THE GAME")
print("It's a word of length:",len(word)) 

print("GUESS THE CHARECTERS\n") 

guesses = '' 

# any number of turns can be used here 
turns = 12


while turns > 0: 
    
    # counts the number of times a user fails 
    failed = 0
    
    # all characters from the input 
    # word taking one at a time. 
    for char in word: 
        
        # comparing that character with 
        # the character in guesses 
        if char in guesses: 
            print(char, end = " ") 
            
        else: 
            print("*", end = " ") 
            # for every failure 1 will be 
            # incremented in failure 
            failed += 1
            

    if failed == 0: 
        # user will win the game if failure is 0 
        # and 'You Win' will be given as output
        print("\n----------------------")  
        print("YEAH!!", name, "YOU  WON THE GAME") 
        
        # this print the correct word 
        print("----------------------")
        print("THE  WORD IS: ", word)
        print("----------------------") 
        break
        
    
    # if user has input the wrong alphabet then 
    # it will ask user to enter another alphabet 
    print("\n") 
    guess = input("GUESS A CHARECTER:")
    print("\n") 
    
    
    # every input character will be stored in guesses 
    guesses += guess 
    
    # check input with the character in word 
    if guess not in word: 
        
        turns -= 1
        
        # if the character doesn’t match the word 
        # then “Wrong” will be given as output 
        print("OOPS! WRONG") 
        print("------------------------")
        
        # this will print the number of 
        # turns left for the user 
        print("YOU HAVE", + turns, 'MORE GUESSES\n') 
        
        
        if turns == 0: 
            print("BETTER LUCK NEXT TIME")
            