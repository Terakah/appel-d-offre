# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:22:43 2021

@author: TeRaKa
"""

import numpy
import math
import matplotlib


"On considère que la biomasse produite est proportionnelle à la quantité de substrat consommé, sans que"
"ce dernier soit renouvelé. Le coefficient de proportionnalité, noté R, correspond au rendement de"
"conversion du substrat en biomasse. Dans cette étude, R vaut 0,68. On a donc X0(t) = -R * S0(t)."
"Au départ, la concentration d’Achromobacter sp est de 0,1 mg/L dans un milieu contenant 1 mg/L de"
"glucose. Analyser comment cette concentration évolue au fil du temps et déterminer la quantité de" 
"bactéries au bout de 10 heures."


R=0.68
rmax=0.0437
K=0.085
X0=0.1
S0=1 


def S1(t,S):
    return rmax*(S*S/(K+S) - rmax*(S/(K+S))*((X0/R)+S0))



T=[]                                               #Listes qui vont contenir les valeurs du temps, de la concentration en substrat (eau glucosée ici), de la biomasse (notamment celle au bout de 10 heures)
S=[]
X=[]
sol=[]
def eulerexplicite2(f,t0,s0,N,tf):                 #Résolution de l'ED par la méthode d'Euler 
    t=t0
    s=s0
    T.append(t)
    S.append(s)
    h= (tf-t0)/float(N)
    for i in range(N):   
        s-=h*f(t,s)
        t+=h
        if abs(t-10)<h/2:
            sol.append(s)
        S.append(s)
        T.append(t)
    return T, S

var2 = eulerexplicite2(S1,0,S0,100000,100)         #On remplit les listes T et S initiallement vides

for i in range(0,len(T)):                          #On exprime X en fonction de S grâce à la résolution de l'équation de rendement faite au préalable
    x = -R*(S[i]-S0)+X0                            
    X.append(x)
    
    
s10 = sol[0]                                       #On pose s10 est environ égale à la concentration du substrat au bout de 10 heures
x10 = -R*(s10-S0)+X0                               #On écrit la biomasse au bout de 10 heures en fonction de s10


matplotlib.pyplot.plot(T, X)                       #Graphe de la biomasse en fonction du temps
matplotlib.pyplot.xlabel('Temps')
matplotlib.pyplot.ylabel('Biomasse')
matplotlib.pyplot.plot(10, x10, '-ro')
matplotlib.pyplot.show()


matplotlib.pyplot.plot(T, S)                       ##Graphe de la concentration du substrat en fonction du temps
matplotlib.pyplot.xlabel('Temps')
matplotlib.pyplot.ylabel('Concentration')
matplotlib.pyplot.plot(10, s10, '-ro')
matplotlib.pyplot.show()

print("Au bout de 10 heures, on obtient une concentration de bactéries/biomasse de " + str(x10) + " mg/L. La biomasse augmente de manière logarithmique.")
print("Au bout de 10 heures, on obtient une concentration de substrat de " + str(s10) + " mg/L.")