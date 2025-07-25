#Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output.
def sort_list():
    l = []
    for i in range(5):
        next_elm = input("Enter a number:")
        l.append(next_elm)

    print("Sorted list ascending:", sorted(l))
    print("Sorted list descending:", sorted(l, reverse=True))

if __name__ == "__main__":
    sort_list()


# product_table

def get_max():
    max_tries = 5
    while max_tries:
        max_num = input("Enter a number: ")
        if max_num.isdigit():
            max_num = int(max_num)
            break
        max_tries -= 1
    return max_num

def mult_table(max_num):
    product_table = []
    for i in range(1, max_num + 1):
        product_table.append([])
        for j in range(1, i + 1):
            product_table[i - 1].append(j * i)

    return product_table

def main():
    max_num = get_max()
    print(mult_table(max_num))

if __name__ == "__main__":
    main()

#Ask the user for his name then confirm that he has entered his name(not an empty string/integers). 
# then proceed to ask him for his email and print all this data(Bonus) check if it is a valid email or not

def is_valid_name(name):
    return name.strip() != "" and not name.strip().isdigit()


def is_valid_email(email):
   
    if "@" in email:
        local_part, _, domain = email.partition("@")
        return "." in domain and local_part != "" and domain != ""
    return False


def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if is_valid_name(name):
            return name
        print(" Invalid name! Please enter a non-empty name that is not a number.")


def get_valid_email():
    while True:
        email = input("Enter your email: ").strip()
        if is_valid_email(email):
            return email
        print(" Invalid email! Please enter a valid email address (example@example.com).")


def main():
    print(" User Information Form")

    name = get_valid_name()
    email = get_valid_email()

    print("\n Data Collected Successfully!")
    print(f"Name : {name}")
    print(f"Email: {email}")


if __name__ == "__main__":
    main()
