# atomic_calculator.py - Shadow Garden Tactical Calculator

print("🌟 Welcome, Operative, to the Shadow Garden Tactical Calculator! 🌟")
print("This tool is for performing precise atomic computations.")
print("---------------------------------------------------------------")

def perform_atomic_operation(num1, num2, operation):
    """
    Performs a specified mathematical operation on two numbers.
    This function demonstrates parameters and a return value.
    It also incorporates conditional logic.
    """
    # Part 1: Variable declarations (local to this function)
    result = None
    operation_name = ""

    # Part 1: Conditionals based on the chosen operation
    if operation == '+':
        result = num1 + num2
        operation_name = "Atomic Addition"
    elif operation == '-':
        result = num1 - num2
        operation_name = "Shadow Subtraction"
    elif operation == '*':
        result = num1 * num2
        operation_name = "Multi-Dimensional Multiplication"
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            operation_name = "Dimensional Division"
        else:
            # Handle division by zero - crucial for tactical integrity!
            print("\n🚨 ERROR: Cannot perform Dimensional Division by zero! Tactical failure averted. 🚨")
            return None, None # Return None for both result and operation name
    else:
        # Handle invalid operation - the Foundation does not tolerate ambiguity!
        print(f"\n🚫 ERROR: Invalid operation '{operation}'. Supported operations are +, -, *, /. �")
        return None, None # Return None for both result and operation name

    # Part 2: Return useful values
    return result, operation_name

# Main program loop to allow multiple calculations (Part 3: Loop Example)
while True:
    print("\n---------------------------------------------------------------")
    print("Enter your numerical inputs and the operation symbol.")
    print("Supported operations: + (Add), - (Subtract), * (Multiply), / (Divide)")
    print("Type 'exit' to conclude the tactical session.")
    print("---------------------------------------------------------------")

    # Get first number from the user
    try:
        input1 = input("Enter the first numerical value (Operative #1): ")
        if input1.lower() == 'exit':
            break # Exit loop if user types 'exit'
        num_one = float(input1) # Convert input to a floating-point number
    except ValueError:
        print("⛔ Invalid input for Operative #1. Please enter a number. ⛔")
        continue # Skip to the next iteration of the loop

    # Get second number from the user
    try:
        input2 = input("Enter the second numerical value (Operative #2): ")
        if input2.lower() == 'exit':
            break # Exit loop if user types 'exit'
        num_two = float(input2) # Convert input to a floating-point number
    except ValueError:
        print("⛔ Invalid input for Operative #2. Please enter a number. ⛔")
        continue # Skip to the next iteration of the loop

    # Get the operation from the user
    op = input("Enter the atomic operation (+, -, *, /): ")
    if op.lower() == 'exit':
        break # Exit loop if user types 'exit'

    # Perform the calculation using our atomic function
    final_result, chosen_operation_name = perform_atomic_operation(num_one, num_two, op)

    # Display the result (Part 4: Simple output DOM interaction equivalent)
    if final_result is not None:
        print(f"\n✨ Initiating {chosen_operation_name} Sequence... ✨")
        # Example: 10 + 5 = 15 --> 10 (Operator) 5 (Operative) = (Result)
        print(f"Calculation: {num_one} {op} {num_two} = {final_result}")
        print(f"📡 Result Transmitted: {final_result} 📡")

print("\nSession concluded. The shadows await your next command. 🌙")
�
