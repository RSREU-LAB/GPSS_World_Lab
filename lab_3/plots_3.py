import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
v_cp = 400  # среднее время обслуживания
rho = 0.9   # коэффициент загрузки
lambda_val = rho / v_cp  # интенсивность входного потока

# Задаем диапазон значений σ от 0 до 400
sigma_values = np.linspace(0, 400, 100)

# Рассчитываем γ для каждого σ
gamma_values = sigma_values / v_cp

# По формуле Поллячека-Хинчина рассчитываем w_cp
w_cp_theor = (lambda_val * v_cp**2 * (1 + gamma_values**2)) / (2 * (1 - rho))

# Рассчитываем остальные параметры
u_cp_theor = w_cp_theor + v_cp
l_cp_theor = lambda_val * w_cp_theor
m_cp_theor = l_cp_theor + rho

# Значения σ для конкретных моделей
sigma_specific = {
    'M/D/1': 0,
    'M/Нормальное/1': 133.333,
    'M/U/1': 230.94,
    'M/M/1': 400
}

# Экспериментальные значения из ваших данных
experimental_data = {
    'M/D/1': {'w': 1844.487, 'u': 2244.447, 'l': 4.158, 'm': 5.058},
    'M/Нормальное/1': {'w': 1855.545, 'u': 2253.525, 'l': 4.181, 'm': 5.078},
    'M/U/1': {'w': 2117.229, 'u': 2516.068, 'l': 4.709, 'm': 5.595},
    'M/M/1': {'w': 3044.264, 'u': 3442.949, 'l': 6.866, 'm': 7.765}
}

# Создаем графики
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# График 1: w_cp от σ
ax1.plot(sigma_values, w_cp_theor, '-', label='Теоретическая кривая', color='black')
for model, sigma in sigma_specific.items():
    ax1.plot(sigma, experimental_data[model]['w'], 'o', markersize=6, color='dimgray')
    ax1.annotate(model, (sigma, experimental_data[model]['w']), 
                xytext=(5, 5), textcoords='offset points')
ax1.set_xlabel('СКО (σ) длительности обслуживания')
ax1.set_ylabel('w_cр')
ax1.grid(True)
ax1.legend()

# График 2: u_cp от σ
ax2.plot(sigma_values, u_cp_theor, '-', label='Теоретическая кривая', color='black')
for model, sigma in sigma_specific.items():
    ax2.plot(sigma, experimental_data[model]['u'], 'o', markersize=6, color='dimgray')
    ax2.annotate(model, (sigma, experimental_data[model]['u']), 
                xytext=(5, 5), textcoords='offset points')
ax2.set_xlabel('СКО (σ) длительности обслуживания')
ax2.set_ylabel('u_cр')
ax2.grid(True)
ax2.legend()

# График 3: l_cp от σ
ax3.plot(sigma_values, l_cp_theor, '-', label='Теоретическая кривая', color='black')
for model, sigma in sigma_specific.items():
    ax3.plot(sigma, experimental_data[model]['l'], 'o', markersize=6, color='dimgray')
    ax3.annotate(model, (sigma, experimental_data[model]['l']), 
                xytext=(5, 5), textcoords='offset points')
ax3.set_xlabel('СКО (σ) длительности обслуживания')
ax3.set_ylabel('l_cр')
ax3.grid(True)
ax3.legend()

# График 4: m_cp от σ
ax4.plot(sigma_values, m_cp_theor, '-', label='Теоретическая кривая', color='black')
for model, sigma in sigma_specific.items():
    ax4.plot(sigma, experimental_data[model]['m'], 'o', markersize=6, color='dimgray')
    ax4.annotate(model, (sigma, experimental_data[model]['m']), 
                xytext=(5, 5), textcoords='offset points')
ax4.set_xlabel('СКО (σ) длительности обслуживания')
ax4.set_ylabel('m_cр')
ax4.grid(True)
ax4.legend()

plt.tight_layout()
plt.savefig("plots_task15.svg", format='svg', dpi=1200, bbox_inches='tight')
plt.show()

# Расчет теоретических значений для конкретных σ
def calculate_theoretical(sigma, v_cp=400, rho=0.9):
    lambda_val = rho / v_cp
    gamma = sigma / v_cp
    w_cp = (lambda_val * v_cp**2 * (1 + gamma**2)) / (2 * (1 - rho))
    u_cp = w_cp + v_cp
    l_cp = lambda_val * w_cp
    m_cp = l_cp + rho
    return w_cp, u_cp, l_cp, m_cp

# Относительные отклонения в процентах
deviations = {}
for model, sigma in sigma_specific.items():
    w_th, u_th, l_th, m_th = calculate_theoretical(sigma)
    w_exp = experimental_data[model]['w']
    u_exp = experimental_data[model]['u']
    l_exp = experimental_data[model]['l']
    m_exp = experimental_data[model]['m']
    
    deviations[model] = {
        'w': abs(w_th - w_exp) / w_th * 100,
        'u': abs(u_th - u_exp) / u_th * 100,
        'l': abs(l_th - l_exp) / l_th * 100,
        'm': abs(m_th - m_exp) / m_th * 100
    }

print("Относительные отклонения экспериментальных данных от теоретических (%):")
for model in deviations:
    print(f"{model}: w_cp={deviations[model]['w']:.2f}%, u_cp={deviations[model]['u']:.2f}%, l_cp={deviations[model]['l']:.2f}%, m_cp={deviations[model]['m']:.2f}%")