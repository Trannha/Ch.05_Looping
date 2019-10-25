'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''


person=0
tie=0
comp=0
done=False
while not done:
    spr=int(input("Choose \n 1.Rock \n 2.Paper \n 3.Scissors \n Press Q to quit. \n"))
    import random
    num=random.randrange(1,4)
    if num==1:
        rps="Rock"
    elif num == 2:
        rps="Paper"
    elif num == 3:
        rps="Scissors"
    if spr==1 and rps == "Paper":
        print("Paper, you lose")
        comp+=1
    elif spr==2 and rps=="Scissors":
        print("Scissors, you lose")
        comp+=1
    elif spr==3 and rps =="Rock":
        print("Rock, you lose.")
        comp+=1
    if spr==1 and rps=="Scissors":
        print("Scissors, you win")
        person+=1
    elif spr==2 and rps=="Rock":
        print("Rock, you win")
        person+=1
    elif spr==3 and rps == "Paper":
        print("Paper, you win")
        person+=1
    if spr==1 and rps=="Rock":
        print("Rock, tie")
        tie+=1
    elif spr==2 and rps=="Paper":
        print("Paper, tie")
        tie+=1
    elif spr==3 and rps=="Scissors":
        print("Scissors, tie")
        tie+=1
    elif spr== "q":
        done=True
        print("User Score:", person)
        print("Computer score:", comp)
        print("Ties:", tie)














