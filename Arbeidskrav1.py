#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:53:10 2026
Arbeidskrav 1
@author: meriam berraho
"""

#%% Totalkostnader elbil

#tilegner all viktig informasjon til variabler 
km = 10000
f = 5000
tfa = 8.38 * 365 #ganger med 365 fordi det er en daglig utgift
watt = 0.2 * 2.0 * km #ganger med totale km kjørt ila. året
bom = 0.1 * km #ganger også med totale km for bompris

elbil = f + tfa + watt + bom

print('Totale årlige kostnader elbil =', elbil)




#%% Totalkostnader bensinbil

#tilegner all viktig informasjon variabler her òg 

f2 = 7500
bensin = 1.0 * km
bom2 = 0.3 * km

bensinbil = f2 + tfa + bensin + bom2

print('Totale årlige kostnader bensinbil', bensinbil)

#Totalkostnader for bensinbil er på 23558.7


#%% Kostnadsdifferanse
kostnadsdifferanse = bensinbil - elbil

print('Hvor mye sparer du ved å ha elbil sammenligner med bensinbil i løpet av ett år?', kostnadsdifferanse)

#Kostnadsdifferansen er 10500 kr i året, som man sparer ved å ha elbil mot bensinbil.


