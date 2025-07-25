#You are given a list of email addresses in the format username@domain.Your task is 
# to use the map() function along with a lambda expression to extract only the domain part from each email address.

def extract_domains(email_list):
    return list(map(lambda email: email.split('@')[1], email_list))

def main():
    emails = [
        "alaa@gmail.com",
        "mohamed@yahoo.com",
        "fatma@iti.gov.eg",
        "omar@outlook.com"
    ]

    domains = extract_domains(emails)

    print(" Email Domains:")
    for domain in domains:
        print(domain)


if __name__ == "__main__":
    main()


#You are given a list of email addresses, some of which are invalid.Your task is 
# to use the filter() function to return only the valid email addresses

def is_valid_email(email):
    if "@" in email:
        local, _, domain = email.partition("@")
        return local != "" and domain != "" and "." in domain
    return False


def filter_valid_emails(email_list):
    return list(filter(is_valid_email, email_list))


def main():
    emails = [
        "alaa@gmail.com",
        "mohamedyahoo.com",      
        "fatma@iti",            
        "omar@outlook.com",    
        "@nope.com",          
        "sara@.com",            
        "hassan@gmail.com"       
    ]

    valid_emails = filter_valid_emails(emails)

    print(" Valid Emails:")
    for email in valid_emails:
        print(email)


if __name__ == "__main__":
    main()
