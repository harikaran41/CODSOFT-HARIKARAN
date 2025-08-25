import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_letters  
    elif complexity == 2:
        characters = string.ascii_letters + string.digits  
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation  
    else:
        print("Invalid complexity choice! Please enter 1, 2, or 3.")
        return None

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("=== PASSWORD GENERATOR ===")
    
    try:
        length = int(input("Enter desired password length: "))
        print("Choose complexity level:")
        print("1 - Letters only")
        print("2 - Letters and numbers")
        print("3 - Letters, numbers, and special characters")
        complexity = int(input("Enter complexity (1/2/3): "))

        password = generate_password(length, complexity)
        if password:
            print("\nGenerated Password:", password)

    except ValueError:
        print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()


    
 