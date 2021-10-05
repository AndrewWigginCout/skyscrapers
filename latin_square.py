# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 14:22:59 2021

@author: X
"""
import copy
#def latin_square(g):
#    for i in range(16):
#        if g[i/4][i%4]=0:
#            nadjv=not_adjacent(i)
#            for e in nadjv:
#                g[i/4][i%4]=e
#                solv=latin_square(g)
#                if
def printg(g):
    rv=''
    for row in g:
        for cell in row:
            rv+=str(cell)
        rv+='\n'
    rv+='\n'
    return rv
def solved(g):
    for y in range(N):
        for x in range(N):
            if g[y][x]==0: return False
    return True

def list_available(y,x,g):
    available = [k for k in range(1,N+1)]
    for j in range(N):
        if j != y and g[j][x] != 0 and g[j][x] in available:
            available.remove(g[j][x])
    for i in range(N):
        if i != x and g[y][i] != 0 and g[y][i] in available:
            available.remove(g[y][i])
    return available
def find_empty(g):
    for y in range(N):
        for x in range(N):
            if g[y][x]==0: return y,x
    return None
count=0
full=''
def guess(g,depth=0):
    rv=[]
    #print("depth={}\n{}".format(depth,printg(g)))
    if solved(g):
        #printg(g)
        #global full
        #full+=printg(g)
        
        return[copy.deepcopy(g)]
    y,x = find_empty(g)
    #print(y,x)
    available = list_available(y,x,g)
    for possible in available:
        g[y][x] = possible
        rv.extend(guess(g,depth+1))
        g[y][x]= 0
    return rv
N=4
g=[
   [0]*N for i in range(N)
   ]
g2=[
    [1,1,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]
#def decodeg(n):
#    for ch in :
#        

rv=guess(g)
def valid_skyscraper_grid(g,clues):
    #down
    for i in range(4):
        if clues[i]==0: continue
        max=g[0][i]
        count=1
        for j in range(1,4):
            if g[j][i]>max:
                count+=1
                max=g[j][i]
        if count!=clues[i]: return False
        
    #up
    for i in range(4):
        if clues[11-i]==0: continue
        max=g[3][i]
        count=1
        for j in range(2,-1,-1):
            if g[j][i]>max:
                count+=1
                max=g[j][i]
        if count!=clues[11-i]: return False
    
    #right
    for j in range(4):
        expected=clues[15-j]
        if clues[15-j]==0: continue
        max=g[j][0]
        count=1
        for i in range(1,4):
            if g[j][i]>max:
                count+=1
                max=g[j][i]
        if count!=clues[15-j]: return False
                
    #left
    for j in range(4):
        z=clues[j+4]
        if clues[j+4]==0: continue
        max=g[j][3]
        count=1
        for i in range(2,-1,-1):
            a=g[j][i]
            if g[j][i]>max:
                count+=1
                max=g[j][i]
        if count!=clues[j+4]: return False
    return True    

def solve_puzzle(clues):
    rv2=[]
    for each in rv:
        if valid_skyscraper_grid(each,clues):
            rv2.append(each)
    return rv2

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

rv2=solve_puzzle(clues[0])