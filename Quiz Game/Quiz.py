score = 0
name = input ("enter your name:\n")
print ("hello",name,"Let's start the quiz")
print("\n")
answer1 = input("which one is the first web browser invented in 1990? \na. Internet Explorer \nb. Mozilla \nc. Mosaic \nd. Nexus \nAnswer: ")
if answer1 == "d" or answer1 == "Nexus":
    score += 1
    print("Correct! you got 1 point")
    print("Score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is Nexus.")
    print("score:" ,score)
    print("\n")

answer2 = input("which on is the first search engine in internet? \na. Google \nb. WAIS  \nc. Archie \nd. Altavista  \nAnswer: ")
if answer2 == "c" or answer2 == "Archie":
    score += 1
    print("Correct! you got 1 point")
    print("Score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is Archie.")
    print("score:" ,score)
    print("\n")

answer3 = input("First computer virus known as- \na. Rabbit \nb. Creeper Virus  \nc. Elk cloner \nd. SCA Virus  \nAnswer: ")
if answer3 == "b" or answer3 == "Creeper Virus":
    score += 1
    print("Correct you got 1 point!")
    print("Score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is Archie.")
    print("score:" ,score)
    print("\n")

answer4 = input("Which American Computer Company is also known by the nick name Big Blue?- \na. IBM \nb. Compaq Corporation  \nc. Microsoft \nd. Apple  \nAnswer: ")
if answer4 == "a" or answer3 == "IBM":
    score += 1
    print("Correct1!")
    print("Score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is IBM.")
    print("score:" ,score)
    print("\n")

if score <= 1:
   print("Your total score is:",score, "Too Bad...")
elif score ==2:
    print ("Your total score is:",score, "Average score")
else:
    print ("Your total score is:",score, "Awesome score...")

    
 




 