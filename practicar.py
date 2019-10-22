import random
headstotal=0
tailstotal=0
for i in range(50):
    rand=random.randrange(0,2)
    if rand == 0:
        print("Heads")
        headstotal=headstotal+1

    else:
        print("Tails")
        tailstotal=tailstotal+1

totaltotal=headstotal+tailstotal
print("Heads total:",headstotal)
print("Tails total:",tailstotal)
print("Total of both:",totaltotal)
