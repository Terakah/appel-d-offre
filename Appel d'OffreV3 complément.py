# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 20:10:39 2021

@author: TeRaKa
"""

import numpy
import math
import matplotlib



R=0.68
rmax=0.0437
K=0.085
X0=0.1
S0=1 


def S1(t,S):                                                    #Définition de l'équation de Monod (ED)
    return rmax*(S*S/(K+S) - rmax*(S/(K+S))*((X0/R)+S0))



T=[]                                            #Listes qui vont contenir les valeurs du temps, de la concentration en substrat (eau glucosée ici) et de la biomasse
S=[]
X3=[]



def eulerexplicite2(f,t0,s0,N,tf):              #Résolution de l'ED par la méthode d'Euler
    t=t0
    s=s0
    T.append(t)
    S.append(s)
    h= (tf-t0)/float(N)
    for i in range(N):   
        s-=h*f(t,s)
        t+=h
        S.append(s)
        T.append(t)
    for j in range(N):
        S[j] += h*S0*36/1000                     #Une fois résolue, on additionne par l'apport en eau glucosée par heure (ici on multiplie par h car c'est le pas)
    for k in range(N):
        S[k] *= numpy.random.sample()
    return T, S

    

var2 = eulerexplicite2(S1,0,S0,100000,1000)    #On remplit les listes T et S qui étaient vides
for i in range(0,len(T)):                      #On exprime X en fonction de S grâce à la résolution de l'équation de rendement faite au préalable
    z = numpy.random.sample()
    x = (-R*(S[i]-S0)+X0)*(1-z)            #On factorise X par la constante trouvée après factorisation en prenant en compte le rejet de l'eau sale
    X3.append(x)





matplotlib.pyplot.plot(T, S,'-g')              #Graphe de la concentration du substrat en fonction du temps (en vert)

matplotlib.pyplot.plot(T, X3,'-r')             #Graphe de la biomasse en fonction du temps (en rouge)


matplotlib.pyplot.show()

