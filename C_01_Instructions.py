# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # checks if the user response is a word in the list
            if item == user_response:
                return item

            # checks if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error of user does not enter something that is valid
        print(error)
        print()


# Displays instructions
def instructions():
    print('''

**** Instructions ****

To begin, choose the number of rounds and either customise
the game parameters or go with the default game (where the
secret number will be between 1 and 100).

Then choose how many rounds you'd like to play <enter> for
infinite mode.

Your goal is to try to guess the secret number without
running out of guesses.

Good luck!

    ''')


# Main routine
print()
print("💎📄✂️ Rock / Paper / Scissors Game ✂️📄💎")
print()

# ask user if they want to see the instructions and display
# them if requested.
want_instructions = string_checker("do you want to read the instructions?")

# checks user enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print("program continues")

