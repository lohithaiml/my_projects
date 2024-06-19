def get_fact(x):
  factors = []
  for i in range(1,x+1):
    if x%i == 0:
      factors.append(i)
  
  return factors
  
      
def mult(x,y):
  return x*y
