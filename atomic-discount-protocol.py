# atomic_discount_protocol.py - Shadow Garden Atomic Discount Protocol

print("--- Initiating Shadow Garden Atomic Discount Protocol ---")
print("This module provides tactical price reductions for assets and intel.")
print("---------------------------------------------------------")

def calculate_atomic_discount(price, discount_percent):
    """
    Calculates the final price after applying a tactical discount.
    Applies the discount only if the discount percentage is 20% or higher.
    This function demonstrates:
    - Parameters: 'price' and 'discount_percent'.
    - Conditionals: Checking if discount_percent meets the threshold.
    - Return Value: The calculated final price or original price.
    """
    # Local variable 'final_price' scope is within this function.
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        print(f"\n✅ Discount Protocol Activated! A {discount_percent}% tactical reduction applied. ✅")
        return final_price
    else:
        print(f"\n⚠️ Discount Protocol Denied. Required minimum discount of 20% not met (Current: {discount_percent}%). Original price retained. ⚠️")
        return price

# Main execution block for the Atomic Discount Protocol
if __name__ == "__main__":
    while True:
        print("\n---------------------------------------------------------")
        print("Enter details for the tactical discount calculation.")
        print("Type 'exit' at any prompt to conclude operations.")
        print("---------------------------------------------------------")

        try:
            original_price_input = input("Enter the original price of the item (Target Value): ")
            if original_price_input.lower() == 'exit':
                break
            original_price = float(original_price_input)

            discount_percent_input = input("Enter the discount percentage (Tactical Reduction %): ")
            if discount_percent_input.lower() == 'exit':
                break
            discount_percent = float(discount_percent_input)

            # Call the function to calculate the discount
            final_calculated_price = calculate_atomic_discount(original_price, discount_percent)
            
            # Display the result based on whether a discount was applied
            if final_calculated_price != original_price:
                print(f"Original Price: {original_price:.2f} | Discount Applied: {discount_percent}%")
                print(f"Final Price after Tactical Reduction: {final_calculated_price:.2f} 💰")
            else:
                print(f"Original Price: {original_price:.2f} | No Discount Applied.")
                print(f"Final Price (Original Price): {final_calculated_price:.2f} 💰")
            
            print("\nType 'exit' or press Enter without value to conclude discount operations.")
        except ValueError:
            print("⛔ Invalid input. Please enter numerical values for price and percentage. ⛔")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        # Prompt to continue or exit the loop
        continue_prompt = input("Continue Discount Protocol? (yes/no or enter for yes): ").lower()
        if continue_prompt == 'no' or continue_prompt == 'exit':
            break

    print("\n--- Atomic Discount Protocol Concluded ---")
    print("\nShadow Garden Financial Operations Ceased. Prepare for next command. �")
�
