import heapq

def min_cost_to_connect_cables(cables):
    # Ініціалізація мін-купи
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Об'єднуємо кабелі поки не залишиться один
    while len(cables) > 1:
        # Витягуємо два найменші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Обчислюємо витрати на з'єднання
        cost = first + second
        total_cost += cost
        
        # Поміщаємо новий кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад
cables = [4, 3, 2, 6]
result = min_cost_to_connect_cables(cables)
print("Загальні витрати на з'єднання кабелів:", result)