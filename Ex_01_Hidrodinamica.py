import math

# Dados
ro = 923.0  # [kg/m^3]
u = 4.3     # [Pa.s]
t_min = 12.0  # [min]
D_pol = 2.5    # [polegadas]
V_litros = 1000.0 # [litros]

# Conversões
t_s = t_min * 60
V_m3 = V_litros/1000
D_m = D_pol * 0.0254

#Cálculos

Q = V_m3 / t_s

A = math.pi * (D_m**2) / 4.0

v = Q / A

Re = (ro * v * D_m) / u

# Resultados

print("Resultados")
print(f"(a) Velocidade do óleo (v): {v:.4f} m/s")
print(f"(b) Número de Reynolds (Re): {Re:.3f}")