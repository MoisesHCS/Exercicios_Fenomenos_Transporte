# Dados
ro = 1.2      # [kg/m^3]
A1 = 0.2      # [m^2]
A2 = 0.04     # [m^2]
v2 = 60       # [m/s]


# Equação da Continuidade
v1 = (A2 / A1) * v2

# Equação de Bernoulli
# P1 - P2 = 0.5 * rho * (v2^2 - v1^2) P2man = P2abs - P2atm
#P2abs = P2atm  P2man = 0
P1man = (0.5 * ro * (v2**2 - v1**2))/1000

# Resultados

print("Resultado")
print(f"P1man : {P1man:.4f} kPa")