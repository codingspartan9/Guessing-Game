import random


def run_computer_guesses_game(number_of_guesses):
    min_number = 0
    max_number = 100
    print(f"Pick a number between 1-100 and I will try to guess it in {number_of_guesses} tries")
    player_has_won = True

    for x in range(number_of_guesses):
        difference = (max_number - min_number) // 2

        if difference == 0:
            difference = 1

        computer_guess = min_number + difference + random.randint(-2, 2)

        player_input = input(f"My guess is {computer_guess}: type 'correct' | 'higher' | 'lower''  ")

        if player_input == "lower":
            max_number = computer_guess

        if player_input == "higher":
            min_number = computer_guess

        if player_input == "correct":
            print("I Won!")
            player_has_won = False
            break

    if player_has_won:
        print("Congratulations You Won!")


def run_player_guesses_game(number_of_guesses):
    computer_number = random.randint(0, 100)
    additional_text = ""
    player_has_won = False
    print(f"I picked a number between 1-100 and I want you to guess it in {number_of_guesses}; I will tell you if your guess is higher, lower, or correct")

    for x in range(number_of_guesses):
        player_guess = int(input(f"{additional_text}; What is your guess  "))

        if player_guess > computer_number:
            additional_text = f"The number is lower than {player_guess}"

        if player_guess < computer_number:
            additional_text = f"The number is higher than {player_guess}"

        if player_guess == computer_number:
            print("You Won!")
            player_has_won = False
            break

    if not player_has_won:
        print(f"I Won! The number was {computer_number}")

while True:
    number_of_guesses = 5
    game_mode = input("What game mode do you want: type '1' for you guess the computer's number and '2' for the computer guessing your number")

    if game_mode == '1':
        run_player_guesses_game(number_of_guesses)

    if game_mode == '2':
        run_computer_guesses_game(number_of_guesses)