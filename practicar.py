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





 print("This program takes three numbers and returns the sum.")
  total = 0
  for i in range(3):
      var = int(input("Give a number: "))
      total += var
  print("The total is:", total)


for i in range(2,101):
    print(i)

    i = 10
    while i > -1:
        print(i)
        i -= 1

        import random

        i = random.randrange(11)
        print(i)

        total = 0
        yourmompos = 0
        yourdadneg = 0
        yourstepbrozero = 0
        for i in range(7):
            nums = int(input("Please give a number: "))
            total += nums
            if nums == 0:
                yourstepbrozero = yourstepbrozero + 1
            elif nums > 0:
                yourmompos = yourmompos + 1
            else:
                yourdadneg = yourdadneg + 1
        print(total)
        print("This is your negative entries: ", yourdadneg)
        print("This is your positive entries:", yourmompos)
        print("This is your zero entries: ", yourstepbrozero)

