import random

def random_number():
    random_num = random.randint(1, 1000)
    return random_num
   
def intro_message():
    print("Guess a number between 1 and 1000.")
    print("Let's see how many tries will it take you.")

def main():
    intro_message()
    num_of_tries = 0
    answer = random_number()
    guess = int(input("What is your guess?: "))
    while guess:
        try:
            if guess < answer:
                num_of_tries += 1
                print("Guess higher")
                guess = int(input("What is your guess?: "))
            elif guess > answer:
                num_of_tries += 1
                print("Guess lower")
                guess = int(input("What is your guess?: "))
            elif guess == answer:
                print(f"Correct. You got it in {str(num_of_tries)} tries.")
                break
        except ValueError:
            print("invalid choice. try again")
            continue
main()