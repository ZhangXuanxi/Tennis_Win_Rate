import numpy as np
import math

def exceed2(p):
    return p*p/(1-2*p*(1-p))


def win_game(p,n):
    ans=0
    for i in range(n,2*n-1):
        ans+=math.comb(i-1,n-1)*p**n*(1-p)**(i-n)
    ans+=(1-p)**(n-1)*p**(n-1)*math.comb(2*n-2,n-1)*exceed2(p)
    return ans 

def win_set(p,n,p7):
    ans=0
    for i in range(n,2*n-1):
        ans+=math.comb(i-1,n-1)*p**n*(1-p)**(i-n)
    ans+=(1-p)**(n-1)*p**(n-1)*math.comb(2*n-2,n-1)*(p*p+2*p*(1-p)*p7)
    return ans  

def win_match(p,n):
    ans=0
    for i in range(n,2*n):
        ans+=math.comb(i-1,n-1)*p**n*(1-p)**(i-n)
    return ans





if __name__ == '__main__':
    
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12,5))
    x=np.linspace(0,1,500)
    plt.plot(x, exceed2(x))
    plt.savefig('exceed2.png')

    plt.figure(figsize=(12,5))
    plt.plot(x, win_game(x,4))
    plt.grid(visible=True)
    plt.xlabel('point win rate')
    plt.ylabel('game win rate')
    plt.savefig('game.png')

    set_win=[win_set(win_game(p,4),6,win_game(p,7))for p in x]
    plt.figure(figsize=(12,5))
    plt.plot(x, set_win)
    plt.grid(visible=True)
    plt.xlabel('point win rate')
    plt.ylabel('set win rate')
    plt.savefig('set.png')

    plt.figure(figsize=(12,5))
    plt.plot(x, [win_match(k,2) for k in set_win])
    plt.grid(visible=True)
    plt.scatter(0.54, win_match(win_set(win_game(0.54,4),6,win_game(0.54,7)),2),c='r')
    plt.xlim(0.4,0.6)
    plt.xlabel('point win rate')
    plt.ylabel('match win rate')
    plt.savefig('match.png')

    
    p=0.54
    pg=win_game(p,4)
    ps=win_set(pg,6,win_game(p,7))
    p3=win_match(ps,3)
    print(p,pg,ps,p3)
    
    
    print(win_set(win_game(0.54,4),6,win_game(0.54,7)))
    print(win_set(win_game(0.46,4),6,win_game(0.46,7)))

    print(win_game(0.54,2),win_game(0.46,2))