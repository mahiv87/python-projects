import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
display = []
lives = 6

hangman = [

    '''
        _______
      |/      |
      |      (_)
      |      \|/
      |       |
      |      / \\
      |
   ___|___
     ''',
    '''
        _______
      |/      |
      |      (_)
      |      \|/
      |       |
      |      
      |
   ___|___
     ''',
    '''
        _______
      |/      |
      |      (_)
      |       |
      |       |
      |      
      |
   ___|___
     ''',
    '''
        _______
      |/      |
      |      (_)
      |       |
      |       
      |      
      |
   ___|___
     ''',
    '''
        _______
      |/      |
      |      (_)
      |      
      |       
      |      
      |
   ___|___
     ''',
    '''
       _______
     |/      |
     |      
     |      
     |       
     |      
     |
  ___|___
    '''
]

for index in range(len(chosen_word)):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: \n").lower()
    # print(guess)

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(hangman[lives])
        if lives == 0:
            end_of_game = True
            print("You lose\n")
            print(f"The answer is {chosen_word}\n")


    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")

