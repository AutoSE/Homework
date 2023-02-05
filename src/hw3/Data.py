import Utils as u
import Cols as c
import cli as g
import Row as r
import num as n
import math
from operator import itemgetter
class Data:
    def __init__(self, src):
        self.rows=[]
        self.cols=None
        fun= lambda x: self.add(x)
        if type(src)==str:
            u.csv(src,fun)
        else:
            u.map(src,fun) if src else u.map({},fun)

    def add(self,t):
        if self.cols:
            t=t if "Row" in str(type(t)) else r.Row(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols=c.Cols(t)

    def clone(self, init):
        return self

    def stats(self, what, cols, nPlaces):
        def fun(k,col):
            if what=='mid':
                val=col.mid()
            else:
                val=col.div()
            return col.rnd(val, nPlaces),col.txt
        if cols:
            return u.kap(cols, fun)
        else:
            return u.kap(self.cols.y, fun)

    def better(self, row1, row2):
        s1,s2,ys,x,y=0,0,self.cols.y
        for col in ys:
            x=col.norm(row1.cells[col.at])
            y=col.norm(row2.cells[col.at])
            s1=s1-math.exp(col.w*(x-y)/len(ys))
            s2=s2-math.exp(col.w*(y-x)/len(ys))
            return s1/len(ys) < s2/len(ys)

    def dist(self, row1, row2, cols=None):
        n,d = 0,0
        for col in (cols or self.cols.x):
            n = n + 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at])**g.the["p"]
        return (d/n)**(1/g.the["p"])

    def around(self, row1, rows=None, cols=None):
        def function(row2):
            return {'row' : row2, 'dist' : self.dist(row1,row2,cols)} 
        return sorted(list(map(function, rows or self.rows)), key= lambda k: k['dist'])

    def half(self, rows=None, cols=None, above=None):
        def dist(row1, row2):
            return self.dist(row1, row2, cols)
        rows=rows or self.rows
        some=u.many(rows, g.the['Sample'])
        A=above or u.any(some)
        B=self.around(A, some)[int((float(g.the['Far'])*len(rows)))]['row']
        c=dist(A,B)
        left,right=[],[]
        
        def project(row):
            return {'row': row, 'dist': u.cosine(dist(row, A), dist(row,B), c)}
        for n, tmp in enumerate(sorted(list(map(project, rows)), key=itemgetter('dist'))):
            if n<=len(rows)//2:
                left.append(tmp['row'])
                mid=tmp['row']
            else:
                right.append(tmp['row'])
        return left, right, A,B,mid,c
