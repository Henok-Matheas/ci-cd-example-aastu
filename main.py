def greet(name):
    return f"Hello {name}, Docker is running!!"

def main():
    name = input("what is your name? ")
    print(greet(name))

if __name__ == "__main__":
    main()