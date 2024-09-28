import random

def guess_the_number():
    print("Welcome to 'Guess the Number' game!")
    
    # Define the range for the random number
    lower_bound = 1
    upper_bound = 100
    attempts = 5  # Max number of attempts
    
    # Generate a random number within the range
    number_to_guess = random.randint(lower_bound, upper_bound)
    
    print(f"Guess the number between {lower_bound} and {upper_bound}. You have {attempts} attempts.")
    
    # Game loop
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if guess < lower_bound or guess > upper_bound:
            print(f"Please enter a number between {lower_bound} and {upper_bound}.")
            continue

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
