import datetime
import time
from generate_country import *
# IDEA to expand:
# could have capitals by continents (easy version) and all countries (difficult)

name = input("Welcome to the world capitals quiz game! What's your name? ")
print("Here are some RULES:")
time.sleep(2)
print("Watch your spelling, but you don't need to capitalize.")
time.sleep(3)
print("If you get stuck or just plain don't know, type in /help/ to get a hint.")
time.sleep(3)
print("You have two hints per question. The third time you type in help, it gives you the answer.")
time.sleep(5)

num_of_questions = int(input("How many questions would you like? "))
correct_answers = 0
wrong_answers = 0

for question in range(num_of_questions):
    question = generate_country() # generate random country through function
    num_of_questions -= 1 # reduce number of questions by one
    if question: # if correct answer, the function returns True
        correct_answers += 1 # if the user answers correctly, a correct answer is added
    else:
        wrong_answers += 1

#appending scores to capitas_scores in form of dict
scores.append({
    "name" : name,
    "correct answers" : correct_answers,
    "all questions" : (correct_answers + wrong_answers),
    "date" : str(datetime.date.today())
})
new_scores = json.dumps(scores)
p2.write_text(new_scores)

print(f"You answered {correct_answers} questions correctly out of {correct_answers + wrong_answers}!")

#gives player chance to view scores
see_scores = input("Would you like to see how others scored? (y/n) ")
if see_scores == "y":
    for score in scores:
        print(score)
