print("Welcome to my computer quiz!")
print('''Instructions:
      1.Each question carries 1 mark.
      2.There is no negative marks.
      3.At the end of the quiz,the score will be given.
      4.Also the percentage of accuracy will be given. ''')
playing = input("Do you want to play? ")
#to check user to play or not,if not yes then quit the quiz
# def quiz(playing):
if playing.lower() != "yes":
        #lower() is a method ie used to make the text to lower case
    quit()

print("Okay! Let's Play :)")
score,questions = 0,0

answer = input("What does CPU stands for? ")
questions+=1
    #title() is used to make it to title case
if answer.title() == "Central Processing Unit" :
    print("You got it!!!")
    score+=1
else:
    print("You've lost it!!!")

answer = input("What does GPU stands for? ")
questions+=1
if answer.title() == "Graphics Processing Unit" :
    print("You got it!!!")
    score+=1
else:
    print("You've lost it!!!")

answer = input("What does RAM stands for? ")
questions+=1
if answer.title() == "Random Access Memory" :
    print("You got it!!!")
    score+=1
else:
    print("You've lost it!!!")

answer = input("What does PSU stands for? ")
questions+=1
if answer.title() == "Power Supply" :
    print("You got it!!!")
    score+=1
else:
    print("You've lost it!!!")

print(f"You got {score} questions correct!")
print(f"You are {(score/questions)*100}% accurate in this quiz!")
# quiz(playing)    
# playing = input("Do you want to take again the quiz? ")
# while playing.lower()=="yes":
#     quiz(playing)
# else:
#     quit()