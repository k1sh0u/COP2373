
import re

def main():

    zip_code = zip_code_test()
    phone_number = phone_number_test()
    ssn = ssn_test()
    statement(zip_code, phone_number, ssn)


def zip_code_test():


    while True:

        raw_zip = input("Enter your zip code: ")
        clean_string = re.sub(r"[^\d]", "", raw_zip)
        if re.match(r"^\d{5}$", clean_string):
            return clean_string
        else:
            print("Please enter a valid zip code")


def phone_number_test():

    while True:

        raw_number = input("Enter your phone number: ")
        clean_string = re.sub(r"[^\d]", "", raw_number)
        if re.match(r"^\d{10}$", clean_string):
            clean_string = f"({clean_string[0:3]}) {clean_string[3:6]}-{clean_string[6:]}"

            return clean_string
        else:
            print("Please enter a valid phone number.")




def ssn_test():

    while True:

        raw_ssn = input("Enter your SSN: ")
        clean_string = re.sub(r"[^\d]", "", raw_ssn)
        if re.match(r"^\d{9}$", clean_string):
            clean_string = f"{clean_string[0:3]}-{clean_string[3:5]}-{clean_string[5:]}"

            return clean_string
        else:
            print("Please enter a valid ssn.")

def statement(zip, phone, ssn):
    print(f"\nDoes this look right?"
          f"\nZip code: {zip}"
          f"\nPhone number: {phone}"
          f"\nSSN: {ssn}")

if __name__ == '__main__':
    main()





