# Dados do Problema

k1 = 0.75  #  W/m.K
k2 = 0.25  #  W/m.K
x2_mm = 100  # Espessura da Parede 2 em mm
p = 0.80

#Cálculos

x2_m = x2_mm / 1000

x1_m = (k1 * x2_m) / (p * k2)

x1_mm = x1_m * 1000

# Resultados

print(f"Cálculo da Espessura da Parede")
print(f"Condutividade (k1): {k1} W/m.K")
print(f"Espessura conhecida (x2): {x2_mm} mm")
print(f"Relação Q1/Q2: {p}")
print("-" * 40)
print(f"Espessura da Parede (x1): {x1_mm:.2f} mm")
print(f"Espessura da Parede (x1): {x1_m:.3f} m")