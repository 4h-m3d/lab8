#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

questions = {
    "maths" = [
        ("What is the square root of 144?", "12"),
        ("What is 15% of 200?", "30"),
        ("What is the value of π (up to 2 decimal places)?", "3.14"),
        ("What is 9 x 8?", "72"),
        ("What is the area of a rectangle with length 5 and width 3?", "15")
],


    "physics" = [
        ("What force pulls objects toward Earth?", "Gravity"),
        ("Who formulated the three laws of motion?", "Isaac Newton"),
        ("What is the unit of electric current?", "Ampere"),
        ("What is the speed of light in vacuum (in m/s)?", "299792458"),
        ("Which form of energy is stored in stretched rubber bands?", "Elastic potential energy")
],


    "computer" = [
        ("What does 'CPU' stand for?", "Central Processing Unit"),
        ("Which programming language is known for its snake logo?", "Python"),
        ("What is the binary equivalent of 5?", "101"),
        ("What does HTML stand for?", "HyperText Markup Language"),
        ("What key is used to copy on Windows (Ctrl + ___)?", "C")
],

}

    "maths_hints" = [
        "It's a two-digit number.",
        "Think of 10% and then half of it.",
        "It's commonly used in circles.",
        "Single-digit numbers multiplied.",
        "Area = length × width."
],

    "physics_hints" = [
        "Starts with 'G'.",
        "He saw an apple fall.",
        "Starts with 'A'.",
        "It's nearly 300 million.",
        "Opposite of kinetic."
],

    "computer_hints" = [
        "It's the brain of the computer.",
        "It's named after a reptile.",
        "Only 1s and 0s.",
        "Used to build web pages.",
        "The copy shortcut key."
],
}


#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """

    if category not in questions or not questions[category]:
        return None, None
    index = random.randint(0, len(questions[category]) - 1)
    return questions[category][index]


#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """

    return player_answer.strip().lower() == correct_answer.strip().lower()

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """

    if category in questions:
        for i, (q, a) in enumerate(questions[category]):
            if q == question:
                del questions[category][i]
                del hints[category][i]
                break

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """

    print(f"\nQuestion: {question}")
    answer = input("Your answer: ")
    return answer
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """

    if category in questions and category in hints:
        for i, (q, a) in enumerate(questions[category]):
            if q == question:
                return hints[category][i]
    return "No hint available."
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """

    print("The correct answer was: {correct_answer}")
    #------------------------

#---------------------------------------




