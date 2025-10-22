import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
NTri = [5, 10, 15, 20, 25, 50, 75, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
SAVi = [0, 2.898, 4.425, 6.715, 8.273, 14.055, 22.264, 34.889, 72.518, 173.754, 340.531, 695.563, 1819.014, 3768.104, 7741.229]

# Линейная интерполяция только между существующими точками
interpolated_SAVi = np.interp(NTri, NTri, SAVi)

# Построение графика с ПРЯМЫМИ линиями между точками
plt.figure(figsize=(12, 8))

# Рисуем прямые линии между точками (без сглаживания)
plt.plot(NTri, SAVi, 'b-', linewidth=2, label='Линейная интерполяция')
plt.plot(NTri, SAVi, 'ro', markersize=6, label='Исходные данные')

# Настройки графика
plt.xscale('log')
plt.yscale('linear')
plt.xlabel('NTri', fontsize=12)
plt.ylabel('SAVi', fontsize=12)
plt.title('Линейная интерполяция SAVi', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()

# Подписываем некоторые ключевые точки
for i, (n, s) in enumerate(zip(NTri, SAVi)):
    if n in [5, 100, 1000, 10000, 20000]:
        plt.annotate(f'({n}, {s:.1f})', (n, s), 
                    textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

plt.tight_layout()
# plt.savefig('linear_interpolation_SAVi.svg', format='svg', dpi=1200)
plt.show()