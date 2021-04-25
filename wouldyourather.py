#python3 ~/Documents/GitHub/avery-python-projects/wouldyourather.py
from random import randint
rathers = {
    """Would You Rather
1: Spend your last hour alive with your family
2: Spend your last hour alive doing something crazy that you've always been scared to do
""": "1. 647,868, or 51%, of people chose option 1 and 617,226, or 49%, chose option 2.",
    """Would You Rather
1: Have full control over your dreams
2: Never have to sleep
""": "1. 813,517, or 68%, of people chose option 1 and 338,579, or 32%, chose option 2.",
    """Would You Rather
1: Master every programming language
2: Master every spoken language
""": "2. 291,002, or 23%, of people chose option 1 and 999,406, or 77%, chose option 2.",
    """Would You Rather
1: Have it always be day
2: Have it always be night
""": "1. 729,990, or 58%, of people chose option 1 and 527,592, or 42%, chose option 2.",
    """Would You Rather
1: Have to laugh loudly every thirty minutes
2: Have to smile every waking hour
""": "2. 244,930, or 36%, of people chose option 1 and 427,080, or 64%, chose option 2.",
    """Would You Rather
1: Jump high
2: Run fast
""": "1. 1,119,455, or 75%, of people chose option 1 and 379,736, or 25%, chose option 2.",
    """Would You Rather
1: Never speak out loud (not even in sign language or a made up language)
2: Constantly speak all of your thoughts out loud
""": "2. 409,473, or 32%, of people chose option 1 and 879,954, or 68%, chose option 2."
}
#Print a welcome message
print("")
print("Hello and welcome to Would You Rather! This is a game where you can either compete with your friends, or play by yourself and try to guess which option is the most commonly picked one.")
print("")
#Ask how many people are playing
  
while True:    
    people = input("How many people are playing today? (Please enter a whole number) ")
    try:
        people = int(people)
        if people >= 1:
            break
        else:
            print("I'm sorry, the number of people has to be greater than 0. ")
            print("")

    except:
        print("I'm sorry, the number of people has to be a whole number.")
        print("")
print("")
people = int(people)

#Ask the names
scores = {}
if people == 1:
    while True:
        name = input("Please enter your first name. ")
        if " " not in name:
            break
        else:
            print("Your name should be one word, no spaces. ")
    scores[name.capitalize()]=0
    print("")
else:
    for i in range(people):
        while True:
            name = input("Player "+str(i + 1)+", what is your name? ")
            if " " not in name:
                break
            else:
                print("Your name should be one word, no spaces. ")
        scores[name.capitalize()]=0
        print("")
#Ask for how many questions they want to play
questions = int(input("How many different questions would you like to go through? (limit is "+str(len(rathers))+") "))
print("")

#Ask for the mode they want to play in
while True:
    mode = input("Do you want to play in easy mode (mode 1) or hard mode (mode 2)? Please type in 1 (for easy mode), 2 (for hard mode), or 3 (to learn what the modes are). ")
    if mode == "3":
        print("")
        print("Easy mode and hard mode are very similar. The only difference is that in hard mode, 1 point is deducted from your score when you get an answer wrong. ")
        input("Hit enter when you are ready to move on. ")
        print("")
    elif mode == "1":
        mode = "easy"
        break
    elif mode == "2":
        mode = "hard"
        break
    else:
        print("Please only enter the number 1, 2, or 3. ")
print("")
print("Ok! The chosen mode is "+mode +" mode.")
input("Hit enter when you are ready to move on to the Would You Rather questions. ")
print("")

valuesList = list(rathers.values())
keysList = list(rathers.keys())
#Give a question, ask for option 1 or 2
for i in range(questions):
    #choose a random question from the dictionary, print it out and get input (1 or 2), make that value in the dictionary become something like "none"
    correct = []
    while True:
        index = randint(0, len(rathers)-1)
        question = keysList[index]
        if valuesList[index] != "Done":
            break
    print(question)
    for player in scores:
        choice = input(player + ", which one do you think is the correct choice? Option 1 or option 2. (Please only enter the number) ")
        if int(choice) == int(valuesList[index][0]):
            scores[player] += 1
            correct.append(player)
        elif mode == "hard":
            scores[player] -= 1
    print("")
    print(valuesList[index])
    print("")
    if people > 1:
        if len(correct) >= 1:    
            print("The players who got it right are: ")
            for i in correct:
                print("- " + i)
        else:
            print("No one got it right! ")
        valuesList[index] = "Done"
        print("Here are the current scores: "+str(scores))
        print("")
    else:
        if len(correct) == 1:
            print("Good job! You got it correct. ")
        else:
            print("I'm sorry, you got it wrong. ")
#Ideas: make it so it checks to make sure you want to move on, make it so the user can type in "commands", make it so user can ask to see standings, make it so the name has to be a string, verify the chosen mode
#Ideas 2:  make it so you can choose a hard mode which removes points for wrong answers, make it so the choice must be 1 or 2, make it so the question number has to be right, make it so it doesn't print the scores the last time
#If they chose the more popular one, print good job or something and add one to their score
nameList = list(scores.keys())
pointsList = list(scores.values())
#sort the list and assign a variable to the value of the greatest number. make sure that value only appears once, then find that value in the list and return the person who got that score.
sortedPoints = pointsList.sort()
greatestScore = sortedPoints[-1]
appearances = sortedPoints.count(greatestScore)
if appearances == 1:
    print("The winner is... ")
    print()
if people > 1:  
    input("Hit enter when you are ready to see your final scores. ")
    print("")
    print("Here are the final scores. ")
    for i in range(len(scores)):
        print(nameList[i]+"'s score is "+str(pointsList[i])+".")
else: 
    input("Hit enter when you are ready to see your score. ")
    print("")
    print("Your final score is "+str(scores[name]))
#After they do all the questions, print who won with a congratulations message
#IDEAS: Make it so it is just for fun, no score and such
