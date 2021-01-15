import matplotlib.pyplot as plt
import numpy as np
from random import random
from math import factorial

def binomial (n,p):
    valeur = []
    binom = []
    for i in range(100):
        binom.append(np.random.binomial(n, p))

    for i in range(100):
        valeur.append(binom.count(i))
    
    return valeur

print(f'Question 2.1 : ')
exp1 = binomial(30, 0.5)
exp2 = binomial(30, 0.7)
exp3 = binomial(50, 0.4)


plt.plot(exp1, label='B(30,0.5)')
plt.plot(exp2, label='B(30,0.7)')
plt.plot(exp3, label='B(50,0.4)')
plt.legend()
plt.title("Question 2.1 : représentation graphique de trois lois de probabilité")
plt.show()
