# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 14:45:37 2021

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


"Dans cette troisième situation expérimentale, on cherche à obtenir une estimation sans modélisation"
"rigoureuse. On suppose que l'expérience a lieu dans un réservoir de 100 m³, constamment brassé, où de"
"l’eau glucosée est injectée en continu pour remplacer l’eau polluée, à un débit de 1 L/s. Si un état" 
"d'équilibre est atteint, quelle sera la concentration de biomasse à la sortie du réservoir ?"



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
    return T, S

    

var2 = eulerexplicite2(S1,0,S0,100000,1000)    #On remplit les listes T et S qui étaient vides
for i in range(0,len(T)):                      #On exprime X en fonction de S grâce à la résolution de l'équation de rendement faite au préalable
    x = (-R*(S[i]-S0)+X0)*1000/1036            #On factorise X par la constante trouvée après factorisation en prenant en compte le rejet de l'eau sale
    X3.append(x)


def equi(count):                               #Recherche d'un temps t (= count) qui est supérieure ou égale à Téquilibre
    count =0
    for i in range(0,len(T)-1):
        if abs(S[i]-S[i+1])<=10**(-6.3) and abs(X3[i]-X3[i+1])<=10**(-6.3):
            return count         
        count += 1


equilibre = (S[equi(0)], X3[equi(0)])          #On approxime les valeurs S(Téquilibre) et X(Téquilibre)


matplotlib.pyplot.plot(T, S,'-g')              #Graphe de la concentration du substrat en fonction du temps (en vert)
matplotlib.pyplot.axhline(y=equilibre[0])      #Droite d'équation y = S(Téquilibre)

matplotlib.pyplot.plot(T, X3,'-r')             #Graphe de la biomasse en fonction du temps (en rouge)
matplotlib.pyplot.axhline(y=equilibre[1])      #Droite d'équation y = X(Téquilibre)


matplotlib.pyplot.show()

print("En cas d'équilibre, la biomasse en sortie de réservoir est d'environ: " 
      + str(X3[equi(0)]) + " mg/L.")



