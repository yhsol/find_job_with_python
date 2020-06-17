def plus(a, b):
  if type(float(a)) != float or type(float(b)) != float:
    return "not correct value type!"
  if type(a) == bool or type(b) == bool:
    return "not correct value type!"
  a = float(a)
  b = float(b)
  return a + b

def minus(a = 0, b = 0):
  a = float(a)
  b = float(b)
  return a - b

def multiplication(a = 0, b = 0):
  a = float(a)
  b = float(b)
  return a * b

def division(a = 0, b = 0):
  a = float(a)
  b = float(b)
  return a / b

def quota(a = 0, b = 0):
  a = float(a)
  b = float(b)
  return a % b

result = plus(3.3, 3.5)
print(result)
print(type(3) != float and type("3") != float)