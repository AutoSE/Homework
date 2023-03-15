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

def copy():
    t1 = {'a' : 1, 'b' : { 'c' : 2, 'd' : [3]}}
    t2 = u.deepcopy(t1)
    t2['b']['d'][0] = 10000
    print('b4', t1, '\nafter', t2)

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

def t_repCols():
    t = u.repCols(u.dofile(c.the['file'])['cols'], d.Data)
    _ = list(map(u.oo, t.cols.all))
    _ = list(map(u.oo, t.rows))

def synonyms():
    data = d.Data(c.the['file'])
    u.show(u.repCols(u.dofile(c.the['file'])['cols'], d.Data).cluster(),"mid",data.cols.all,1)

def t_repRows():
    t=u.dofile(c.the['file'])
    rows = u.repRows(t, d.Data, u.transpose(t['cols']))
    _ = list(map(u.oo, rows.cols.all))
    _ = list(map(u.oo, rows.rows))

def prototypes():
    t = u.dofile(c.the['file'])
    rows = u.repRows(t, d.Data, u.transpose(t['cols']))
    u.show(rows.cluster(),"mid",rows.cols.all,1)

def position():
    t = u.dofile(c.the['file'])
    rows = u.repRows(t, d.Data, u.transpose(t['cols']))
    rows.cluster()
    u.repPlace(rows)

def every():
    u.repgrid(c.the['file'], d.Data)

def all():
    print('the')
    egs['the']=the()
    print('copy')
    egs['copy']=copy()
    print('sym')
    egs['sym']=sym()
    print('num')
    egs['num']=num()
    print('repCols')
    egs['repCols']=t_repCols()
    print('synonyms')
    egs['synonyms']=synonyms()
    print('repRows')
    egs['repRows']=t_repRows()
    print('every')
    egs['every']=every()
    print('position')
    egs['position']=position()
    print('prototypes')
    egs['prototypes']=prototypes()
