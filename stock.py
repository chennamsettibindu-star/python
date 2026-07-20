# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 150
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

n = int(input("\nHow many different stocks do you own? "))

for i in range(n):
    stock_name = input(f"\nEnter stock {i+1} name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock_name] = quantity
    else:
        print("Stock not available in the price list!")

print("\n===== Portfolio Summary =====")

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}")

print("\nTotal Investment Value: $", total_investment)

# Save result to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("===== Portfolio Summary =====\n")
    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity
        file.write(
            f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}\n"
        )
    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nPortfolio summary saved to 'portfolio_summary.txt'")