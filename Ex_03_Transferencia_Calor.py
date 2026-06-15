# Dados do Problema

k = 0.6              # (kcal/h.m.°C)
x_cm = 25            # (cm)
T_int = 20           # (°C)
T_ext = -20          # (°C)
Area_total = 1000    # (m²)
tempo_h = 10         # (h)
PC_carvao = 5500     # (kcal/Kg)
rendimento = 0.5     # (50%)

# Cálculos

x_m = x_cm / 100

dT = T_int - T_ext

Q_inicial = (k * dT) / x_m

Q_perda = Q_inicial * Area_total * tempo_h

Q_forn = Q_perda / rendimento

m_carvao = Q_forn / PC_carvao

# Resultados

print(f"(a) Perda de Calor por m² por Hora")
print(f"Q': {Q_inicial:.2f} kcal/h.m²")
print("-" * 30)

print(f"(b) Quantidade de Carvão Utilizada")
print(f"Perda Total de Calor em 10h (Q_perda): {Q_perda:,.0f} kcal")
print(f"Energia Fornecida Necessária (Q_forn): {Q_forn:,.0f} kcal (Rendimento de {rendimento*100:.0f}%)")
print(f"Massa de Carvão Utilizada (m): {m_carvao:.2f} Kg")