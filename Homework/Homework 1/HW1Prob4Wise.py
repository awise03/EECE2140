game_over = False
while not game_over:
    print()
    import random
    guessed = False
    random = random.randint(1,1000)
    print("Guess my number between 1 and 1000 with the fewest possible guesses: ")
    while not guessed:
        valid = False
        while not valid:
            guess = int(input("Input a number between 1 and 1000: "))
            if 1 < guess < 1000: 
                valid = True
                break
            else:
                print("Invalid number. Please try again.")
        if guess < random: print("Too low. Try again")
        elif guess > random: print("Too high. Try again")
        else:
            print("Congratulations. You guessed the number!")
            guessed = True
    
    play_again = input("Would you like to play again? (y/n) ")
    if play_again == "y":
        continue
    else:
        game_over = True
