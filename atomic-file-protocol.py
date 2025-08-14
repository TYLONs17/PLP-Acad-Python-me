# atomic_file_protocol.py - Shadow Garden Data Infiltration & Transformation Protocol

print("--- Initiating Shadow Garden Data Infiltration & Transformation Protocol ---")
print("This module ensures secure handling and modification of classified intel files.")
print("----------------------------------------------------------------------------")

# Global variables for atomic substitution (Part 2: Scope - Global)
ATOMIC_SUBSTITUTIONS = {
    'shadow': '🌌SHADOW-PROTOCOL🌌',
    'garden': '🌿GARDEN-MATRIX🌿',
    'atomic': '✨ATOMIC-BURST✨',
    'master': '👑MASTER-INTELLIGENCE�',
    'power': '⚡INFINITE-POWER⚡',
    'intel': '📡SECURE-INTEL📡'
}

def transform_atomic_intel(line_of_data):
    """
    Transforms a single line of data using atomic substitutions.
    This function demonstrates:
    - Parameters: 'line_of_data'
    - Local Scope: 'modified_line', 'word'
    - Loop: Iterates through defined substitutions.
    - Return Value: The modified line.
    """
    modified_line = line_of_data.strip() # Start with clean line (Part 2: Local Scope)
    
    # Part 3: Loop Example (Implicit loop over dictionary items)
    for original, atomic_version in ATOMIC_SUBSTITUTIONS.items():
        # Case-insensitive replacement (Part 1: Conditional logic within replacement)
        modified_line = modified_line.replace(original, atomic_version)
        modified_line = modified_line.replace(original.capitalize(), atomic_version)
        modified_line = modified_line.replace(original.upper(), atomic_version)
    
    return modified_line + " ⚔️\n" # Add a tactical mark and newline

def execute_infiltration_protocol():
    """
    Manages the reading of an input file, transformation of its content,
    and writing to an output file, with robust error handling.
    This function demonstrates:
    - Error Handling (try-except-finally blocks)
    - File Read/Write Operations
    - Looping through file content
    - Function reuse (calling transform_atomic_intel)
    """
    input_filename = ""
    output_filename = ""
    input_file = None
    output_file = None

    try:
        # Ask the user for the input filename
        input_filename = input("Enter the path to the original intel file (input_file.txt): ")
        if not input_filename:
            print("Operation aborted: Input filename cannot be empty.")
            return

        # Open the input file for reading (Part 4: File Read)
        # Error Handling Lab: Handle if the file doesn't exist or can't be read
        input_file = open(input_filename, 'r', encoding='utf-8')
        print(f"📡 Accessing intel from '{input_filename}'... SUCCESS. 📡")

        # Ask the user for the output filename
        output_filename = input("Enter the path for the transformed intel file (output_file.txt): ")
        if not output_filename:
            print("Operation aborted: Output filename cannot be empty.")
            return

        # Open the output file for writing (Part 4: File Write)
        output_file = open(output_filename, 'w', encoding='utf-8')
        print(f"✍️ Preparing secure channel for '{output_filename}'... READY. ✍️")

        line_count = 0
        # Read the file line by line and write a modified version to a new file (Part 4: File Read & Write)
        # Part 3: Loop Example (for loop iterating over file lines)
        for line in input_file:
            transformed_line = transform_atomic_intel(line) # Reuse our transformation function
            output_file.write(transformed_line)
            line_count += 1
        
        print(f"\n✅ Data Transformation Complete! {line_count} lines of intel processed. ✅")
        print(f"Transformed intel saved to '{output_filename}'.")

    # Error Handling Lab: Catch specific file-related exceptions
    except FileNotFoundError:
        print(f"\n🚨 ERROR: Intel file '{input_filename}' not found. Verify path and try again. 🚨")
    except PermissionError:
        print(f"\n🚨 ERROR: Insufficient permissions to access or write file. Check file permissions. 🚨")
    except IOError as e:
        print(f"\n🚨 ERROR: An I/O error occurred during file operation: {e}. 🚨")
    except Exception as e: # Catch any other unexpected errors
        print(f"\n🚨 CRITICAL ERROR: An unexpected system anomaly occurred: {e}. Protocol Halted. 🚨")
    finally:
        # Ensure files are closed, regardless of success or error (Part 4: Robustness)
        if input_file:
            input_file.close()
            print(f"🔒 Input intel file '{input_filename}' securely closed. 🔒")
        if output_file:
            output_file.close()
            print(f"🔒 Output intel file '{output_filename}' securely closed. 🔒")

# Main execution entry point
if __name__ == "__main__":
    execute_infiltration_protocol()
    print("\n--- Protocol Concluded. The shadows watch over your data. 🌙 ---")

�
