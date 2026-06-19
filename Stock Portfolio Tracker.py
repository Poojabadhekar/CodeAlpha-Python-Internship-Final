stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = {}
total_value = 0

n = int(input("How many stocks do you own? "))

for i in range(n):
    stock = input("Enter stock symbol: ").upper()

    if stock not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input("Enter quantity: "))
    portfolio[stock] = quantity

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_value += value

    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")

print("\nTotal Portfolio Value = $", total_value)

with open("portfolio_report.txt", "w") as file:
    file.write("Stock Portfolio Report\n")
    file.write("----------------------\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(f"{stock}: {quantity} shares = ${value}\n")

    file.write(f"\nTotal Value = ${total_value}")

print("Report saved as portfolio_report.txt")