#https://www.codewars.com/kata/5671d975d81d6c1c87000022/train/python
from itertools import permutations, product
import copy
 
default=[1,2,3,4]
blank=[
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]
       ]
class skyscraper:
    def __init__(self,g,clues):
#        self.g=[]
#        for i in range(4):
#            self.g.append([0,0,0,0])
        self.clues=clues
#        print(self.g)
        self.g=g
        print(self.clues)
    def find_doubles(self):
        rv=[]
        for i in range(4):
            if self.clues[i]>0 and self.clues[11-i]>0: rv.append(i)
        for i in range(4,8):
            if self.clues[i]>0 and self.clues[19-i]>0: rv.append(i)
        print("find doubles= ",rv)
        return rv
        
    def iterate_on_doubles(self):
        for i in self.find_doubles():
            if i<4:
                v=[self.g[y][i] for y in range(4)]
                v.append(self.clues[i])
                v.append(self.clues[11-i])
                
                for row in solve_row(v):
                    g2=copy.deepcopy(self.g)
                    for y in range(4):
                        g2[y][i]=row[y]
                    printg(g2)
    def fill_row(self,i):
        if i<4:
            for y in range(4):
                v.append(self.g[y][i])
            v.append(self.clues[i])
            v.append(self.clues[11-i])
            
            for prow in solve_row(v):
                for y in range(4):
                    #collect all others and compare
                    for x in range(4):
                        if x==i: continue
                        if g[y][x]==
                        used=[g[i][x]]
def compare_column(i,j,g):
    allowable=[1,2,3,4]
    for y in range(4):
        if x == i: continue
        if g[y][i]==0: continue
        allowable.remove(g[y][i])
        return allowable
def compare_row(i,j,g):
    allowable=[1,2,3,4]
    for x in range(4):
        if x==i: continue
        if g[j][i]==0: continue
        allowable.remove(g[j][x])
    return allowable
def check_row(v):
    #print("check row v=",v)
    max=v[0]
    count=[1,1]
    for i in range(1,4):
        if v[i]>max:
            max=v[i]
            count[0]+=1
    max=v[3]
    for i in range(2,-1,-1):
        if v[i]>max:
            max=v[i]
            count[1]+=1
    if v[4]>0 and v[4]!=count[0]: return False
    if v[5]>0 and v[5]!=count[1]: return False
    return True
def possible_rows(v):
    for p in permutations(range(1,5)):
        if passes(p,v):
            p=list(p)
            p.extend([v[4],v[5]])
            rv.append(p)
    return rv
def passes(p,v):
    pass
def solve_row(v):
    print("solve row v=",v)
    rv=[]
    #count=0
    #already=[v[i] for i in range(4) if v[i]>0 ]
    a = set(v[0:4])
    needed = set((1,2,3,4))-a
#    print("needed=",needed)
    ps=permutations(needed)
    for p in ps:
#        print("p=",p)
        w=drop_in(p,v)
        if check_row(w): rv.append(w)
    for each in rv:
        pass
        print(each)
    return(rv)
        
def drop_in(p,w):
#    print("p,w=",list(p),w)
    v=copy.copy(w)
#    print("v=",v)
    pi=0
    for i in range(4):
        if v[i]==0:
            v[i]=p[pi]
            pi+=1
    return(v)
        
def printg(g):
    for row in g:
        for c in row:
            print(c,end='')
        print('')
    print('')
#for i in range(16):
#s=''
#for p in product([0,1,2,3,4],[0,1,2,3,4]):
#    for v in permutations(range(1,5)):
#        v=list(v)
#        v.append(p[0])
#        v.append(p[1])
#        myb=check_row(v)
#        if myb: s+=str(v)+'\n'
#print(s)
#for v in permutations(range(1,5)):
#    print(v)
    
clues = (
( 2, 2, 1, 3,  
  2, 2, 3, 1,  
  1, 2, 2, 3,  
  3, 2, 1, 3 ),
( 0, 0, 1, 2,   
  0, 2, 0, 0,   
  0, 3, 0, 0, 
  0, 1, 0, 0 )
)

outcomes = (
( ( 1, 3, 4, 2 ),       
  ( 4, 2, 1, 3 ),       
  ( 3, 4, 2, 1 ),
  ( 2, 1, 3, 4 ) ),
( ( 2, 1, 4, 3 ), 
  ( 3, 4, 1, 2 ), 
  ( 4, 2, 3, 1 ), 
  ( 1, 3, 2, 4 ) )
)

#test.describe ("4 by 4 skyscrapers")
#test.it ("should pass all the tests provided")
#
#test.assert_equals (solve_puzzle (clues[0]), outcomes[0])
#test.assert_equals (solve_puzzle (clues[1]), outcomes[1])

x = skyscraper(blank,clues[0])
x.iterate_on_doubles()

#v=[0,0,0,0,1,3]
#p=[1,2,4,3]
#solve_row(v)