import cli as c
import Num as n
import Sym as s
import random
import Utils as u


#sys.path.insert(0, os.getcwd())
#egs[]=(os.getcwd())
#egs[]=(sys.path)
egs={}
def the():
  #egs[]=(c.the)
  return True

def rand():
  num1,num2 = n.Num(),n.Num()
  u.Seed=c.the['seed']
  for i in range(1,1001):
    num1.add(u.rand(0,1))
  u.Seed=c.the['seed']
  
  for i in range(1,1001):
    num2.add(u.rand(0,1))
  m1,m2 = u.rnd(num1.mid(),10) , u.rnd(num2.mid(),10)
  return m1==m2 and 0.5 == u.rnd(m1,1)

def sym():
  sym=s.Sym()
  for i,x in enumerate(["a","a","a","a","b","b","c"]):
    sym.add(x)
  return "a"==sym.mid() and 1.379==u.rnd(sym.div())

def num():
  num=n.Num()
  for i,x in enumerate([1,1,1,1,2,2,3]):
    num.add(x)
  return 11/7==num.mid() and 0.787==u.rnd(num.div(),3)

def all():
  egs['the']=the()
  egs['rand']=rand()
  egs['sym']=sym()
  egs['num']=num()