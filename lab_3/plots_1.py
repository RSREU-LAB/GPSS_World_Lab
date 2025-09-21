import matplotlib.pyplot as plt
import numpy as np

# Данные из имитационного моделирования
rho_sim = [0.45, 0.5, 0.81, 0.9]
w_sim = [325.366, 419.971, 1707.194, 3044.264]
u_sim = [724.546, 822.705, 2108.266, 3442.949]
l_sim = [0.369, 0.531, 3.44, 6.866]
l_max_sim = [11, 14, 35, 44]
m_sim = [0.821, 1.04, 4.248, 7.765]

# Данные из аналитического моделирования (только те, что есть в отчете)
rho_analytical = [0.45, 0.5, 0.81, 0.9]
w_analytical = [327.273, 400, 1705.263, 3600]
u_analytical = [727.273, 800, 2105.263, 4000]
l_analytical = [0.37, 0.5, 3.462, 8.1]
m_analytical = [0.82, 1, 4.272, 9]

# Настройка стиля графиков
plt.style.use('default')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

# Создание графиков
fig, axes = plt.subplots(3, 2, figsize=(15, 10))
fig.suptitle('Зависимости параметров СМО M/M/1 от коэффициента загрузки ρ', fontsize=18, weight='semibold')

# График 1: Среднее время ожидания в очереди
axes[0, 0].plot(rho_sim, w_sim, 'o-', label='Имитационное моделирование', color='black')
axes[0, 0].plot(rho_analytical, w_analytical, 's--', label='Аналитическая модель', color='dimgray')
axes[0, 0].set_xlabel('Коэффициент загрузки ρ')
axes[0, 0].set_ylabel('w_cр')
axes[0, 0].set_title('Зависимость w_cр от ρ')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# График 2: Среднее время пребывания в системе
axes[0, 1].plot(rho_sim, u_sim, 'o-', label='Имитационное моделирование', color='black')
axes[0, 1].plot(rho_analytical, u_analytical, 's--', label='Аналитическая модель', color='dimgray')
axes[0, 1].set_xlabel('Коэффициент загрузки ρ')
axes[0, 1].set_ylabel('u_cр')
axes[0, 1].set_title('Зависимость u_cр от ρ')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# График 3: Средняя длина очереди
axes[1, 0].plot(rho_sim, l_sim, 'o-', label='Имитационное моделирование', color='black')
axes[1, 0].plot(rho_analytical, l_analytical, 's--', label='Аналитическая модель', color='dimgray')
axes[1, 0].set_xlabel('Коэффициент загрузки ρ')
axes[1, 0].set_ylabel('l_cр')
axes[1, 0].set_title('Зависимость l_cр от ρ')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# График 4: Максимальная длина очереди (только имитационное моделирование)
axes[1, 1].plot(rho_sim, l_max_sim, 'o-', label='Имитационное моделирование', color='black')
axes[1, 1].set_xlabel('Коэффициент загрузки ρ')
axes[1, 1].set_ylabel('l_max')
axes[1, 1].set_title('Зависимость l_max от ρ')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

# График 5: Среднее число заявок в системе
axes[2, 0].plot(rho_sim, m_sim, 'o-', label='Имитационное моделирование', color='black')
axes[2, 0].plot(rho_analytical, m_analytical, 's--', label='Аналитическая модель', color='dimgray')
axes[2, 0].set_xlabel('Коэффициент загрузки ρ')
axes[2, 0].set_ylabel('m_cр')
axes[2, 0].set_title('Зависимость m_cр от ρ')
axes[2, 0].legend()
axes[2, 0].grid(True, alpha=0.3)

# График 6: Процентные изменения параметров при уменьшении ρ на 10%
parameters = ['w_cр', 'u_cр', 'l_cр', 'l_max', 'm_cр']
high_load_changes = [56.1, 61.2, 50.1, 79.6, 54.8]  # Для ρ=0.9→0.81
moderate_load_changes = [77.5, 88.1, 69.5, 78.6, 78.9]  # Для ρ=0.5→0.45

x = np.arange(len(parameters))
width = 0.35

axes[2, 1].bar(x - width/2, high_load_changes, width, label='Высокая нагрузка (ρ=0.9→0.81)', color='black')
axes[2, 1].bar(x + width/2, moderate_load_changes, width, label='Умеренная нагрузка (ρ=0.5→0.45)', color='dimgray')
axes[2, 1].set_xlabel('Параметры СМО')
axes[2, 1].set_ylabel('Уменьшение параметра, %')
axes[2, 1].set_title('Изменение параметров при уменьшении ρ на 10%')
axes[2, 1].set_xticks(x)
axes[2, 1].set_xticklabels(parameters)
axes[2, 1].legend()
axes[2, 1].grid(True, alpha=0.3)

# Добавляем подписи значений на столбцах
for i, v in enumerate(high_load_changes):
    axes[2, 1].text(i - width/2, v + 1, f'{v}%', ha='center')
    
for i, v in enumerate(moderate_load_changes):
    axes[2, 1].text(i + width/2, v + 1, f'{v}%', ha='center')

plt.tight_layout()
plt.savefig("MM1_plots.svg", format='svg', dpi=1200, bbox_inches='tight')
plt.show()