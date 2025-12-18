def best_time_to_buy_and_sell_stock(prices):

    min_price = float(' inf ')
    max_profit = 0


    for price in prices :
        if price < min_price :
            min_price = price

        profit = price - min_price

        if profit > max_profit :
            max_profit = profit 

    return max_profit


test_case = ([7,3,24,632,425,24],  
            [45,342,6,64,23,1,345],
             [7,1,3,6,4,2,8])

for i in test_case:
    print(best_time_to_buy_and_sell_stock(i))
      
