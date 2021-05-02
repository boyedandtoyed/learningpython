r"""guess_the_word = "NONNONONO".lower()
word_list = list(guess_the_word)
guess_list = ["?"] * len(word_list)
life = 9
print("You've only nine chances.")
symbol = u'\u2764'
while life >= 1 and guess_list != word_list:
    guessed_word = input("Enter the guessed letter or word: ").lower()
    if guessed_word in guess_list:
        print("Already used")
    elif guessed_word == guess_the_word:
        print("CONGRATULATIONS!!!!!!")
        break
    elif guessed_word in word_list:
        for i in range(len(word_list)):
            if word_list[i] == guessed_word:
                guess_list[i] = guessed_word
        print("you're correct this time you now have %s lives" % (symbol*life))
        print(guess_list)
        if guess_list == word_list:
            print("Congrats")
    else:
        life -= 1
        print("you're wrong this time you now have %s lives" % (symbol*life))
if life == 0:
    print("Since you've exhausted lives, try next time, the word was %s" % guess_the_word)
"""
