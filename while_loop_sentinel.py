total_sum = 0

while True:
    user_input = input("Enter a number (or 'stop' to finish): ")
    
    if user_input.strip().lower() == "stop":  # Proper indentation
        break  # Proper indentation

    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'stop'.")
        break

    print("The total sum is:", total_sum)
