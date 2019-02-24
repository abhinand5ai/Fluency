tests = int(input())

for _ in range(tests):
    n = int(input())
    stock_prices = list(map(int,input().strip().split()))
    print(stock_prices)
    gradient = [tomorrow-today for today,tomorrow in zip(stock_prices[:-1],stock_prices[1:])]
    day =0;
    buy = -1
    for i in range(n-1):
        if gradient<0 and buy>0:
            sell = i
            buy = -1
        if gradient>0 and buy<0:
            buy = i
            

