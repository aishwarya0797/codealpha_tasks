def get_stock_prices():
    """
    Hardcoded stock prices dictionary.
    We can change values as needed.
    """
    return {
        "APPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "AMZN": 130,
        "MSFT": 320
    }


def display_available_stocks(stock_prices):
    """Show available stocks and their prices."""
    print("\nAvailable Stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")


def get_user_portfolio(stock_prices):
    """
    Take stock name and quantity input from user.
    Returns a dictionary: {stock_name: quantity}
    """
    portfolio = {}

    while True:
        stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()

        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print("Stock not found in price list. Please try again.")
            continue

        qty_input = input(f"Enter quantity for {stock_name}: ").strip()

        if not qty_input.isdigit():
            print("Quantity must be a positive whole number.")
            continue

        quantity = int(qty_input)

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        # If same stock entered multiple times, add quantity
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    return portfolio


def calculate_total_investment(portfolio, stock_prices):
    """
    Calculate total investment and line-by-line breakdown.
    Returns (total_value, breakdown_list)
    """
    total_value = 0
    breakdown = []

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        investment = price * qty
        total_value += investment
        breakdown.append((stock, qty, price, investment))

    return total_value, breakdown


def save_to_file(filename, breakdown, total_value):
    """
    Save result to .txt or .csv based on file extension.
    """
    if filename.endswith(".txt"):
        with open(filename, "w") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("-" * 40 + "\n")
            for stock, qty, price, investment in breakdown:
                file.write(f"{stock} | Qty: {qty} | Price: ${price} | Value: ${investment}\n")
            file.write("-" * 40 + "\n")
            file.write(f"Total Investment Value: ${total_value}\n")
        print(f"Saved successfully to {filename}")

    elif filename.endswith(".csv"):
        with open(filename, "w") as file:
            file.write("Stock,Quantity,Price,Investment\n")
            for stock, qty, price, investment in breakdown:
                file.write(f"{stock},{qty},{price},{investment}\n")
            file.write(f"TOTAL,,,{total_value}\n")
        print(f"Saved successfully to {filename}")

    else:
        print("Unsupported file format. Use .txt or .csv")


def main():
    stock_prices = get_stock_prices()

    print("=== Stock Portfolio Tracker ===")
    display_available_stocks(stock_prices)

    portfolio = get_user_portfolio(stock_prices)

    if not portfolio:
        print("\nNo stocks entered. Exiting program.")
        return

    total_value, breakdown = calculate_total_investment(portfolio, stock_prices)

    print("\nPortfolio Summary:")
    for stock, qty, price, investment in breakdown:
        print(f"{stock} -> Qty: {qty}, Price: ${price}, Value: ${investment}")

    print(f"\nTotal Investment Value: ${total_value}")

    save_choice = input("\nDo you want to save result to file? (yes/no): ").lower().strip()
    if save_choice == "yes":
        filename = input("Enter filename (example: report.txt or report.csv): ").strip()
        save_to_file(filename, breakdown, total_value)
    else:
        print("Result not saved.")


if __name__ == "__main__":
    main()