import cli as c
import num as n
import sym as s
import Utils as u
import os
import Data as d

egs={}
line=0

def the():
    print(c.the)
    egs['the'] = c.the
    return True

def rand():
    Seed = 1
    t=[]
    for i in range(1,1000+1):
        t.append(u.rint(0,100,1))
    Seed=1
    U=[]
    for i in range(1,1000+1):
        U.append(u.rint(0,100,1))
    for k,v in enumerate(t):
        assert(v==U[k])

def some():
    c.the['Max'] = 32
    num1 = n.Num()
    for i in range(1,10001):
        num1.add(i)
    print(num1.has)

def nums():
    num1, num2 = n.Num(),n.Num()
    global Seed
    Seed = c.the['seed']
    for i in range(1,10001):
        num1.add(u.rand(0,1))
    Seed = c.the['seed']
    for i in range(1,10001):
        num2.add(u.rand(0,1)**2)
    m1,m2 = u.rnd(num1.mid(),1), u.rnd(num2.mid(),1)
    d1,d2 = u.rnd(num1.div(),1), u.rnd(num2.div(),1)
    print(1, m1, d1)
    print(2, m2, d2) 
    return m1 > m2 and .5 == u.rnd(m1,1)

def syms():
    sym_obj = s.Sym()
    for k,x in enumerate(["a","a","a","a","b","b","c"]):
        sym_obj.add(x)
    print(sym_obj.mid(), u.rnd(sym_obj.div()))
    return 1.379 == u.rnd(sym_obj.div())

def csv():
    def fn(t):
        global numberofchars
        numberofchars+=len(t)
    global numberofchars
    numberofchars=0
    u.csv(c.the['file'],fn)
    return 3192==numberofchars

def data():
    data = d.Data(c.the["file"])
    return len(data.rows) == 398 and data.cols.y[0].w == -1 and data.cols.x[1].at == 1 and len(data.cols.x) == 4

def clone():
    data1 = d.Data(c.the["file"])
    data2 = data1.clone(data1.rows)
    return len(data1.rows) == len(data2.rows) and data1.cols.y[1].w == data2.cols.y[1].w and data1.cols.x[1].at == data2.cols.x[1].at and len(data1.cols.x) == len(data2.cols.x)

def around():
    data = d.Data(c.the["file"])
    print(0,0,data.rows[1].cells)
    for n,t in enumerate(data.around(data.rows[1])):
        if n%50==0:
            print(n,u.rnd(t['dist'],2),t['row'].cells)

def half():
    data=d.Data(c.the['file'])
    left,right,A,B,mid,C=data.half()
    print(len(left),len(right),len(data.rows))
    print(A.cells,C)
    print(mid.cells)
    print(B.cells)

def cluster():
    data = d.Data(c.the['file'])
    u.show(data.cluster(), "mid", data.cols.y, 1)

def optimize():
    data = d.Data(c.the['file'])
    u.show(data.sway(),'mid',data.cols.y, 1)

def all():
    print('the')
    egs['the']=the()
    print('rand')
    egs['rand']=rand()
    print('some')
    egs['some']=some()
    print('nums')
    egs['nums']=nums()
    print('syms')
    egs['syms']=syms()
    print('csv')
    egs['csv']=csv()
    print('data')
    egs['data']=data()
    print('clone')
    egs['clone']=clone()
    print('around')
    egs['around']=around()
    print('half')
    egs['half']=half()
    print('cluster')
    egs['cluster']=cluster()
    print('optimize')
    egs['optimize']=optimize()
