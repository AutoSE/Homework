import Utils as u
import Cols as c
import cli as g
import Row as r
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
            t=t if str(type(t))=='Row' else r.Row(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols=c.Cols(t)

    def clone(self, init):
        data=Data(self.cols.names)
        u.map(init,lambda x: data.add(x)) if init else u.map([],lambda x: data.add(x))

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

    def dist(self, row1, row2, cols):
        n,d = 0,0
        for _,col in (cols.items() if cols else  self.cols.x.items()):
            n = n + 1
            d = d + col.dist(row1.cells[col.at], row2.cells[col.at])**g.the["p"]
        return (d/n)**(1/g.the["p"])