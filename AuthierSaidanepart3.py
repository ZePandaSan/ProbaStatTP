import matplotlib.pyplot as plt
import numpy as np
from random import random
from math import *


def ecart_type_emp(data):
    moyenne = sum(data)/len(data)
    somme = 0
    for valeur in data:
        somme += (valeur-moyenne)**2
    return sqrt(somme/(len(data)-1))




poids = [0.499, 0.509, 0.501, 0.494, 0.498, 0.497, 0.504, 0.506,
         0.502, 0.496, 0.495, 0.493, 0.507, 0.505, 0.503, 0.491]
moyenne = sum(poids)/len(poids)
print(f"Moyenne empirique : {moyenne}")
plt.hist(poids, bins=15, density=True)
plt.title("Histogramme des fréquences")
plt.show()
et = ecart_type_emp(poids)
interval95 = 1.761
intervalC95 = [moyenne - interval95*et/sqrt(len(poids)),
        moyenne + interval95*et/sqrt(len(poids))]
print(f"Interval à 95% (confiture): {intervalC95}")

interval99 = 2.624
intervalC99 = [moyenne - interval99*et/sqrt(len(poids)),
        moyenne + interval99*et/sqrt(len(poids))]
print(f"Interval à 99% (confiture) = {intervalC99}")

poids2 = [85.06, 91.44, 87.93, 89.02, 87.28, 82.34, 86.23, 84.16, 88.56,
                90.45, 84.91, 89.90, 85.52, 86.75, 88.54, 87.90]
moyenne = sum(poids2)/len(poids2)

et = ecart_type_emp(poids2)

intervalC95 = [moyenne - interval95*et/sqrt(len(poids2)),
        moyenne + interval95*et/sqrt(len(poids2))]
print(f"Interval à 95% (avocat) = {intervalC95}")

n = 500
proba = 95/n
ecart_type = sqrt(proba*(1-proba)/n)
quantile = 2.576

intervalC99 = [proba-quantile*ecart_type/sqrt(n), proba+quantile*ecart_type/sqrt(n)]
print(f"Compagnie : Interval à 99% = {intervalC99}")

n = 100
binomiale = np.random.binomial(n, 0.5, 500)
ecart_type = sqrt(100*0.5*(1-0.5))
moyenne = sum(binomiale)/len(binomiale)

intervalC95 = [moyenne - 1.96*ecart_type/sqrt(n), moyenne + 1.96*ecart_type/sqrt(n)]
print(f"Binomiale : interval à 95% = {intervalC95}")
