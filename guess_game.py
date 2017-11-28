import random


def guess_game():
    print("Type 'quit' to exit")
    game = True
    user_choice = 0

    while game:
        guess_number = random.randint(1, 9)
        while user_choice != guess_number and user_choice != 'quit':
            user_choice = input("Guess the number: ")
            if user_choice.isnumeric():
                user_choice = int(user_choice)
            if user_choice == 'quit':
                print("Thanks for playing!")
                game = False
                break

            if user_choice > guess_number:
                if abs(user_choice - guess_number == 1):
                    print("Your on fire!!!!!")
                elif abs(user_choice - guess_number) == 2:
                    print("Getting warmer!!")
                else:
                    print("To big!")

            if user_choice < guess_number:
                if abs(user_choice + guess_number) == 1:
                    print("Your on fire!!!!")
                elif abs(user_choice + guess_number) == 2:
                    print("Getting Warmer!!")
                else:
                    print("To little")

            if user_choice == guess_number:
                print("Correct!")
                user_input = input("Would you like to play again (Yes or Y) or (quit): ").lower()
                while user_input not in ('yes', 'y', 'quit'):
                    print("Please enter valid answer (Yes or Y) or (quit)")
                    user_input = input("Would you like to play again(Yes or Y): ").lower()

                if user_input == 'quit':
                    print("Thanks for playing! Goodbye")
                    game = False
                    break


guess_game()

