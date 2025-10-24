import numpy as np
import matplotlib.pyplot as plt

print("=== EJERCICIO 1: FUNCIÓN DE DENSIDAD CONTINUA ===\n")

# 1. Encontrar el valor de k
def ejercicio_1():
    # Cálculo de k
    integral = (6**3)/3 - (0**3)/3  # ∫x²dx de 0 a 6 = x³/3|0 a 6
    k = 1/integral
    
    print(f"∫₀⁶ kx² dx = k * {integral} = 1")
    print(f"k = 1/{integral} = {k:.6f}")
    print(f"k = 1/72 = {1/72:.6f}")
    
    # Cálculo de P(1 ≤ X < 5)
    prob = (1/k) * ((5**3 - 1**3)/3) * k  # Más simple: ∫x²dx de 1 a 5 / 72
    prob_calculada = (125 - 1)/(3 * 72)  # (5³ - 1³)/(3*72)
    
    print(f"\nP(1 ≤ X < 5) = ∫₁⁵ (1/72)x² dx")
    print(f"= (1/72) * [(5³ - 1³)/3]")
    print(f"= (1/72) * [(125 - 1)/3]")
    print(f"= (1/72) * [124/3]")
    print(f"= 124/216 = {124/216:.6f}")
    print(f"= 31/54 = {31/54:.6f}")
    
    return k, prob_calculada

k, prob_1 = ejercicio_1()

print("\n" + "="*50)
print("=== EJERCICIO 2: SUMA DE DOS DADOS ===\n")

def ejercicio_2():
    # Probabilidades de cada suma
    sums = list(range(2, 13))
    probabilities = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
    
    print("Distribución de probabilidad:")
    print("Suma | Probabilidad")
    print("-" * 20)
    for s, p in zip(sums, probabilities):
        casos = min(s-1, 13-s)
        print(f"{s:2}   | {casos}/36 = {p:.4f}")
    
    # Valor esperado
    E_X = sum(s * p for s, p in zip(sums, probabilities))
    
    print(f"\nValor esperado E(X):")
    print("Método 1: E(D1) = E(D2) = (1+2+3+4+5+6)/6 = 21/6 = 3.5")
    print("E(X) = E(D1) + E(D2) = 3.5 + 3.5 = 7.0")
    print(f"Método 2: Σ[x * p(x)] = {E_X:.6f}")
    
    # Varianza
    E_X2 = sum((s**2) * p for s, p in zip(sums, probabilities))
    Var_X = E_X2 - E_X**2
    
    print(f"\nVarianza Var(X):")
    print("Método 1: Var(D1) = E(D1²) - [E(D1)]²")
    print("E(D1²) = (1+4+9+16+25+36)/6 = 91/6 ≈ 15.1667")
    print("Var(D1) = 91/6 - (21/6)² = 91/6 - 441/36 = 105/36 = 35/12 ≈ 2.9167")
    print("Var(X) = Var(D1) + Var(D2) = 35/12 + 35/12 = 35/6 ≈ 5.8333")
    print(f"Método 2: E(X²) - [E(X)]² = {E_X2:.6f} - {E_X**2:.6f} = {Var_X:.6f}")
    
    # Función de distribución acumulativa
    print(f"\nFunción de distribución acumulativa F(x):")
    acumulada = 0
    print("x  | F(x)")
    print("-" * 15)
    for s, p in zip(sums, probabilities):
        acumulada += p
        print(f"{s:2} | {acumulada:.4f} ({acumulada*36:.0f}/36)")
    
    return sums, probabilities, E_X, Var_X

sums, probs, E_X, Var_X = ejercicio_2()

# Gráficas
print("\n" + "="*50)
print("=== GRÁFICAS ===")

def graficar_resultados():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Gráfica 1: Función de densidad del ejercicio 1
    x1 = np.linspace(0, 6, 100)
    y1 = (1/72) * x1**2
    ax1.plot(x1, y1, 'b-', linewidth=2, label='f(x) = (1/72)x²')
    ax1.fill_between(x1, y1, where=(x1>=1)&(x1<5), alpha=0.3, color='red', 
                    label='P(1 ≤ X < 5)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.set_title('Ejercicio 1: Función de Densidad')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Gráfica 2: Distribución de suma de dados
    ax2.bar(sums, probs, alpha=0.7, color='green', label='p(x)')
    ax2.set_xlabel('Suma de dados')
    ax2.set_ylabel('Probabilidad')
    ax2.set_title('Ejercicio 2: Distribución de Suma de Dos Dados')
    ax2.set_xticks(sums)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# Resumen final
print("\n" + "="*50)
print("=== RESUMEN FINAL ===\n")

print("EJERCICIO 1:")
print(f"• k = 1/72 ≈ {1/72:.6f}")
print(f"• P(1 ≤ X < 5) = 31/54 ≈ {31/54:.6f}")

print("\nEJERCICIO 2:")
print(f"• E(X) = 7")
print(f"• Var(X) = 35/6 ≈ {35/6:.6f}")
print("• p(x) = min(x-1, 13-x)/36, para x = 2,...,12")

# Mostrar gráficas
try:
    graficar_resultados()
    print("\n✓ Gráficas generadas exitosamente")
except:
    print("\n⚠ No se pudieron mostrar las gráficas (posible problema con matplotlib)")

print("\n" + "="*50)
