# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 00:46:47 2020

@author: Milan
"""
# a)
Textfile = 'viscosity_of_gases.dat' # Name des gelesenen Files
infile = open(Textfile,'r') # oeffnen den File
rows = infile.readlines() # Reihen ablesen
mu_data = {} # Das verschachteltes Dictionary in das die Namen der Parameter als Keys
# und Werte als Values hinzugefuegt werden  
for row in rows: #  Zaehlen jede Reihe
    
    name = str(row[:17]) # Der Name des Gases in jeder Reihe ist unterschiedlich gross, deswegen 
    # wird der letzte Element des groessten Names (zusammen mit seiner Separation) berucksichtigt. Deswegen 16, wo 17 nicht zaehlt.
    name = name.strip() # Abschneiden der leeren Stellen
    row = row.split() # Separation der Spalten Elementen
    
    if row!= []: # Wenn es um keine leere Reihe geht
        
        
        if row[0]!='#': # Wenn es mit keinem '#' anfaengt, sonst ist es ein unnotwendiger Komentar.
        
            value_2 = float(row[-1]) # der letzte Wert
            value_1 = float(row[-2]) # der vorletzte Wert
            value_0 = float(row[-3]) # der vorvorletzte Wert
            # Name ist key des verschachtelten mu_data dictionary (Art des Gases) und 
            # 'C', 'T_0' und 'mu_0' sind die keys (Namen der Parameter) und value_0, value_1 und value_2 sind die values (Parameter).
            mu_data[name]= {'C':value_0,'T_0':value_1,'mu_0':value_2}
    
        
#b)
def mu(T,gas,mu_data): # berechnet den Wert der Formel
    
    mu_0 = mu_data[gas]['mu_0'] # mu_0 Konstante aus dem mu_data Dictionary
    T_0 = mu_data[gas]['T_0'] # T_0 Konstante aus dem mu_data Dictionary
    C = mu_data[gas]['C'] # C Konstante aus dem mu_data Dictionary
    
    mu = mu_0*(T_0 - C)/(T + C)*(T/T_0)**1.5 # Die Formel
    
    return mu # Die ausgegebene Menge

#c)
    
import numpy as np  
import matplotlib.pyplot as plt

T = np.linspace(273,373,1000) # Die numpy array von 1000 Temperatur Komponenten 
# im [273,373] Intervall.

mu_T_air = mu(T,'air',mu_data) # Luft mu_T
mu_T_CO2 = mu(T,'carbon dioxide',mu_data) # Kohlenstoffdioxid mu_T
mu_T_H2 = mu(T,'hydrogen',mu_data) # Wasserstoff mu_T
plt.plot(T,mu_T_air,T,mu_T_CO2,T,mu_T_H2) # Der Plot als Funktion von T
label = ['air','carbon dioxide','hydrogen'] # Die Namen in der Legende
plt.legend(label,shadow=True,fontsize=9) # Die legende mit dem Schatten und Buchstabegroesse 9
#plt.xlim(273,373)
plt.title('mu als Funktion von T') # Der Title





