distaway=100
thirst=100
cameltired=0
endgoal=300
print("Welcome to Jojo's Bizarre Sun Run!")
print("The goal of the game is to run from the Sun towards the safepoint while managing your thirst and camel.")
start=input("Press s to start. \n")
if input=="s":
    done=False
while not done:

    print("The Sun is 100 km away.")
    print("You are full on water/thirst")
    print("Your camel is not tired")
    run=input("Press R to run ")
