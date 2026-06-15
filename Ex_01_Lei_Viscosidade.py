import matplotlib.pyplot as plt

# Dados

# Viscosidades (N.s/m²)
mu1, mu2, mu3 = 0.15, 0.5, 0.2

# Espessuras (m)
h1, h2, h3   = 0.0005, 0.00025, 0.0002

# força (N), área (m²)
F, A = 100.0, 1.0

# Tensão de cisalhamento
tau = F / A

# Queda de velocidade em cada camada
du1 = tau * h1 / mu1
du2 = tau * h2 / mu2
du3 = tau * h3 / mu3

# Velocidades acumuladas
u12 = du1
u23 = du1 + du2
V   = du1 + du2 + du3

# Resultados
print("Velocidade da placa superior V =", round(V, 5), "m/s")
print("Velocidade na interface µ1-µ2 =", round(u12, 5), "m/s")
print("Velocidade na interface µ2-µ3 =", round(u23, 5), "m/s")

# Gráfico do perfil de velocidade

# Alturas acumuladas
y0 = 0
y1 = h1
y2 = h1 + h2
y3 = h1 + h2 + h3

# Plotando o gráfico
plt.plot([0, u12], [y0, y1], 'r-', linewidth=2, label='Camada μ1')
plt.plot([u12, u23], [y1, y2], 'g-', linewidth=2, label='Camada μ2')
plt.plot([u23, V], [y2, y3], 'b-', linewidth=2, label='Camada μ3')

plt.xlabel("Velocidade (m/s)")
plt.ylabel("Altura (m)")
plt.title("Perfil de velocidade em 3 camadas")
plt.legend()
plt.grid(True)
plt.show()
