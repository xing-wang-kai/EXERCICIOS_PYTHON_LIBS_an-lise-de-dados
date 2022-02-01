import matplotlib.pyplot as plt

from matplotlib import pyplot as plt
import numpy as np

#%matplotlib inline

import random

dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)

print(dados1)
print(dados2)

plt.plot(dados1, dados2)

print(plt.plot(dados1, dados2))

fig, ax = plt.subplots(1,2, figsize=(12, 5))

x = range(5)

print(np.array(x))
print(fig)
x = np.array(x)

print(x**3)

print("Tipo de ax = ", type(ax))
print("Conteúdo de ax[0] = ", ax[0])
print("Conteúdo de ax[1] = ", ax[1])

ax[0].plot(x, x, label='eq_1') # cria gráfico sobre eixo 0
ax[0].plot(x, x**2, label='eq_2') # cria gráfico sobre eixo 0
ax[0].plot(x, x**3, label='eq_3') # cria gráfico sobre eixo 0
ax[0].set_xlabel('Eixo x') #nomeia o gráfico para o eixo x
ax[0].set_ylabel('Eixo y') # nomeia o gráfico para o eixo y
ax[0].set_title("Gráfico 1") # titulo para o gráfico
ax[0].legend()