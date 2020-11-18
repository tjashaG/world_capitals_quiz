from pathlib import Path
import json
import random
import datetime
import time
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
    random_country = lst[index]  # generate random country through random index
    right_answer = capital[random_country]
    answer = input(f"What's the capital of {random_country}? ")
    if answer.lower() == right_answer.lower(): #generate correct answer for random country through dict key:value pair
        print("Correct!")
        return True
    elif answer.lower() == "help":
        print("Here's a hint!")
        print(f"The correct answer STARTS with: {right_answer[0:2]}")
        assisted_answer = input()
        if assisted_answer.lower() == right_answer.lower():
            print("There you go! You just needed a nudge ;) ")
            return True
        elif assisted_answer.lower() == "help":
            print("It's OK if you still don't know! ")
            print(f"The correct answer ENDS with: {right_answer[(len(right_answer) - 3):]}")
            assisted_answer2 = input()
            if assisted_answer2.lower() == right_answer.lower():
                print("I knew you knew it!")
                return True
            elif assisted_answer2.lower() == "help":
                print(f"*sigh* Might as well GIVE you the answer... It's {right_answer}!")
                return False
            else:
                print(f"Incorrect! It's {capital[random_country]}.")
                return False
        else:
            print(f"Incorrect! It's {capital[random_country]}.")
            return False
    else:
        print(f"Incorrect! It's {capital[random_country]}.")
        return False

name = input("Welcome to the world capitals quiz game! What's your name? ")
print("Here are some RULES:")
time.sleep(3)
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
