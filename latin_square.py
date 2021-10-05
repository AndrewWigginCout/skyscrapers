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
        if j == y: continue
        if g[j][x] != 0:
            if g[j][x] in available: available.remove(g[j][x])
    for i in range(N):
        if i == x: continue
        if g[y][i] != 0:
            if g[y][i] in available: available.remove(g[y][i])
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
N=3
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

for each in rv:
    print(printg(each))