# atomic_list_operations.py - Shadow Garden Atomic Data Sequence Module

print("--- Initiating Shadow Garden Atomic Data Sequence ---")
print("This module performs critical array manipulations for intelligence processing.")
print("------------------------------------------------------")

def execute_atomic_list_sequence():
    """
    Executes a sequence of list manipulations as a core atomic data operation.
    This function demonstrates list creation, appending, inserting, extending,
    removing, sorting, and finding elements within a list.
    """
    print("\n--- Atomic Data Sequence Protocol ---")
    # Create an empty list called my_list.
    my_list = []
    print(f"1. Initializing Atomic Data Array: {my_list}")

    # Append the following elements to my_list: 10, 20, 30, 40.
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    print(f"2. Appending Core Data Elements: {my_list}")

    # Insert the value 15 at the second position (index 1) in the list.
    my_list.insert(1, 15)
    print(f"3. Inserting Priority Intel (15 at position 2): {my_list}")

    # Extend my_list with another list: [50, 60, 70].
    my_list.extend([50, 60, 70])
    print(f"4. Extending Array with Auxiliary Data: {my_list}")

    # Remove the last element from my_list.
    removed_element = my_list.pop()
    print(f"5. Removing Last Redundant Datum ({removed_element}): {my_list}")

    # Sort my_list in ascending order.
    my_list.sort()
    print(f"6. Sorting Array for Optimal Analysis: {my_list}")

    # Find and print the index of the value 30 in my_list.
    try:
        index_of_30 = my_list.index(30)
        print(f"7. Locating Critical Datum (30): Found at Tactical Index {index_of_30}")
    except ValueError:
        print("7. Critical Datum (30) not found. Anomaly detected!")
    print("--- Atomic Data Sequence Protocol Complete ---")

# Execute the list sequence when this script is run directly
if __name__ == "__main__":
    execute_atomic_list_sequence()
    print("\nShadow Garden Data Operations Concluded. Prepare for next command. 🌙")
