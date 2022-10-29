def multiplication(x , y):
  result = 0
  for i in range(x):
    result = result + y
  return result 

def exponent(a , b):
  result = 1
  for i in range(a):
    result = result * b 
  return result

def square(num):
  return multiplication(num,num)
  

def main():
  result1 = multiplication(x=5 , y=6)
  print (result1)

  result2 = exponent(a=5 , b=6)
  print(result2)

  result3 = square(5)
  print(result3)

main()