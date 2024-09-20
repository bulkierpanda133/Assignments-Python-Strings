def input_length_validator():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    if len(first_name) < 2:
        print("Error: First name must be at least 2 characters long.")
    elif len(last_name) < 2:
        print("Error: Last name must be at least 2 characters long.")
    else:
        print(f"Welcome, {first_name} {last_name}!")

# Run the input validator
input_length_validator()
