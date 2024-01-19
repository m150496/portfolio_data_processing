# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:27:18 2020

@author: Milan
"""

#Milan Cukovic
#01531871
m_e = 9.1094 * 10**-31 # Die Elektronenmasse in kg
e=1.6022 * 10**-19     # Elementarladung in C
eps_0 = 8.8542 * 10**-12 # die Dielektrizitaetskonstante in C^2s^2kg^-1m^-3
h = 6.6261 * 10**-34    # das Planck'sche Wirkungsquantum in Js
c = 2.99792 * 10**8     # Lichtgeschwindigkeit in m/s
n_f_L=1                 # Lyman Anfangswert
n_f_B=2                 # Balmer Anfangswert
n_i_L=n_f_L             # Lyman Anfangswert (for schleife)
n_i_B=n_f_B             # Balmer Anfangswert (for Schleife)
J=6.24150913 * 10**18   # eV in J
eV=1.60217662 * 10**-19 # J in eV
nm=10**-9               # m in nm
m=10**9                 # nm in m

Lyman = [[],[]]
Balmer = [[],[]]
    
print("Lyman:") # Titel der Tabelle
print("nf ni E(eV) lambda(nm)") #Bezeichnungen der Tabelle
for i in range(0,5):

    n_i_L+=1
    v=-(((m_e*e**4)/(8*(eps_0)**2*h**2))*(1/n_i_L**2-1/n_f_L**2))/h # in Hz
    Lyman[1].append((c/v) * m) #Wellenlaenge
    Lyman[0].append(v*h * J) #Energie in ElectronVolt

    print('%d  %d %.2f  %.1f' %(n_f_L,n_i_L, Lyman[0][i], Lyman[1][i])) #die berechneten Werte

print("Balmer:") # Titel der Tabelle
print("nf ni E(eV) lambda(nm)") #Bezeichnungen der Tabelle  
for i in range(0,5):
    
    n_i_B+=1
    v=-(((m_e*e**4)/(8*(eps_0)**2*h**2))*(1/n_i_B**2-1/n_f_B**2))/h # in Hz
    Balmer[1].append((c/v) * m) #Wellenlaenge
    Balmer[0].append(v*h * J) #Energie in ElectronVolt
    
    print('%d  %d %.2f  %.1f' %(n_f_B,n_i_B, Balmer[0][i], Balmer[1][i])) #die berechneten Werte
    
        
        
        