import random
import string

def password_generate(length):
    if length < 1:
        raise ValueError("Password length must be at least 1")
    characters = string.ascii_letters + string.digits + string.punctuation   
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: ")) 
        password = password_generate(length)
        print(f"Generated password is: {password}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()
