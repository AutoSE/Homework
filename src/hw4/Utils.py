import math
import sys
import re
import math
import copy
import json
from pathlib import Path
Seed = 937162211

def settings(s):
    return dict(re.findall("\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)",s))

#Numerics
def rint(lo, hi):
    return math.floor(0.5 + rand(lo, hi))

def rand(lo, hi):
    lo= lo or 0
    hi= hi or 1
    global Seed
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi-lo) * Seed / 2147483647

def rnd(n, nPlaces=3    ):
    mult = 10**nPlaces 
    return math.floor(n * mult + 0.5) / mult

def cosine(a, b, c):
    x1 = (a**2 + c**2 - b**2) / (2**c)
    x2 = max(0, min(1, x1))
    y  = (a**2 - x2**2)**0.5
    return x2, y


#Strings
def fmt(sControl):
    return str(sControl)

def oo(t):
    d = t.__dict__
    d['a'] = t.__class__.__name__
    d['id'] = id(t)
    d = dict(sorted(d.items()))
    print(d)

def coerce(s):
    if s=='true' or s=='True':
        return True
    elif s=='false' or s=='False':
        return False
    elif s.isdigit():
        return int(s)
    elif '.' in s:
        if s.replace('.','').isdigit():
            return float(s)
        else:
            return s
    else:
        return s

def csv(sFilename, fun):
    sFilename=Path(sFilename)
    t=[]
    f=open(sFilename.absolute(),'r')
    lines=f.readlines()
    for line in lines:
        t=[]
        for s in re.findall("([^,]+)", line):
            t.append(coerce(s))
        fun(t)


#Lists
def map(t, fun):
    u={}
    for v in t:
        k=fun(v)
        if k:
            u[k]=v
        else:
            u[1+len(u)]=v
    return u

def kap(t, fun):
    u={}
    for k,v in enumerate(t):
        v,k=fun(k,v)
        if k:
            u[k]=v
        else:
            u[1+len(u)]=v
    return u

def any(t):
    return t[rint(0,len(t)-1)]

def many(t,n):
   u=[]
   for i in range(1,n+1):
    u.append(any(t))
   return u

def show(node, what, cols, nPlaces, lvl =0):
    if node:
        print('| ' * lvl + str(len(node['data'].rows)) + '  ', end = '')
        if not node.get('left') or lvl==0:
            print(node['data'].stats("mid",node['data'].cols.y,nPlaces))
        else:
            print('')
        show(node.get('left'), what,cols, nPlaces, lvl+1)
        show(node.get('right'), what,cols,nPlaces, lvl+1)

def deepcopy(t):
    return copy.deepcopy(t)

def repCols(cols, DATA):
    cols = deepcopy(cols)
    for col in cols:
        col[len(col) - 1] = col[0] + ":" + col[len(col) - 1]
        for j in range(1, len(col)):
            col[j-1] = col[j]
        col.pop()
    first_col = ['Num' + str(k+1) for k in range(len(cols[1])-1)]
    first_col.append('thingX')
    cols.insert(0, first_col)
    return DATA(cols)

def repRows(t, DATA, rows):
    rows = deepcopy(rows)
    for j, s in enumerate(rows[-1]):
        rows[0][j] = rows[0][j] + ":" + s
    rows.pop()
    for n, row in enumerate(rows):
        if n == 0:
            row.append('thingX')
        else:
            u = t['rows'][- n]
            row.append(u[len(u) - 1])
    return  DATA(rows)

def dofile(sFile):
    file = open(sFile, 'r', encoding='utf-8')
    text  = re.findall(r'(?<=return )[^.]*', file.read())[0].replace('{', '[').replace('}',']').replace('=',':').replace('[\n','{\n' ).replace(' ]',' }' ).replace('\'', '"').replace('_', '"_"')
    file.close()
    return json.loads(re.sub("(\w+):", r'"\1":', text))

def transpose(t):
    u=[]
    for i in range(len(t[1])):
        u.append([])
        for j in range(len(t)):
            u[i].append(t[j][i])
    return 

def repgrid(sFile, DATA):
    t = dofile(sFile)
    rows = repRows(t, DATA, transpose(t['cols']))
    cols = repCols(t['cols'], DATA)
    show(rows.cluster(),"mid",rows.cols.all,1)
    show(cols.cluster(),"mid",cols.cols.all,1)
    repPlace(rows)

def repPlace(data):
    n,g = 20,{}
    for i in range(1, n+1):
        g[i]={}
        for j in range(1, n+1):
            g[i][j]=' '
    maxy = 0
    print('')
    for r,row in enumerate(data.rows):
        c = chr(97+r).upper()
        print(c, row.cells[-1])
        x,y= row.x*n//1, row.y*n//1
        maxy = int(max(maxy,y+1))
        g[y+1][x+1] = c
    print('')
    for y in range(1,maxy+1):
        print(' '.join(g[y].values()))