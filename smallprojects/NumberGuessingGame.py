import random

no_to_guess = random.randint(1,100)
guess_count = 0
guess_limit = 10
guess = None
chance = 9

while guess_count < guess_limit :
    guess = int(input(f'chance {chance + 1} left, guess the number: ')) if chance != 0 else int(input('chance last, guess the number: ')) 
    chance -=1

    if int(guess) < int(no_to_guess) :
        guess_count +=1
        if guess_count != 10:
          print('too low')
        else:
          print('You lose!')
         
        
    elif int(guess) > int(no_to_guess):
        guess_count +=1
        if guess_count != 10:
          print('too high')
        else:
            print('You lose!')
            
        
    elif int(guess) == int(no_to_guess):
        print('you guess right, you win')
        break
    