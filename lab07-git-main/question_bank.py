#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

questions = {
    "Science": [
        ("What planet is known as the Red Planet?", "Mars"),
        ("What gas do plants absorb from the atmosphere?", "Carbon Dioxide"),
        ("What is the boiling point of water in Celsius?", "100"),
        ("What organ pumps blood through the body?", "Heart"),
        ("What gas do humans exhale?", "Carbon Dioxide"),
        ("What part of the atom has a positive charge?", "Proton"),
        ("What is the chemical symbol for water?", "H2O"),
        ("What galaxy is Earth located in?", "Milky Way"),
        ("What force keeps us on the ground?", "Gravity"),
        ("What planet is closest to the Sun?", "Mercury")
    ],
    "History": [
        ("Who was the first President of the United States?", "George Washington"),
        ("In which year did World War II end?", "1945"),
        ("What wall fell in 1989?", "Berlin Wall"),
        ("Who discovered America?", "Christopher Columbus"),
        ("Which war was fought between the North and South in the US?", "The Civil War"),
        ("What year did the Titanic sink?", "1912"),
        ("Who was known as the Maid of Orléans?", "Joan of Arc"),
        ("Which empire built the Colosseum?", "Roman Empire"),
        ("What was the name of Darwin’s ship?", "HMS Beagle"),
        ("Which queen ruled the UK before Elizabeth II?", "Queen Victoria")
    ],
    "Movies": [
        ("Who directed 'Inception'?", "Christopher Nolan"),
        ("What is the name of the wizard school in Harry Potter?", "Hogwarts"),
        ("Which character says 'I'll be back'?", "The Terminator"),
        ("What is the name of the snowman in Frozen?", "Olaf"),
        ("Which movie features Jack Sparrow?", "Pirates of the Caribbean"),
        ("What movie won Best Picture in 2020?", "Parasite"),
        ("Who played the Joker in The Dark Knight?", "Heath Ledger"),
        ("What film has a blue alien race on another planet?", "Avatar"),
        ("What sci-fi film has R2-D2 and C-3PO?", "Star Wars"),
        ("Which movie features the song 'Let It Go'?", "Frozen")
    ]
}

hints = {
    "Science": [
        "Named after a Roman god of war.",
        "It's a greenhouse gas.",
        "A round number.",
        "It beats regularly.",
        "Same gas that plants need.",
        "Starts with 'P'.",
        "Two hydrogen, one oxygen.",
        "Spiral galaxy we're part of.",
        "Starts with 'G'.",
        "Not Venus, not Earth..."
    ],
    "History": [
        "On the US one dollar bill.",
        "Mid-1940s.",
        "Symbol of Cold War divide.",
        "In 1492, he sailed the ocean blue.",
        "Fought in the 1860s.",
        "The ship hit an iceberg.",
        "French war heroine.",
        "They also had gladiators.",
        "Starts with HMS.",
        "She ruled during the 1800s."
    ],
    "Movies": [
        "He also directed The Dark Knight.",
        "Starts with 'H'.",
        "He wears sunglasses and is a robot.",
        "He likes warm hugs.",
        "A pirate captain.",
        "South Korean film.",
        "He won an Oscar posthumously.",
        "Tall blue aliens on Pandora.",
        "Classic space opera.",
        "Disney princess movie."
    ]
}


#---------------------------------------


    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
def select_random_question(category):
    if category not in questions or not questions[category]:
        return None, None
    index = random.randint(0, len(questions[category]) - 1)
    return questions[category][index]


#---------------------------------------


    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
def check_answer(player_answer, correct_answer):
    return player_answer.strip().lower() == correct_answer.strip().lower()

#---------------------------------------


    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
def remove_question(category, question):
    if category in questions:
        for i, (q, a) in enumerate(questions[category]):
            if q == question:
                del questions[category][i]
                del hints[category][i]
                break

#---------------------------------------


    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
def display_question_and_accept_answer(question):
    print(f"\nQuestion: {question}")
    answer = input("Your answer: ")
    return answer
    #------------------------

#---------------------------------------


    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
def provide_hint(category, question):
    if category in questions and category in hints:
        for i, (q, a) in enumerate(questions[category]):
            if q == question:
                return hints[category][i]
    return "No hint available."
    #------------------------

#---------------------------------------


    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
def display_correct_answer(correct_answer):
    print(f"The correct answer was: {correct_answer}")
    #------------------------

#---------------------------------------




