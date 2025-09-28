import math
import pandas as pd

# Среднее время обслуживания для одноканальной системы
v1 = 400


# Функция для вычисления P0
def calc_p0(rho, n):
    # Сумма членов от 0 до n
    sum_terms = 0
    for i in range(0, n + 1):
        term = (rho ** i) / math.factorial(i)
        sum_terms += term

    # Последний член формулы
    last_term = (rho ** (n + 1)) / (math.factorial(n) * (n - rho))
    return 1 / (sum_terms + last_term)


# Функция для расчёта параметров
def mmn_characteristics(n):
    # Интенсивность входного потока (
    lambd = 0.5 / v1 # Заменить для 0.9
    # Среднее время обслуживания для N-канальной системы
    vi_avg = n * v1
    # Интенсивность обслуживания одного канала
    mu = 1 / vi_avg
    # Коэффициент загрузки системы ρN
    rhoN = lambd * vi_avg
    # Коэффициент загрузки для формул
    rho = rhoN
    # Вероятность пустой системы P0
    P0 = calc_p0(rho, n)
    # Среднее время ожидания в очереди w
    w = (P0 * rho ** n) / (math.factorial(n - 1) * mu * (n - rho) ** 2)
    # Среднее время обслуживания
    v_serv = 1 / mu
    # Среднее время пребывания в системе u
    u = w + v_serv
    # Среднее число заявок в очереди l
    l = lambd * w
    # Среднее число заявок в системе m
    m = lambd * u
    return l, w, u, m, P0


# Количество каналов
N_values = [1, 2, 4, 8, 16]

# Для ρN = 0.9·N
data = []
for n in N_values:
    # Рассчёт всех характеристик
    l, w, u, m, P0 = mmn_characteristics(n)
    data.append([n, l, w, u, m])

# Создание DataFrame с результатами
result = pd.DataFrame(data, columns=["N", "lср", "wср", "uср", "mср"])

# Округление значений для удобства чтения
result["lср"] = result["lср"].round(3)
result["wср"] = result["wср"].round(3)
result["uср"] = result["uср"].round(3)
result["mср"] = result["mср"].round(3)


print(result)