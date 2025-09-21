import matplotlib.pyplot as plt
import numpy as np


# СКО для каждого типа распределения
sigma_mm = 400  # M/M/1
sigma_mu = 230.94  # M/U/1
sigma_norm = 133.333  # M/Нормальное/1
sigma_md = 0  # M/D/1

sigma_values = [sigma_md, sigma_norm, sigma_mu, sigma_mm]

# Среднее время ожидания
w_cp_values = [1844.487, 1855.545, 2117.229, 3044.264]

# Среднее время пребывания в системе
u_cp_values = [2244.447, 2253.525, 2516.068, 3442.949]

# Средняя длина очереди
l_cp_values = [4.158, 4.181, 4.709, 6.866]

# Среднее число заявок в системе
m_cp_values = [5.058, 5.078, 5.595, 7.765]

# Создаем графики
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

# График зависимости w_cp от σ
ax1.plot(sigma_values, w_cp_values, 'o-', linewidth=2, markersize=8, color='gray')
ax1.set_xlabel('СКО (σ) длительности обслуживания')
ax1.set_ylabel('w_cp')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_title('Зависимость w_cp от σ')

# График зависимости u_cp от σ
ax2.plot(sigma_values, u_cp_values, 's-', linewidth=2, markersize=8, color='gray')
ax2.set_xlabel('СКО (σ) длительности обслуживания')
ax2.set_ylabel('u_cp')
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_title('Зависимость u_cp от σ')

# График зависимости l_cp от σ
ax3.plot(sigma_values, l_cp_values, 'X-', linewidth=2, markersize=8, color='gray')
ax3.set_xlabel('СКО (σ) длительности обслуживания')
ax3.set_ylabel('l_cp')
ax3.grid(True, linestyle='--', alpha=0.7)
ax3.set_title('Зависимость l_cp от σ')

# График зависимости m_cp от σ
ax4.plot(sigma_values, m_cp_values, 'd-', linewidth=2, markersize=8, color='gray')
ax4.set_xlabel('СКО (σ) длительности обслуживания')
ax4.set_ylabel('m_cp')
ax4.grid(True, linestyle='--', alpha=0.7)
ax4.set_title('Зависимость m_cp от σ')

# Подписи точек
labels = ['M/D/1', 'M/Нормальное/1', 'M/U/1', 'M/M/1']
for i, label in enumerate(labels):
    ax1.annotate(label, (sigma_values[i], w_cp_values[i]), textcoords="offset points", xytext=(0,10), ha='center')
    ax2.annotate(label, (sigma_values[i], u_cp_values[i]), textcoords="offset points", xytext=(0,10), ha='center')
    ax3.annotate(label, (sigma_values[i], l_cp_values[i]), textcoords="offset points", xytext=(0,10), ha='center')
    ax4.annotate(label, (sigma_values[i], m_cp_values[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.savefig("plots_task14.svg", format='svg', dpi=1200, bbox_inches='tight')
plt.show()