import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(random.choice(characters) for i in range(length))
    
    return pwd

def main():
    while True:
        try:

            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Please enter a positive integer for the password length.")
            else:
                pwd = generate_password(length)
                print(f"Generated Password: {pwd}")
            again = input("Do you want to generate another password? (Yes/No): ").strip().lower()
            if again != 'Yes':
                print("Thank you for using the Password Generator!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
