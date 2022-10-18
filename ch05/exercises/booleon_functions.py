scoreValue = float(input("My score is "))

score1 = (scoreValue >= 90)
score2 = (scoreValue >= 80 and scoreValue < 90)
score3 = (scoreValue >= 70 and scoreValue < 80)
score4 = (scoreValue >= 60 and scoreValue < 70)
score5 = (scoreValue < 60)

def percentage_to_letter(score=0):
  if score1:
    print ("Grade A")
    return True
  if score2:
    print ("Grade B")
    return True
  if score3:
    print ("Grade C")
    return True
  if score4:
    print ("Grade D")
    return False
  if score5:
    print ("Grade F")
    return False
    
print(percentage_to_letter())