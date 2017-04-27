import random
import sys
import time


def alive(lives, count, guessed, random_capital, wrong_letters, guessed_l):
    print("Wrong letters are:"," ".join(set(wrong_letters)))
    guess = input("Give me a letter or a word: ").upper()
    count = count + 1
    if len(guess) == 1:
        if(guess in random_capital):
            guessed = guessed + guess
            print("The letter is in the word.", "\n", " ".join(letter if letter in guessed else '_' for letter in random_capital))
            guessed_l.append(guess)
            if set(guessed_l) == set(random_capital):
                you_win(end, count, random_capital)
        else:
            lives = life_lost(lives, wrong_letters, guess, 1)
    if len(guess) != 1:
        if guess == random_capital:
            you_win(end, count, random_capital)
        else:
            lives = life_lost(lives, wrong_letters, guess, 2)
    return lives

def life_lost(lives, wrong_letters, guess, lost_l): # word_or_letter: "word" or "letter"
    print("Wrong!You lost " + str(lost_l) + " life(s)!")
    lives = lives - lost_l
    wrong_letters.append(guess)
    print("You have " + str(lives) + " lives.")
    return lives

def play_q():
    again = input("Press Y for YES or any other button for NO.").upper()
    if again == "Y":
        return
    else:
        sys.exit()

def you_win(end, count, random_capital):
    end = time.time()
    total_time = str(round(end - start))
    letters_count = str(count)
    print("\nYOU WIN!"," You guessed after","".join(str(count)),"letters. It took you","".join(str(round(end - start))),"seconds.\n\nDo you want to play again?")
    play_q()

def game_over(start, count, random_capital):
    end = time.time()
    print("GAME OVER.", "\n", " The word was:" , random_capital, "\nYou tried to put","".join(str(count)),"letters. It took you","".join(str(round(end - start))),"seconds to LOST.\nDo you want to play again?","\n")
    play_q()

def main():
    while True:
        opened_file = open('countries_and_capitals.txt').read().splitlines() #otwiera plik tekstowy z listą państ i stolic
        random_pair = random.choice(opened_file).split(' | ') #losuje linię tekstu z pliku
        random_country = random_pair[0].upper() #pierwszy element listy, państwo
        random_capital = random_pair[1].upper() #drugi element listy, miasto
        lives = 5
        guessed = '' #tworzymy stringa słowo
        guessed_l = []
        count = 0 #licznik ilości prób
        start = time.time() #odpalamy licznik czasu
        wrong_letters = []
        print("Hello, let\'s play Hangman!\nTry to guess one of the World capitals:\n","".join("_" for letter in random_capital),"You have 5 lives.")
        while lives > 0:
            if lives == 1:
                print("HELP: The capital of","".join(random_country) + "!")
                lives = alive(lives, count, guessed, random_capital, wrong_letters, guessed_l)
            else:
                lives = alive(lives, count, guessed, random_capital, wrong_letters, guessed_l)
        else:
            game_over(start, count, random_capital)


if __name__ == "__main__":
    main()
