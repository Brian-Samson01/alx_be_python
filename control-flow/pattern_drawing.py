# pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# While loop to handle rows
while row < size:
    # For loop to print stars in each row
    for _ in range(size):
        print("*", end="")
    
    # Move to the next line after finishing a row
    print()
    
    # Increment the row counter
    row += 1
