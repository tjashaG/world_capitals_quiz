from pathlib import Path
import json
import random


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
