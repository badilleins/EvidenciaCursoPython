def read_int(prompt, min, max):
   while True:
        try:
            user_input = input(prompt)
            value = int(user_input)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Error: the value is not within permitted range ({min_val}..{max_val})")
        except ValueError:
            print("Error: wrong input")


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
    