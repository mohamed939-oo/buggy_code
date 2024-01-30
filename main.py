print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    exit()
print("Okay! Let's play : ")
score = 0
ls = ["19", "20", "21", "22"]
answer = input("How old are you? ")
if answer.lower() in ls:
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
l = ["blue", "white", "red", "black", "brown", "green", "yallow", "orange"]

answer = input("What is your favorite color?")
if answer.lower() in l:
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what is your dream job? ")
if answer.lower() == "":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("What is the capital of France? ")  # Introducing a new unrelated question
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%")
