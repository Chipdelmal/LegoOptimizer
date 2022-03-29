from itertools import groupby

def runLength(s_list):
    # https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-75.php
    grp = groupby(s_list)
    runL = tuple([tuple([len(list(group)), key]) for key, group in grp])
    return runL

def flatten(t):
    # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
    return [item for sublist in t for item in sublist]


class NotFound(BaseException):
    pass

from collections import defaultdict
def subsetsum(A,N):
    res=[[0]]+[[] for i in range(N)]
    for i,a in enumerate(A):
        k=1<<i        
        stop=[len(l) for l in res] 
        for shift,l in enumerate(res[:N+1-a]):
            n=a+shift   
            ln=res[n]
            for s in l[:stop[shift]]: ln.append(s+k)
    return res

res = subsetsum(A,max(B))
solB = [res[b] for b in B]
exactsol = ~-(1<<len(A))

def decode(answer):
    return [[A[i] for i,b in enumerate(bin(sol)[::-1]) if b=='1'] for sol in answer] 

def solve(i,currentsol,answer):
        if currentsol==exactsol : print(decode(answer))
        if i==len(B): return
        for sol in solB[i]:
                if not currentsol&sol:
                    answer.append(sol)
                    solve(i+1,currentsol+sol,answer)
                    answer.pop()