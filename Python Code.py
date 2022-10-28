print("Welcome to the Love Calculator!")

name1 = input("What is your name?")
name2 = input("What is your partner's name?")

score_true = 0
score_love = 0

for letter in (name1 + name2):
    if letter == "T" or letter == 't':
        score_true += 1
    elif letter == "R" or letter == "r":
        score_true += 1
    elif letter == "U" or letter == "u":
        score_true += 1
    elif letter == "E" or letter == "e":
        score_true += 1

for character in (name1 + name2):
    if character == "L" or character == "l":
        score_love += 1
    elif character == "O" or character == "o":
        score_love += 1
    elif character == "V" or character == "v":
        score_love += 1
    elif character == "E" or character == "e":
        score_love += 1

total_score = str(score_true)+str(score_love)

if int(total_score) < 10 or int(total_score) > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif 40 < int(total_score) < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
    
