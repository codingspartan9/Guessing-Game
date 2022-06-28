import random
def run_computer_guesses_game(number_of_guesses):
    min_number, max_number = 0, 100
    print(f"Pick a number between 1-100 and I will try to guess it in {number_of_guesses} tries")
    for x in range(number_of_guesses):
        computer_guess = min_number + (max_number - min_number) // 2 if (max_number - min_number) // 2 != 0 else 1 + random.randint(-2, 2)
        player_input = input(f"My guess is {computer_guess}: type 'correct' | 'higher' | 'lower''  ")
        max_number, min_number = computer_guess if player_input == "lower" else max_number, computer_guess if player_input == "higher" else min_number
        if player_input == "correct": return "I Won!"
    return "Congratulations You Won!"
def run_player_guesses_game(number_of_guesses):
    computer_number, additional_text = random.randint(0, 100), ""
    print(f"I picked a number between 1-100 and I want you to guess it in {number_of_guesses}; I will tell you if your guess is higher, lower, or correct")
    for x in range(number_of_guesses):
        player_guess = int(input(f"{additional_text}; What is your guess  "))
        additional_text = f"The number is lower than {player_guess}" if player_guess > computer_number else f"The number is higher than {player_guess}"
        if player_guess == computer_number: return "You Won!"
    return f"I Won! The number was {computer_number}"
while True: print((run_player_guesses_game if input("What game mode do you want: type '1' for you guess the computer's number and '2' for the computer guessing your number") == '1' else run_computer_guesses_game)(7))