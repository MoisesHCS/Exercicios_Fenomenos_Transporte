import math
import matplotlib.pyplot as plt

# Dados
comprimento = 10.0      # m
diametro_tubo = 0.02    # m
diametro_fio = 0.000001 # m
delta_p = 5000          # Pa
viscosidade = 0.04      # Pa.s

# Função da velocidade
def velocidade(r):
    return (1/(16*viscosidade)) * (delta_p/comprimento) * (
        diametro_fio**2 - 4*r**2
        - ((diametro_tubo**2 - diametro_fio**2)/math.log(diametro_fio/diametro_tubo)) * math.log(2*r/diametro_fio)
    )

# Função da tensão de cisalhamento
def tensao(r):
    A = (diametro_tubo**2 - diametro_fio**2) / math.log(diametro_fio/diametro_tubo)
    return (delta_p / (16*comprimento)) * (-8*r - A/r)

# Raio onde a tensão é zero
r_zero = math.sqrt((diametro_tubo**2 - diametro_fio**2) / (8*math.log(diametro_tubo/diametro_fio)))

# Listas de pontos para o gráfico
raios = [ (diametro_fio/2 + i*(diametro_tubo/2 - diametro_fio/2)/300) for i in range(301) ]
raios_mm = [r*1000 for r in raios]   # converter para mm
tensoes = [tensao(r) for r in raios]
velocidades = [velocidade(r) for r in raios]

# Criar gráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))

#Gráfico da tensão
ax1.plot(tensoes, raios_mm, color="red")
ax1.axvline(0, color="gray", linestyle="--")
ax1.set_xlabel("Tensão de cisalhamento τ (Pa)")
ax1.set_ylabel("Raio r (mm)")
ax1.set_title("Distribuição da tensão de cisalhamento")
ax1.grid(True)

# Gráfico da velocidade

ax2.plot(velocidades, raios_mm, color="green")
ax2.set_xlabel("Velocidade V(r) (m/s)")
ax2.set_ylabel("Raio r (mm)")
ax2.set_title("Distribuição da velocidade")
ax2.grid(True)

plt.tight_layout()
plt.show()

print(f"Raio onde τ = 0: {r_zero*1000:.3f} mm")