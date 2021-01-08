import numpy as np
import math
import matplotlib.pyplot as plt

def GeraMatriz():
	matriz = np.random.uniform(-10,10,(100,2))
	return matriz

def GeraAptidao(a):
	b = np.array([])
	for i in a:
		f = 0.5 - (math.sin(math.sqrt(i[0]**2+i[1]**2))**2-0.5)/((1+0.001*(i[0]**2+i[1]**2))**2)
		b = np.append (b,f)
	return b

def soma(b):
	c = np.array([])
	aux = 0;
	j = 0;
	for i in b:
		aux = aux+i
		c = np.append(c,aux)
	return c

def casais(matrizFinal):
	aux = matrizFinal[:,3]
	casal = []
	for i in range(100):
		r = np.random.uniform(0,np.amax(aux))
		for index, value in enumerate(aux):
			if r < value:
				casal.append(index)
				break;		
	return casal	

def GeraFilhos(vetor,matriz):
	filhos = np.empty((100,2))
	tamanho = len(vetor)
	i=0
	while(i < tamanho):
		rand = np.random.randint(0, 2)
		if (rand == 0):
			 filhos[i,0] = matriz[vetor[i],0]
			 filhos[i,1] = matriz[vetor[i],1]
			 filhos[i+1,0] = matriz[vetor[i+1],0]
			 filhos[i+1,1] = matriz[vetor[i+1],1]
		else:
			 alfa =  np.random.uniform(0,1)
			 filhos[i,0] = alfa*matriz[vetor[i],0] + (1-alfa)*matriz[vetor[i+1],0]
			 filhos[i,1] = alfa*matriz[vetor[i],1] + (1-alfa)*matriz[vetor[i+1],1] 
			 filhos[i+1,0] = alfa*matriz[vetor[i+1],0] + (1-alfa)*matriz[vetor[i],0]
			 filhos[i+1,1] = alfa*matriz[vetor[i+1],1] + (1-alfa)*matriz[vetor[i],1]
		i+=2
	return filhos



init = GeraMatriz()
f = []
for i in range(100):
	b = GeraAptidao(init)
	c = np.c_[init, b]
	d = soma(b)
	matrizFinal = np.c_[c, d]
	casal = casais(matrizFinal)
	filhos = GeraFilhos(casal,matrizFinal)
	init = filhos
	x = b**2
	f.append(np.sum(x))
	print(f[i])

plt.plot( list(range(0, 100)), f)

plt.show()