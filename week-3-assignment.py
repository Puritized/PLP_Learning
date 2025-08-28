def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Only applies discount if discount_percent is 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Main Program
print("\n--- Discount Calculator ---")
# Get user input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(original_price, discount)

# Print result
if discount >= 20:
    print(f"The final price after {discount}% discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The price remains: {final_price:.2f}")
