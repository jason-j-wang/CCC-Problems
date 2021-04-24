import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n_cities, n_routes = int(input()), int(input())

network = [[-1] * (n_cities + 1) for _ in range(n_cities + 1)]
for _ in range(n_routes):
    x, y, cost = [int(data) for data in input().split()]
    network[x][y] = cost
    network[y][x] = cost

n_sellers = int(input())
prices = [float('inf')] * (n_cities + 1)

for _ in range(n_sellers):
    city, price = [int(data) for data in input().split()]
    prices[city] = price

dest = int(input())

min_price = [float('inf')] * (n_cities + 1)
min_price[dest] = 0

best_price = float('inf')
queue = [(0, dest)]
while queue:
    price, city = heappop(queue)
    best_price = min(best_price, price + prices[city])
    for adj_city in range(n_cities + 1):
        adj_price = network[city][adj_city]
        if adj_price == -1:
            continue
        if min_price[adj_city] > min_price[city] + adj_price:
            min_price[adj_city] = min_price[city] + adj_price
            heappush(queue, (min_price[adj_city], adj_city))

print(best_price)
