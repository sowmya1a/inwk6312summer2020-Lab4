import os

lst=[]
def check(dirname):
  for name in os.listdir(dirname):
    path= os.path.join(dirname,name)
    if os.path.isfile(path):
      lst.append(path)
    else: 
      check(path)
  return lst


print(check('documents'))
