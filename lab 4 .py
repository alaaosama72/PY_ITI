# Email valid

def is_valid_email(email):
    try:
        if '@' not in email or '.' not in email:
            return False

        username, domain = email.split('@')

        domain_parts = domain.split('.')
        if len(domain_parts) < 2:
            return False

        if not username or not domain or not all(domain_parts):
            return False

        return True

    except ValueError:
        return False

    except Exception:
        return False


def get_valid_emails(emails):
    return list(filter(is_valid_email, emails))


def extract_domains(valid_emails):
    return list(map(lambda email: email.split('@')[1], valid_emails))



def main():
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        email = input("Enter your email: ").strip()
        if is_valid_email(email):
            print("Your valid email is:", email)
            break
        else:
            print(" Invalid email. Please try again.")
            attempts += 1

    if attempts == max_attempts:
        raise Exception("❗ You reached 5 attempts. Please contact the company.")

    emails = [
        "alaa@example.com",
        "ali@gmail.com",
        "Osame@yahoo.com",
        "noha@iti.gov",
        "user@domain.uk",
        "invalidemail.com",
        "test@.com",
        "@nodomain.com",
        "user@outlook.com",
        "EWE@SDG.SD"
    ]

    valid_emails = get_valid_emails(emails)
    domains = extract_domains(valid_emails)

   
    print("\n Valid Emails:")
    for email in valid_emails:
        print(" -", email)

    print("\n Domains:")
    for domain in domains:
        print(" -", domain)


if __name__ == "__main__":
    main()
