import random
import time
from uzwords import words

def random_words():
    a = random.choice(words)
    while "-" in a or " " in a:
        a = random.choice(words)
    return a

def test(letter, word):
    a = ""
    for i in word:
        if i in letter:
            a += i
        else:
            a += "-"
    return a


def main():
    enter_words = ""
    random_word = random_words().lower()
    print(f">>> I conceived {len(random_word)} one word, find this!")
    main_letters = set(random_word)
    while main_letters:
        print(test(enter_words, random_word))
        if enter_words:
            print(f"number of entered letters: {len(enter_words)}")
        letter = input("\n>>> enter the letter: ").lower()

        if letter in enter_words:
            print("\n>>> you entered this letter!")
            continue
        elif letter in main_letters:
            print(">>> GOODJOB!")
            main_letters.remove(letter)
        enter_words += letter
    print(f">>> SUCCESS, you finded the word at {len(enter_words)} attempts!")
main()




