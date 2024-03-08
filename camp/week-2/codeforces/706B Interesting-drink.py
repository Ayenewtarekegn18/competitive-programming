shops = int(input())
prices = list(map(int,input().split()))
days = int(input())
money = []
for i in range(days):
    money.append(int(input()))
count = 0
prices.sort()
for i in money:
    l = 0
    r = len(prices) - 1
    while l <= r:
        mid = (l + r) // 2
        if prices[mid]<=i:
            l = mid +1
        else:
            r = mid - 1   
    print(l)


