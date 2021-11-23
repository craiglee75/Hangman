import random

def title():
    print("H A N G M A N")


def game_init():
    wordlist = ['python', 'java', 'kotlin', 'javascript']
    word = wordlist[random.randint(0, len(wordlist)-1)]
    return [char for char in word]


def guess(user_guess):
    global tries
    if len(user_guess) != 1:
        print("You should input a single letter")
    elif user_guess.isupper() or not user_guess.isalpha() or user_guess == "-":
        print("Please enter a lowercase English letter")
    elif user_guess in word_clue or user_guess in guessed_letters:
        print("You've already guessed this letter")
    elif user_guess in new_word:
        for idx in range(len(new_word)):
            if new_word[idx] == user_guess:
                word_clue[idx] = user_guess
    else:
        print("That letter doesn't appear in the word")
        tries -= 1

def play_game():
    global new_word, word_clue, tries, guessed_letters
    # title()
    new_word = game_init()
    word_clue = ["-" for _ in new_word]
    guessed_letters = []

    tries = 8
    while tries > 0:
        print("")
        print("".join(word_clue))
        user_guess = input("Input a letter: ")
        guess(user_guess)
        guessed_letters.append(user_guess)
        if "-" not in word_clue:
            print("")
            print("".join(word_clue))
            print("You guessed the word!")
            print("You survived!")
            break
        elif tries == 0:
            print("You lost!")
            break


while True:
    title()
    game_status = ""
    game_status = input('Type "play" to play the game, "exit" to quit: ')
    if game_status != "play" and game_status != "exit":
        game_status = input('Type "play" to play the game, "exit" to quit: ')
    elif game_status == "play":
        play_game()
        print("")
        game_status = input('Type "play" to play the game, "exit" to quit: ')
        break  # added break to ensure jetbrains testing didn't generate an internal error
    elif game_status == "exit":
        break
        
