# Write a program that counts up the number of vowels [a, e, i, o, u]contained in the string.

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

#  Write a program that prints the locations of "i" character in any string you added.

def find_char_positions(text, target_char):
    positions = []
    for index, char in enumerate(text):
        if char == target_char:
            positions.append(index)
    return positions

# Write a program that generate a multiplication table from 1 to the number passed.


def generate_table(n):
    result = []
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            result.append(f"{i}x{j}={i*j}")
    return result


# Mario Pyramid

def show_pyramid(max_stars):
    for i in range(max_stars):
        print(" " * (max_stars - i - 1) + "*" * (i + 1))


if __name__ == "__main__":
    print("Count Vowels")
    input_string = input("Enter a string: ")
    print(f"Number of vowels: {count_vowels(input_string)}")

    print("-" * 30)

    print("Multiplication Table")
    n = int(input("Enter a number: "))
    print(mult_table(n))

    print("-" * 30)

    print("Find positions of 'i'")
    input_string = input("Enter a string: ")
    print(f"Positions of 'i': {find_i(input_string)}")

    print("-" * 30)

    print("Show Pyramid")
    max_stars = int(input("Enter the number of pyramid rows: "))
    show_pyramid(max_stars)
