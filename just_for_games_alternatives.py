r"""random = "bishow".lower()
symbol = '\u2764'
life = 9
word_list = list(random)
guess_list = ["??"]*len(random)
def word_list_loop(guessed_word, word_list=word_list, guess_list=guess_list):
    for i in range(len(word_list)):
        if word_list[i] == guessed_word:
            guess_list[i] = guessed_word
    print("correct,%s" % guess_list)

def mainloop( life=life, guess_list=guess_list, word_list=word_list):
    while life >= 1 and guess_list != word_list:
        guessed_word = input("Enter the guessed word: ")
        if guessed_word == random:
            print("Congrats")
            break
        elif guessed_word in guess_list:
            print("Already used...")
        elif guessed_word in word_list:
            word_list_loop(guessed_word)
        else:
            life = life - 1
            print("You've lost a life now: You've %s lifes" % (life * symbol))
    if life>=1 and guess_list == word_list:
        print("congrats!!!")
mainloop()
"""
