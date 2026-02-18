from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Let the player choose a difficulty level
print("Welcome to the Quiz Game!")
print("Choose your difficulty level:")
print("  1 - Easy")
print("  2 - Medium")
print("  3 - Hard")

choice = input("Enter 1, 2 or 3: ")
difficulty_map = {"1": "easy", "2": "medium", "3": "hard"}
difficulty = difficulty_map.get(choice, "easy")
print(f"\nYou chose: {difficulty.upper()}\n")

# Filter questions by chosen difficulty
question_bank = []
for question in question_data:
    if question["difficulty"] == difficulty:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

if not question_bank:
    print("No questions available for this difficulty.")
else:
    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz!")
    if quiz.score >= len(question_bank):
        print(f"Perfect score! Your final score was: {quiz.score}/{quiz.question_number}")
    elif quiz.score >= len(question_bank) // 2:
        print(f"Great job! Your final score was: {quiz.score}/{quiz.question_number}")
    else:
        print(f"Better luck next time! Your final score was: {quiz.score}/{quiz.question_number}")
