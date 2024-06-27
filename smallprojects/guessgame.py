secret_word = "batman"
guess =""
count_guess = 0
limit_guess = 3
out_of_guess = False

print("guess my favourite superhero")

while guess != secret_word and not(out_of_guess):
    
    if count_guess < limit_guess :
        guess = input('enter guess: ')
        count_guess += 1
    else :
        out_of_guess = True

if out_of_guess:
    print("out of guesses!")
else:
    print("you win!")


