import math

# Dados do Problema

Q = 600       # Taxa de calor (W)
x_mm = 5      # Espessura (mm)
D_mm = 200    # Diâmetro (mm)
T2 = 110      # Temperatura da superfície interna (C)

# Cálculos

x_m = x_mm / 1000
D_m = D_mm / 1000

# Cálculo da Área (A = pi * D^2 / 4)
A = math.pi * (D_m ** 2) / 4

# Alumínio
k_Al = 240     # Condutividade do Alumínio (W/m.K)

# Cálculo da variação da T para o alumínio (delta T)
dT_Al = (Q * x_m) / (k_Al * A)

# Cálculo de T1 (T1 = T2 + dT)
T1_Al = T2 + dT_Al

# Cobre
k_Cu = 390     # Condutividade do Cobre (W/m.K)

# Cálculo da variação da T para o cobre (delta T)
dT_Cu = (Q * x_m) / (k_Cu * A)

# Cálculo de T1
T1_Cu = T2 + dT_Cu

# Resultados

print(f"Superfície do Fogão:")
print(f"Área da Base (A): {A:.6f} m²")
print(f"Espessura (x): {x_m} m")
print("-" * 55)

print(f"1. Alumínio (k = {k_Al:.0f} W/m.K)")
print(f"   Variação de Temperatura (dT_Al): {dT_Al:.2f} °C")
print(f"   Temperatura da Superfície (T1_Al): {T1_Al:.2f} °C")
print("-" * 55)

print(f"2. Cobre (k = {k_Cu:.0f} W/m.K)")
print(f"   Variação de Temperatura (dT_Cu): {dT_Cu:.2f} °C")
print(f"   Temperatura da Superfície (T1_Cu): {T1_Cu:.2f} °C")