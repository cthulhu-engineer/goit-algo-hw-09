import time

from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins

amount = 11236744

print(f"Сума, яку необхідно зібрати: {amount}")

# Жадібний алгоритм
start_time = time.time()
greedy_result = find_coins_greedy(amount)
end_time = time.time()
print(f"Жадібний алгоритм: {greedy_result}")
print(f"Час виконання: {end_time - start_time} секунд")

# Алгоритм динамічного програмування
start_time = time.time()
dp_result = find_min_coins(amount)
end_time = time.time()
print(f"Алгоритм динамічного програмування: {dp_result}")
print(f"Час виконання: {end_time - start_time} секунд")
