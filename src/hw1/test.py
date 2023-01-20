



import cli as c
import Num as n
import Sym as s
import random
import Utils as u


#sys.path.insert(0, os.getcwd())
#print(os.getcwd())
#print(sys.path)


egs={}
def the():
  #print(c.the)
  return True

def rand():
  num1,num2 = n.Num(),n.Num()
  seed=c.the['seed']
  
  for i in range(1,1001):
    num1.add(u.rand(0,1))
  seed=c.the['seed']
  
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

print(the())
print(rand())
#print(sym())
print(num())
'''
def rand():
  text="generate, reset, regenerate same"
  num1,num2 = NUM(),NUM()
  Seed=the.seed; for i=1,10^3 do num1:add( rand(0,1) ) end
  Seed=the.seed; for i=1,10^3 do num2:add( rand(0,1) ) end
  local m1,m2 = rnd(num1:mid(),10), rnd(num2:mid(),10)
  return m1==m2 and .5 == rnd(m1,1) end 


eg("rand","generate, reset, regenerate same", function()
  local num1,num2 = NUM(),NUM()
  Seed=the.seed; for i=1,10^3 do num1:add( rand(0,1) ) end
  Seed=the.seed; for i=1,10^3 do num2:add( rand(0,1) ) end
  local m1,m2 = rnd(num1:mid(),10), rnd(num2:mid(),10)
  return m1==m2 and .5 == rnd(m1,1) end )

eg("sym","check syms", function()
  local sym=SYM()
  for _,x in pairs{"a","a","a","a","b","b","c"} do sym:add(x) end
  return "a"==sym:mid() and 1.379 == rnd(sym:div())end)

eg("num", "check nums", function()
  local num=NUM()
  for _,x in pairs{1,1,1,1,2,2,3} do num:add(x) end
  return 11/7 == num:mid() and 0.787 == rnd(num:div()) end )
  '''
