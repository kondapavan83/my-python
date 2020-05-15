def hello(func):
  def h1():
    return(func)
  print(h1())
  print("hello")
  print(h1())


def dec(p):
  return ("{}".format(p*10))
