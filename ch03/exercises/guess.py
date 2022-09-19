import random
number_list = range(1,11)
number = random.choice(number_list)

for i in range(3):
  print ("Enter a number between 1 and 10: ")
  guess = int(input())
  if guess < number:
    print ("Too Low")
  if guess > number:
    print ("Too High")
  if guess == number:
    print ("Correct!")
    break