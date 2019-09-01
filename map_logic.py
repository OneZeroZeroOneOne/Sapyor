
from loguru import logger
import random



def mapa():
    x = 7
    y = 9
    bombs = 12
    l = [[0 for i in range(0,x+1)] for i in range(0,y+1)]
    for i in l:
        print(i)
    while(bombs>0):
        a = random.randint(0,y)
        b = random.randint(0,x)
        if l[a][b]==0:
            l[a][b]=9
            bombs-=1
    print("________________________")
    for i in range(0,y+1):
        for j in range(0,x+1):
            if l[i][j]>=9:
                if i>0:
                    l[i-1][j]+=1
                    if j>0:
                        l[i-1][j-1]+=1
                    if j<x:
                        l[i-1][j+1]+=1
                if i<y:
                    l[i+1][j]+=1
                    if j>0:
                        l[i+1][j-1]+=1
                    if j<x:
                        l[i+1][j+1]+=1
                if j>0:
                    l[i][j-1]+=1
                if j<x:
                    l[i][j+1]+=1
    for i in range(0,y+1):
        for j in range(0,x+1):
            if l[i][j]>=9:
                l[i][j]="*"
            else:
                l[i][j]= str(l[i][j])
    for i in l:
        print(i)
    return l
