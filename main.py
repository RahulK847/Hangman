import random
from hangman_art import stages, logo
from hangman_words import word_list
print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if display.count(guess)!=0:
      print("Hey, looks like you already guess that")
    else:
      
      for position in range(word_length):
          if guess==chosen_word[position]:
              display[position] = guess
      if guess not in chosen_word:
          print("Wrong Guess, You lose a life")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print("You lose.")
      if "_" not in display:
          end_of_game = True
          print("You win.")
    print(f"{' '.join(display)}")
    print(stages[lives])