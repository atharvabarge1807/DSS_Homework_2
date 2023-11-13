import random

def generate_random_integer(minimum, maximum):
    """
    Generate a random integer within the specified range.

    Parameters:
    - minimum (int): The lower bound of the range (inclusive).
    - maximum (int): The upper bound of the range (inclusive).

    Returns:
    int: A random integer within the specified range.
    """
    return random.randint(minimum, maximum)


def generate_random_operator():
    """
    Generate a random arithmetic operator (+, -, *).

    Returns:
    str: A randomly chosen arithmetic operator.
    """
    return random.choice(['+', '-', '*'])


def calculate_result(num1, num2, operator):
    """
    Calculate the result of an arithmetic operation.

    Parameters:
    - num1 (int): The first operand.
    - num2 (int): The second operand.
    - operator (str): The arithmetic operator (+, -, *).

    Returns:
    tuple: A tuple containing the problem statement and the result of the calculation.
    """
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    problem_statement = f"{num1} {operator} {num2}"
    return problem_statement, result


def math_quiz():
    """
    Conduct a math quiz game.

    The game presents users with math problems, checks their answers, and provides a final score.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = calculate_result(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            user_answer = 0

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
