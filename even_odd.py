def extract_even_odd_numbers(input_file, output_even_file, output_odd_file):
    try:
        with open(input_file, 'r') as infile:
            numbers = [int(num) for num in infile.read().split()]

            # Filter even and odd numbers using list comprehensions
            even_numbers = [str(num) for num in numbers if num % 2 == 0]
            odd_numbers = [str(num) for num in numbers if num % 2 != 0]
