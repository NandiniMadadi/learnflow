import random

# Define questions for each topic and difficulty level
topics = {
    "geography": {
        "easy": [
            {"question": "What is the highest mountain in the world?", "answer": "Mount Everest"},
            {"question": "Which country has the most population?", "answer": "China"},
            {"question": "What is the longest river in the world?", "answer": "Nile"}
        ],
        "medium": [
            {"question": "Which country has the largest land area?", "answer": "Russia"},
            {"question": "What is the smallest country in the world?", "answer": "Vatican City"},
            {"question": "What is the longest river in the world?", "answer": "Nile"}
        ],
        "hard": [
            {"question": "Which desert is the largest in the world?", "answer": "Sahara"},
            {"question": "What is the deepest point in the ocean?", "answer": "Mariana Trench"},
            {"question": "Which country has the most islands?", "answer": "Sweden"}
        ]
    },
    "science": {
        "easy": [
           {"question": "What is the center of an atom called?", "answer": "Nucleus"},
            {"question": "What is H2O commonly known as?", "answer": "Water"},
            {"question": "What gas do plants absorb from the atmosphere?", "answer": "Carbon dioxide"}
        ],
        "medium": [
            {"question": "What is the chemical symbol for gold?", "answer": "Au"},
            {"question": "What is the chemical formula for table salt?", "answer": "NaCl"},
            {"question": "Who is known as the father of modern physics?", "answer": "Albert Einstein"}
        ],
        "hard": [
            {"question": "What is the heaviest naturally occurring element?", "answer": "Uranium"},
            {"question": "What is the main gas found in the air we breathe?", "answer": "Nitrogen"},
            {"question": "Who developed the theory of evolution?", "answer": "Charles Darwin"}
        ]
    }
}

def select_topic():
    while True:
        topic = input("Select topic (geography, science): ").lower()
        if topic in topics:
            return topic
        else:
            print("Invalid topic. Please choose again.")

def select_difficulty(topic):
    while True:
        difficulty = input("Select difficulty (easy, medium, hard): ").lower()
        if difficulty in topics[topic]:
            return difficulty
        else:
            print("Invalid difficulty level. Please choose again.")

def ask_question(question_data):
    question = question_data["question"]
    answer = question_data["answer"]
    user_answer = input(f"{question} ")
    
    if user_answer.strip().lower() == answer.strip().lower():
        print("Correct!")
        return True
    else:
        print(f"Incorrect! The correct answer was {answer}.")
        return False

def quiz_game():
    print("Welcome to the Quiz Game!")
    score = 0
    topic = select_topic()
    difficulty = select_difficulty(topic)
    selected_questions = topics[topic][difficulty]
    random.shuffle(selected_questions)

    for question_data in selected_questions:
        if ask_question(question_data):
            score += 1

    print(f"Game over! Your final score is: {score} out of {len(selected_questions)}")

if __name__ == "__main__":
    quiz_game()