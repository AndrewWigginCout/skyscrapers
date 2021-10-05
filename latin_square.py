# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 14:22:59 2021

@author: X
"""
N=4
#def latin_square(g):
#    for i in range(16):
#        if g[i/4][i%4]=0:
#            nadjv=not_adjacent(i)
#            for e in nadjv:
#                g[i/4][i%4]=e
#                solv=latin_square(g)
#                if
def solved(g):
    for row in g:
        for cell in row:
            print(cell,end="")
        print("")
    print("")
def test(g):
    for y in range(N):
        for x in range(N):
            if g[y][x]==0: return False
    return True

def list_available(y,x,g):
    available = [k for k in range(1,N+1)]
    for j in range(N):
        for i in range(N):
            if (j,i) == (y,x): continue
            if g[j][i] != 0: available.remove(g[j][i])
    return available

def guess(g,depth=0):
    solved(g)
    print("depth=",depth)
    if test(g):
        solved(g)
        return
    for y in range(4):
        for x in range(4):
            if g[y][x]: continue
            available = list_available(y,x,g)
            for possible in available:
                g[y][x] = possible
                guess(g,depth+1)
                g[y][x]=0
            
g=[
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]]

guess(g)