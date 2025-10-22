import numpy as np


# Данные из вашего моделирования (транспортные средства : средняя длина очереди)
vehicles = [5, 10, 15, 20, 25, 50, 75, 100, 200, 500, 1000]
queue_lengths = [0.025, 2.898, 4.425, 6.715, 8.273, 14.055, 22.264, 34.889, 72.518, 173.754, 340.531]
times = [3270.253, 7750.597, 11409.755, 16484.959, 20550.939, 38243.384, 58779.862, 80634.816, 159836.394, 396800.786, 788349.781]


# Расчет скорости нарастания очереди
def calculate_growth_rate(vehicles, queue_lengths):
    # Используем линейную регрессию для определения скорости роста
    x = np.array(vehicles)
    y = np.array(queue_lengths)
    
    # Линейная регрессия: y = a + b * x
    A = np.vstack([x, np.ones(len(x))]).T
    b, a = np.linalg.lstsq(A, y, rcond=None)[0]
    
    print(f"\nQUEUE GROWTH RATE:")
    print(f"    Linear model: queue length = {a:.3f} + {b:.3f} x vehicles")
    print(f"    Growth rate: {b:.3f} queue unit / 1 vehicle")
    print(f"    Growth rate: {b/444:.6f} queue unit / time unit")  # Tи = 444
    
    return a, b

a, b = calculate_growth_rate(vehicles, queue_lengths)