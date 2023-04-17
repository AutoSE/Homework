import cli as c
import num as n
import sym as s
import Utils as u
import os
import random

egs={}

def ok(n=1):
    random.seed(n)

def samples():
    for i in range(1,11):
        print("",''.join(u.samples(["a","b","c","d","e"])))

def num():
    k=n.Num([1,2,3,4,5,6,7,8,9,10])
    print("",k.n, k.mu, k.sd)

def gaussian():
    t=[]
    for i in range(1, 10001):
        t.append(u.gaussian(10, 2))
    k=n.Num(t)
    print("",k.n, k.mu, k.sd)

def bootmu():
    a,b=[],[]
    for i in range(1,101):
        a.append(u.gaussian(10,1))
    print("","mu ","sd","cliffs","boot","both")
    print("","---","--","------","----","----")
    tmp=[10+(x*0.1) for x in range(0, 11)]
    for mu in tmp:
        b=[]
        for i in range(1,100+1):
            b.append(u.gaussian(mu,1))
        cl=u.cliffsDelta(a, b)
        bs=u.bootstrap(a,b)
        print("",mu,1,cl,bs,cl and bs)

def basic():
    print("\t\ttruee",u.bootstrap([8, 7, 6, 2, 5, 8, 7, 3],[8, 7, 6, 2, 5, 8, 7, 3]),u.cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3],[8, 7, 6, 2, 5, 8, 7, 3]))
    print("\t\tfalse",u.bootstrap([8, 7, 6, 2, 5, 8, 7, 3],[9, 9, 7, 8, 10, 9, 6]),u.cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3],[9, 9, 7, 8, 10, 9, 6])) 
    print("\t\tfalse",u.bootstrap([0.34, 0.49, 0.51, 0.6,0.34,0.49,0.51,0.6],[0.6,0.7,0.8,0.9,0.6,0.7,0.8,0.9]),u.cliffsDelta([0.34,0.49,0.51,0.6,0.34,0.49,0.51,0.6],[0.6,0.7,0.8,0.9,0.6,0.7,0.8,0.9]))

def pre():
    print('eg3')
    d=1
    for i in range(1,11):
        t1,t2=[],[]
        for j in range(1, 33):
            t1.append(u.gaussian(10,1))
            t2.append(u.gaussian(d*10,1))
        print('\t',d,True if d<1.1 else False, u.bootstrap(t1, t2), u.bootstrap(t1, t1))
        d=d+0.05

def five():
    for rx in u.tiles(u.scottKnot([u.RX([0.34,0.49,0.51,0.6,.34,.49,.51,.6],"rx1"),u.RX([0.6,0.7,0.8,0.9,.6,.7,.8,.9],"rx2"),u.RX([0.15,0.25,0.4,0.35,0.15,0.25,0.4,0.35],"rx3"),u.RX([0.6,0.7,0.8,0.9,0.6,0.7,0.8,0.9],"rx4"),u.RX([0.1,0.2,0.3,0.4,0.1,0.2,0.3,0.4],"rx5")])):
        print(rx['name'],rx['rank'],rx['show'])

def six():
    for rx in u.tiles(u.scottKnot([u.RX([101,100,99,101,99.5,101,100,99,101,99.5],"rx1"),u.RX([101,100,99,101,100,101,100,99,101,100],"rx2"),u.RX([101,100,99.5,101,99,101,100,99.5,101,99],"rx3"),u.RX([101,100,99,101,100,101,100,99,101,100],"rx4")])):
        print(rx['name'],rx['rank'],rx['show'])

def tiles():
    rxs,a,b,c,d,e,f,g,h,j,k=[],[],[],[],[],[],[],[],[],[],[]
    for i in range(0,1000):
        a.append(u.gaussian(10,1))
    for i in range(0,1000):
        b.append(u.gaussian(10.1,1))
    for i in range(0,1000):
        c.append(u.gaussian(20,1))
    for i in range(0,1000):
        d.append(u.gaussian(30,1))
    for i in range(0,1000):
        e.append(u.gaussian(30.1,1))
    for i in range(0,1000):
        f.append(u.gaussian(10,1))
    for i in range(0,1000):
        g.append(u.gaussian(10,1))
    for i in range(0,1000):
        h.append(u.gaussian(40,1))
    for i in range(0,1000):
        j.append(u.gaussian(40,3))
    for i in range(0,1000):
        k.append(u.gaussian(10,1))
    for k,v in enumerate([a,b,c,d,e,f,g,h,j,k]):
        rxs.append(u.RX(v,"rx"+str(k+1)))
    for i,x in enumerate(rxs):
        for z,y in enumerate(rxs):
            if u.mid(x) < u.mid(y):
                rxs[z],rxs[i]=rxs[i],rxs[z]
    for rx in u.tiles(rxs):
        print("",rx['name'],rx['show'])

def sk():
    rxs,a,b,c,d,e,f,g,h,j,k=[],[],[],[],[],[],[],[],[],[],[]
    for i in range(0,1000):
        a.append(u.gaussian(10,1))
    for i in range(0,1000):
        b.append(u.gaussian(10.1,1))
    for i in range(0,1000):
        c.append(u.gaussian(20,1))
    for i in range(0,1000):
        d.append(u.gaussian(30,1))
    for i in range(0,1000):
        e.append(u.gaussian(30.1,1))
    for i in range(0,1000):
        f.append(u.gaussian(10,1))
    for i in range(0,1000):
        g.append(u.gaussian(10,1))
    for i in range(0,1000):
        h.append(u.gaussian(40,1))
    for i in range(0,1000):
        j.append(u.gaussian(40,3))
    for i in range(0,1000):
        k.append(u.gaussian(10,1))
    for k,v in enumerate([a,b,c,d,e,f,g,h,j,k]):
        rxs.append(u.RX(v,"rx"+str(k+1)))
    for rx in u.tiles(u.scottKnot(rxs)):
        print("",rx['rank'],rx['name'],rx['show'])

def all():
    print('ok')
    egs['ok']=ok()
    print('samples')
    egs['samples']=samples()
    print('num')
    egs['num']=num()
    print('gaussian')
    egs['gaussian']=gaussian()
    print('bootmu')
    egs['bootmu']=bootmu()
    print('basic')
    egs['basic']=basic()
    print('pre')
    egs['pre']=pre()
    print('five')
    egs['five']=five()
    print('six')
    egs['six']=six()
    print('tiles')
    egs['tiles']=tiles()
    print('sk')
    egs['sk']=sk()


