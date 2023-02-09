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

def sym():
    sym_obj = s.Sym()
    for k,x in enumerate(["a","a","a","a","b","b","c"]):
        sym_obj.add(x)
    egs['sym'] = "a" == sym_obj.mid() and 1.379 == u.rnd(sym_obj.div())
    return "a" == sym_obj.mid() and 1.379 == u.rnd(sym_obj.div())

def num():
    num_obj = n.Num()
    for k,x in enumerate([1,1,1,1,2,2,3]):
        num_obj.add(x)
    egs['num'] = 11/7 == num_obj.mid() and 0.787 == u.rnd(num_obj.div())
    return 11/7 == num_obj.mid() and 0.787 == u.rnd(num_obj.div())


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
    print('data')
    egs['data']=data()
    print('sym')
    egs['sym']=sym()
    print('num')
    egs['num']=num()
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
