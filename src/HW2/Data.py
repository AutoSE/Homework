import Utils as u
import Cols as c
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
            return kap(cols, fun)
        else:
            return kap(self.cols.y, fun)
