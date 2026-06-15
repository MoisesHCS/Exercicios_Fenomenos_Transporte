import numpy as np
import matplotlib.pyplot as plt

#Dados
h = 0.02  #m
u_max = 5.0  #m/s
mu = 0.05  #Pa.s

# Gerar dados para os gráficos
y = np.linspace(0.0001, h, 100)

# Calcular o perfil de velocidade u(y)
u = u_max * (1 - (y / h)**0.5)

# Calcular a tensão de cisalhamento tau(y)
du_dy = - (u_max / 2) * (1 / h**0.5) * (1 / y**0.5)
tau = mu * du_dy

#Gráfico de Velocidade
plt.figure(figsize=(8, 6))
plt.plot(u, y, color='blue', linewidth=2)
plt.title('Perfil de Velocidade $u(y)$')
plt.xlabel('Velocidade $u$ (m/s)')
plt.ylabel('Distância $y$ (m)')
plt.grid(True)
plt.show()

#Gráfico de Tensão de Cisalhamento
plt.figure(figsize=(8, 6))
plt.plot(tau, y, color='red', linewidth=2)
plt.title('Tensão de Cisalhamento $\\tau(y)$')
plt.xlabel('Tensão $\\tau$ (Pa)')
plt.ylabel('Distância $y$ (m)')
plt.grid(True)
plt.show()