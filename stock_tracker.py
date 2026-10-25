# CodeAlpha Internship - Task 2

# Stock Portfolio Tracker

stock_prices = {
"AAPL": 180,
"TSLA": 250,
"GOOGL": 140,
"MSFT": 420,
"AMZN": 190
}

portfolio = {}

print("=" * 40)
print("     STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
print(f"{stock}: ${price} per share")

print("\nEnter stock symbols and quantities.")
print("Type 'done' when finished.\n")

while True:
stock_name = input("Enter stock symbol: ").strip().upper()

```
if stock_name == "DONE":
    break

if stock_name not in stock_prices:
    print("Invalid stock symbol. Choose from the list.")
    continue

try:
    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        continue

except ValueError:
    print("Please enter a valid whole number.")
    continue

portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
```

print("\n" + "=" * 40)
print("       INVESTMENT SUMMARY")
print("=" * 40)

total_investment = 0

for stock, quantity in portfolio.items():
price = stock_prices[stock]
investment = price * quantity
total_investment += investment

```
print(f"{stock}: {quantity} shares x ${price} = ${investment}")
```

if not portfolio:
print("No stocks were selected.")

print("-" * 40)
print(f"Total Investment: ${total_investment}")

with open("portfolio_summary.txt", "w", encoding="utf-8") as file:
file.write("STOCK PORTFOLIO SUMMARY\n")
file.write("=" * 30 + "\n")

```
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    file.write(
        f"{stock}: {quantity} shares x ${price} = ${investment}\n"
    )

file.write("-" * 30 + "\n")
file.write(f"Total Investment: ${total_investment}\n")
```

print("\nSummary saved to portfolio_summary.txt")
print("Thank you for using Stock Portfolio Tracker!")
