import matplotlib.pyplot as plt

# Количество каналов
N = [1, 2, 3, 4]

# Экспериментальные данные
l_exp = [8.411, 0.235, 0.031, 0.004]
w_exp = [3732.386, 103.95, 13.591, 1.931]
u_exp = [4131.004, 503.431, 413.203, 401.526]
m_exp = [9.294, 1.132, 0.929, 0.903]

# Теоретические данные
l_th = [7.923, 0.238, 0.035, 0.004]
w_th = [3521.5, 106.1, 14.03, 1.945]
u_th = [3920.611, 506.98, 415.363, 403.278]
m_th = [8.821, 1.140, 0.938, 0.907]

# Создаём фигуру и подграфики
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Сравнение экспериментальных и теоретических данных СМО (1–4 канала)", fontsize=16)

# l̄
axs[0, 0].plot(N, l_exp, 'o-', label='Экспериментальное')
axs[0, 0].plot(N, l_th, 's--', label='Теоретическое')
axs[0, 0].set_title("Среднее число заявок в очереди (l̄)")
axs[0, 0].set_xlabel("N")
axs[0, 0].set_ylabel("l̄")
axs[0, 0].legend()
axs[0, 0].grid(True)

# w̄
axs[0, 1].plot(N, w_exp, 'o-', label='Экспериментальное')
axs[0, 1].plot(N, w_th, 's--', label='Теоретическое')
axs[0, 1].set_title("Среднее время ожидания в очереди (w̄)")
axs[0, 1].set_xlabel("N")
axs[0, 1].set_ylabel("w̄")
axs[0, 1].legend()
axs[0, 1].grid(True)

# ū
axs[1, 0].plot(N, u_exp, 'o-', label='Экспериментальное')
axs[1, 0].plot(N, u_th, 's--', label='Теоретическое')
axs[1, 0].set_title("Среднее время пребывания в системе (ū)")
axs[1, 0].set_xlabel("N")
axs[1, 0].set_ylabel("ū")
axs[1, 0].legend()
axs[1, 0].grid(True)

# m̄
axs[1, 1].plot(N, m_exp, 'o-', label='Экспериментальное')
axs[1, 1].plot(N, m_th, 's--', label='Теоретическое')
axs[1, 1].set_title("Среднее число заявок в системе (m̄)")
axs[1, 1].set_xlabel("N")
axs[1, 1].set_ylabel("m̄")
axs[1, 1].legend()
axs[1, 1].grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
