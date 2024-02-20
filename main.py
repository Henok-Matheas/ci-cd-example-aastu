def greet(name):
    return f"Hello {name}, Docker is running!!"

def main():
    """Entry point for the application script"""
    name = input("what is your name? ")
    print(greet(name))

if __name__ == "__main__":
    main()