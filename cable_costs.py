import heapq

def minimize_cable_costs(cable_lengths):
    heapq.heapify(cable_lengths)

    total_cost = 0

    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        combined = first + second
        heapq.heappush(cable_lengths, combined)
        total_cost += combined

    return total_cost

cable_lengths = [5, 2, 4, 8, 6, 7]
print("Мінімальні витрати на з'єднання кабелів:", minimize_cable_costs(cable_lengths))