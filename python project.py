


import math
import random
import time

def easy_quiz():
    questions = [
        ("Simplify 4(10+15÷5×4−2×2)\n", "72"),
        ("Simplify the expression: 2x + 3x - 5\n", "5x - 5"),
        ("Solve for x: 4x + 2 = 18\n", "4"),
        ("Expand the expression: (x + 3)(x - 2)\n", "x^2 + x - 6"),
        ("Factorize the expression: x^2 - 5x + 6\n", "(x - 2)(x - 3)"),
        ("Solve for x: 3x - 4 = 2x + 1\n", "5")
    ]
    random.shuffle(questions)
    start_time = time.time()
    for question, answer in questions:
        timer_start = time.time()
        while time.time() - timer_start < 60:
            remaining_time = 60 - int(time.time() - start_time)
            print(f"Time Remaining: {remaining_time} seconds")
            print(question)
            user_answer = input()
            if user_answer.strip() == answer:
                print("Correct!")
                break
            else:
                print("Incorrect! Try again.")
        else:
            print("Time's up! Quiz aborted.")
            return

def hard_quiz():
    questions = [
        ("Solve for x: sin(x) = √3/2, where 0 ≤ x ≤ 2π\n", "π/3"),
        ("Prove the identity: cos^2(x) + sin^2(x) = 1\n", "Identity holds for all x"),
        ("Solve for x: 2cos^2(x) - cos(x) - 1 = 0, where 0 ≤ x ≤ 2π\n", "π/3, 5π/3"),
        ("Find the exact value of: tan(π/4 + π/3)\n", "√3"),
        ("If sin(x) = 4/5 and x is in the second quadrant, find cos(x) and tan(x)\n", "-3/5, -4/3")
    ]
    random.shuffle(questions)
    start_time = time.time()
    for question, answer in questions:
        timer_start = time.time()
        while time.time() - timer_start < 120:
            remaining_time = 120 - int(time.time() - start_time)
            print(f"Time Remaining: {remaining_time} seconds")
            print(question)
            user_answer = input()
            if user_answer.strip() == answer:
                print("Correct!")
                break
            else:
                print("Incorrect! Try again.")
        else:
            print("Time's up! Quiz aborted.")
            return

def main():
    print("Welcome to the Math Quiz!")
    while True:
        print("\nMenu:")
        print("1. Easy (Algebra)")
        print("2. Hard (Trigonometry)")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            easy_quiz()
        elif choice == '2':
            hard_quiz()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()    
    
    # import necessary modules from python std. lib.
import random
import time

# A dictionary to map the operation symbols to their corresponding functions
# lamda is used  to create a function that will only contain simple expression
operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}

def generate_question():
    """Generates a math question along with its answer."""
    a, b = random.randint(1, 10-100), random.randint(1, 100)
    op = random.choice(list(operations.keys()))  # Randomly choose an operation
    question = f"What is {a} {op} {b}?"
    answer = operations[op](a, b)  # Calculate the answer using the selected operation
    return question, answer

def timed_math_challenge(duration=30):
    """Runs the timed math challenge for the specified duration."""
    print("Welcome to the Timed Math Challenge!")
    print(f"You have {duration} seconds to answer as many questions as you can.\nLet's begin!")
    
    start_time = time.time()
    score = 0

    while time.time() - start_time < duration:
        q, ans = generate_question()
        # try is used for error handling
        try:
            user_ans = int(input(q))
            if user_ans == ans:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
        except ValueError:  # In case the user enters something that's not an integer
            print("Please enter a valid number.")

    print(f"Time's up! You answered {score} questions correctly in {duration} seconds.")

# Start the challenge
timed_math_challenge()
    
    
    
    