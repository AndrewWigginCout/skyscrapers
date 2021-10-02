from itertools import permutations, product
 
class skyscraper:
    def __init__(self,clues):
        self.g=[]
        for i in range(4):
            self.g.append([0,0,0,0])
        self.clues=self.clues
    def find_doubles():
        rv=[]
        for i in range(4):
            if self.clues[i]>0 and self.clues[11-i]>0: rv.append(i)
        for i in range(4,8):
            if self.clues(i)>0 and self.clues[19-i]>0: rv.append(i)
        return rv
        
    def iterate_on_doubles():
        for i in find_doubles():
            if i<4:
                v=[self.g[y][i] for y in range(4)]
                v.append(self.clues[i])
                v.append(self.clues[11-i])
                print(v)
                
def check_row(v):
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

test.describe ("4 by 4 skyscrapers")
test.it ("should pass all the tests provided")

test.assert_equals (solve_puzzle (clues[0]), outcomes[0])
test.assert_equals (solve_puzzle (clues[1]), outcomes[1])