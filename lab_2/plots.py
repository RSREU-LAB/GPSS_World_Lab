# import matplotlib.pyplot as plt
# import numpy as np

# # Данные
# quantum_sizes = np.array([1, 4, 16, 64])
# avg_times = np.array([149.687, 160.406, 203.655, 282.741])

# # Создаем график с линейной осью X
# plt.figure(figsize=(10, 6))
# plt.plot(quantum_sizes, avg_times, 'o-', linewidth=2, markersize=8, color='black')

# # Добавляем подписи значений над точками
# for i, (q, t) in enumerate(zip(quantum_sizes, avg_times)):
#     plt.annotate(f'{t}', (q, t), textcoords="offset points", xytext=(-10,5), ha='center')

# # Настраиваем внешний вид графика
# plt.title('Зависимость среднего времени пребывания заявки в системе\n от величины кванта', fontsize=14)
# plt.xlabel('Величина кванта (q)', fontsize=12)
# plt.ylabel('Среднее время пребывания в системе', fontsize=12)
# plt.grid(True, linestyle='--', alpha=0.7)

# # Устанавливаем конкретные значения на оси X
# plt.xticks(quantum_sizes)

# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Данные
n_values = [3, 6, 9, 12]
smo1_util = [0.587, 0.673, 0.644, 0.634]
smo2_util = [0.856, 0.968, 0.981, 0.995]
smo3_util = [0.053, 0.065, 0.061, 0.060]

plt.figure(figsize=(10, 6))
plt.plot(n_values, smo1_util, marker='o', label='СМО1', linewidth=2, color='black')
plt.plot(n_values, smo2_util, marker='s', label='СМО2', linewidth=2, color='dimgray')
plt.plot(n_values, smo3_util, marker='^', label='СМО3', linewidth=2, color='gray')
plt.title('Загрузка системы в зависимости от количества заявок')
plt.xlabel('Количество заявок')
plt.ylabel('Коэффициент загрузки')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('plot_2_1.png', dpi=300)
plt.show()


plt.figure(figsize=(10, 6))
smo1_queue = [0.445, 0.997, 1.190, 1.152]
smo2_queue = [1.053, 3.292, 6.121, 9.155]
smo3_queue = [0.006, 0.005, 0.003, 0.005]

plt.plot(n_values, smo1_queue, marker='o', label='СМО1', linewidth=2, color='black')
plt.plot(n_values, smo2_queue, marker='s', label='СМО2', linewidth=2, color='dimgray')
plt.plot(n_values, smo3_queue, marker='^', label='СМО3', linewidth=2, color='gray')
plt.title('Средняя длина очереди в зависимости от количества заявок')
plt.xlabel('Количество заявок')
plt.ylabel('Длина очереди')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('plot_2_2.png', dpi=300)
plt.show()


plt.figure(figsize=(10, 6))
smo1_wait = [78.394, 152.372, 191.012, 183.117]
smo2_wait = [232.452, 629.477, 1209.673, 1763.893]
smo3_wait = [5.344, 4.183, 2.655, 4.382]

plt.plot(n_values, smo1_wait, marker='o', label='СМО1', linewidth=2, color='black')
plt.plot(n_values, smo2_wait, marker='s', label='СМО2', linewidth=2, color='dimgray')
plt.plot(n_values, smo3_wait, marker='^', label='СМО3', linewidth=2, color='gray')
plt.title('Среднее время ожидания в зависимости от количества заявок')
plt.xlabel('Количество заявок')
plt.ylabel('Время ожидания')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('plot_2_3.png', dpi=300)
plt.show()