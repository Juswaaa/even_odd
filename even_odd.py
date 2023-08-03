def extract_even_odd_numbers(input_file, output_even_file, output_odd_file):
    try:
        with open(input_file, 'r') as infile:
            numbers = [int(num) for num in infile.read().split()]

            # Filter even and odd numbers using list comprehensions
            even_numbers = [str(num) for num in numbers if num % 2 == 0]
            odd_numbers = [str(num) for num in numbers if num % 2 != 0]
            
            # Write even numbers to the 'even.txt' file
            with open(output_even_file, 'w') as even_file:
                even_file.write("\n".join(even_numbers))

            # Write odd numbers to the 'odd.txt' file
            with open(output_odd_file, 'w') as odd_file:
                odd_file.write("\n".join(odd_numbers))

            print("Even numbers have been written to 'even.txt'")
            print("Odd numbers have been written to 'odd.txt'")
