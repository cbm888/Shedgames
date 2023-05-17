import random
import shedman_visual
import words

def random_city():
    list = ["back to Alvin", "to Crosby", "to Conroe", "to Bastrop", "to Lockhart", "to Pflugerville with Goss"]
    num = random.randint(0,len(list))
    return list[num]


def Alvinite_status():
    list2 = ["Midlane Ashe", "Broken arm", "methed up", "Talk of Alvin valued contributor", "AHS tree lover", "Captain D's rewards member", "Earl Humbird campaign manager", "Joel Castro's scorned ex-lover"]
    random_status = random.choice(list2)
    return random_status
 

def get_valid_word(list):
    invalid_letter = False
    validated_word = False
    while not validated_word:
        word = list[random.randint(0,len(list))]
        for char in word:
            if char == " " or char == "-":  
                invalid_letter = True
                break      
        if invalid_letter:
            continue
        else:
            return word   

def word_display(word,word_letters):
    display = ""
    for letter in word:
        if letter not in word_letters:
            display += letter
        else:
            display += "_"
    return display

gallows = shedman_visual.lives_visual_dict 
imported_word_list = words.words
word = get_valid_word(imported_word_list).upper()
word_letters = set(word.upper())
alphabet = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
used_letters = []
lives = 7
winner = False
winner_location = random_city()
alvinite_status = Alvinite_status()

while lives > 0 and winner == False:
    print(f"Alvinite Status: {alvinite_status}" )
    print(gallows[lives])
    print("You have " + str(lives) + " meth hits left.")
    display_word = word_display(word.upper(), word_letters)
    print("Current word: " + display_word)
    print("You have used the letters: " + str(used_letters))
    input_valid = False
    while not input_valid:
        user_letter = input("Please guess a letter: ").upper()
        if len(user_letter) != 1: 
            print("I know this game might not be obvious because you were put through the AISD school system, but this must be a single character.")
            print(f"Alvinite Status: {alvinite_status}" )
            continue
        elif user_letter not in alphabet:
            print("Must be valid letter. They recently added letters to the Alvin Elementary School curriculum, but may not have taught them while you were there.")
            print(f"Alvinite Status: {alvinite_status}" )
            continue
        elif user_letter in used_letters:
            print("You have already used this letter. Please try again. This is not like the school board elections where you choose the same thing every time forever.")
            print(f"Alvinite Status: {alvinite_status}" )
            continue
        elif user_letter != word_letters:
            print("You really are from Alvin, huh?")
            print(f"Alvinite Status: {alvinite_status}" )
        else:
            input_valid = True
    if user_letter in word.upper():
        used_letters.append(user_letter)
        word_letters.remove(user_letter)
        print("You guessed correctly! Lets get out the grill and celebrate.")
    else: 
        used_letters.append(user_letter)
        lives -= 1
        print("The letter is not in the word. Spicy spaghetti for your kids. Please try again.")
    display_word = word_display(word.upper(), word_letters)
    if "_" not in display_word:
        winner = True
        print(f"Congratulations! You got it! You get to shed {winner_location} now.")
        print(word_display(word, word_letters))

if winner == False:
    print(f"Alvinite Status: {alvinite_status}" )
    print(gallows[lives])
    print("Oh no, you died because too much meth! By the way, the word was", word)
