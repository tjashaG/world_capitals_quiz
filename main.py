from pathlib import Path
import json
import random
import datetime
#could add hints using the slice method
#could have capitals by continents (easy version) and all countries (difficult)

p2 = Path(".", "data", "capitals_scores.txt")
scores = json.loads(p2.read_text())
p = Path(".", "data", "quiz_capitals.txt")
capital = json.loads(p.read_text())
#keys = capital.keys() #get the keys from dict - thought this was why I was getting only keys in the list. Nothing changed since I commented it out, so I guess it's unimportant.
lst = list(capital) #turn dictionary into a list of just countries (don't understand why JUST countries and not country/capital pair)


#function to generate random country
def generate_country():
    index = random.randint(1, len(lst) - 1)  # give index a random number
    random_country = lst[index]  # generate random country through random index number
    answer = input(f"What's the capital of {random_country}? ")
    if answer.lower() == (capital[random_country]).lower(): #generate correct answer for random country through dict key:value pair
        print("Correct!")
        return True
    else:
        print(f"Incorrect! It's {capital[random_country]}.")
        return False

name = input("Welcome to the world capitals quiz game! What's your name? ")
print("Watch your spelling, but you don't need to capitalize.")
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
#appending scores to the capitas_scores in form of dict
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
