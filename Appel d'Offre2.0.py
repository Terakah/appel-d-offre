# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:28:27 2021

@author: TeRaKa
"""

import numpy
import math
import matplotlib


"On fait l'hypothèse que la concentration en substrat reste constante tout au long de l’expérience."
"Le milieu contient 1 mg/L de glucose, et la concentration initiale d’Achromobacter sp est de 0,1 mg/L."
"À quel moment la biomasse atteindra-t-elle 1 g/L ?"


R=0.68
rmax=0.0437
K=0.085
X0=0.1
S0=1 

def X2(t):                                          #Fonction trouvée en résolvant l'équation de Monod (en posant pour tout t, S(t)=S0 constant)
    return X0*math.exp(t*(rmax*S0)/(K+S0))



def solution(f,n):                                  #Création des listes X(t) et T tel que pour tout t, on a environ X(t) <= 1g/L (= 1000mg/L)                 
    X=[]
    T=[]
    x=0
    t=0
    h=1/float(n)
    while x<1000+h:
        X.append(x)
        T.append(t)
        x = f(t)
        t+=h
    return T,X,t,f(t)
    
Tlist,Xlist,t1000,x1000 = solution(X2,10000)        #On fixe les variables et les listes pour tracer les graphes           

 
matplotlib.pyplot.plot(Tlist, Xlist)                #Graphe de la biomasse en fonction du temps et tel qu'on a environ X(t)<= 1g/L
matplotlib.pyplot.plot(t1000, x1000, '-ro')         #Point où la biomasse est environ égale à 1g/L

matplotlib.pyplot.xlabel('Temps')
matplotlib.pyplot.ylabel('Biomasse')
matplotlib.pyplot.show()


print("La biomasse atteint " + str(x1000) + " mg/L (donc environ 1g/L) après " + str(t1000) + " heures.")






