stock_price = [10000,12200,13000,14000,15000,16000,17000]

def get_max_profit(stock_price):
    max_profit = 0
    min_price = float('inf')
    for price in stock_price:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit
def get_which_day_to_buy(stock_price):
    return stock_price.index(min(stock_price)),min((stock_price))
days = {0 : "Monday", 1 : "Tuesday", 2 : "Wednesday", 3 : "Thursday", 4 : "Friday", 5 : "Saturday", 6 : "Sunday"}

def main():
    print("Calculating max profit...")
    print(get_max_profit(stock_price))
    print(get_which_day_to_buy(stock_price))
    print(days[get_which_day_to_buy(stock_price)[0]])


if __name__ == "__main__":
    main()