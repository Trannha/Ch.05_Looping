  #Sign your name: Nha

'''
1. Make the following program work.
   '''

print("This program takes three numbers and returns the sum.")
total = 0
for i in range(3):
    var = int(input("Give a number: "))
    total += var
print("The total is:", total)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2,101):
    print(i)

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
i = 10
while i > -1:
    print(i)
    i -= 1






'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
i = random.randrange(11)
print(i)





'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''

total=0
yourmompos=0
yourdadneg=0
yourstepbrozero=0
for i in range(7):
    nums=int(input("Please give a number: "))
    total+= nums
    if nums == 0:
        yourstepbrozero = yourstepbrozero + 1
    elif nums > 0:
        yourmompos = yourmompos + 1
    else:
        yourdadneg = yourdadneg + 1
print(total)
print("This is your negative entries: ", yourdadneg)
print("This is your positive entries:",yourmompos)
print("This is your zero entries: ", yourstepbrozero)