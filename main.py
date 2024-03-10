import heapq

def find_optimal_order(cables):
  heapq.heapify(cables)
  order = []
  total_cost = 0

  while len(cables) > 1:
    cable_1 = heapq.heappop(cables)
    cable_2 = heapq.heappop(cables)
    order.append((cable_1, cable_2))
    cost = cable_1 + cable_2
    total_cost += cost
    heapq.heappush(cables, cost)
  
  return order, total_cost

cables = [10, 20, 5, 15]
order, total = find_optimal_order(cables)
print("Оптимальний порядок об'єднання кабелів:", order)
print("Загальні витрати:", total)
