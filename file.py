from numpy import array, zeros
import numpy as np
import time
ti = time.time()

a = array([[2,-6,-1], 
           [-3,-1,7], 
           [-8,1,-2]],
          float)
b = array([-38,-34,-20], float)

n =len(b)
x =zeros(n, float)

print(a)
print(b)
print ("")

#Langkah Eliminasi
for k in range(n-1):
    for i in range(k+1, n):
        if a[i, k] == 0.0: continue
        konstanta = a[i, k]/a[k, k]
        for j in range(k, n):
            a[i, j] = a[i, j] - a[k, j] * konstanta
            b[i] = b[i] - b[k] * konstanta
            
            print("")
            print(konstanta)
            print(a)
            print(b)

print("")
print("Matriks segitiga atas yang terbentuk adalah: ")
print(a)
print(b)

#Langkah Substitusi
x[n-1] = b[n-1] / a[n-1, n-1]
for i in range(n-2, -1, -1):
    sum_ax = b[i]
    for j in range(i+1, n):
        sum_ax = sum_ax - a[i, j] * x[j]
    x[i] = (sum_ax)/a[i, i]
    
print("")
print("Solusi dari sistem persamaan tersebut adalah:")
print("{x,y,z} = ",x)
to = time.time()
print("durartion: ",to-ti,"seconds")
