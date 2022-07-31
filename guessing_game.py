## Project: Guessing Game using While loop
secret_num = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess_num = float(input('Guess: '))
    guess_count += 1
    if guess_num == secret_num:
        print('You won!')
        break   # break would directly terminate the loop without even evaluating the loops terminating condition
    else:
        print('You missed! Try again.')
else:  # Note: while loop also has an else part, else part is activated if while loop is normally terminated without any break
    print('Sorry, you run out of chances.')



# Key Note: while loop also has an else part, else part is activated if while loop is normally terminated without any break