import matplotlib.pyplot as plt
import numpy as np

def moyenne(tab):
    return sum(tab)/len(tab)


def coef_regression(tab1, tab2):
    beta_1 = 0
    temp1 = 0
    beta_0 = 0
    temp2 = 0
    for i in range(0, len(tab1)):
        temp1 += (tab1[i]-moyenne(tab1))*(tab2[i]-moyenne(tab2))
        temp2 += (tab1[i]-moyenne(tab1))**2
    beta_1 = temp1/temp2
    beta_0 = moyenne(tab2)-beta_1*moyenne(tab1)
    return (beta_0, beta_1)

def matA(x):
    vect = np.ones(len(x))
    Atranspose = np.vstack((vect, x))
    A = np.transpose(Atranspose)
    return (A,Atranspose)
def matY(y):
    return np.matrix(y_i).transpose()
def matBeta(inv,Atranspose,Y):
    B1=np.dot(inv,Atranspose)
    B2=np.dot(B1,Y)
    return np.asarray(B2).reshape(-1)

###############################################################################
x_i = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
y_i = [43, 45, 48, 51, 55, 57, 59, 63, 66, 68]

print(f"Moyenne x_i : {moyenne(x_i)}")
print(f"Moyenne y_i : {moyenne(y_i)}")
print(f"(Beta_0,Beta_1) = {coef_regression(x_i,y_i)}")
coefs = coef_regression(x_i, y_i)
x = np.linspace(40, 100)
plt.plot(x, coefs[0]+coefs[1]*x)
plt.scatter(x_i, y_i, label="Nuage de points")
p = np.polyfit(x_i, y_i, 1)
plt.plot(x, p[1]+p[0]*x, label="Droite de régression")
plt.legend()
plt.title("Nuage de points et droite de régression")
plt.show()
A,A_transpose=matA(x_i)
Y=matY(y_i)
A_transposeA = np.dot(A_transpose, A)
inv_ATA = np.linalg.inv(A_transposeA)
beta=matBeta(inv_ATA,A_transpose,Y)
print(f"Beta : {beta}")
plt.figure()
plt.plot(x_i, y_i, 'ro', label="Nuage de point")
plt.plot(x, beta[0] + beta[1]*x, label="Droite de régression")
plt.title("Nuage de points et droite de régression")
plt.show()




