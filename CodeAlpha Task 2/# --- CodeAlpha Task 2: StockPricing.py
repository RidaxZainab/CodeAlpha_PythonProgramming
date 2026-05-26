stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "NVDA": 450,
    "MSFT": 420
}

print("=== WELCOME TO CODEALPHA STOCK TRACKER ===")
print("Available Stocks:", list(stock_prices.keys()))
print("-----------------------------------------")

user_stock = input("Enter the stock name : ").upper().strip()

if user_stock in stock_prices:
    shares_input = input(f"How many shares of {user_stock} do you own? ")
    
    if shares_input.isdigit():
        shares = int(shares_input)
        current_rate = stock_prices[user_stock]
        total_value = shares * current_rate
        
        print("\n--- PORTFOLIO SUMMARY ---")
        print(f"Stock Name: {user_stock}")
        print(f"Price per Share: ${current_rate}")
        print(f"Total Shares: {shares}")
        print(f"Total Investment Value: ${total_value}")
        print("-------------------------")
        
        my_file = open("my_portfolio.txt", "w")
        my_file.write("=== My Stock Portfolio ===\n")
        my_file.write(f"Stock: {user_stock}\n")
        my_file.write(f"Quantity: {shares}\n")
        my_file.write(f"Total Investment Value: ${total_value}\n")
        my_file.close()
        
        print("Data successfully saved to 'my_portfolio.txt'!")
    else:
        print("Invalid input! Please enter a valid number for shares.")
else:
    print("Error: This stock is not available in our system.")