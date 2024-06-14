def convert_to_integer(string):
    try:
        number =int(string)
        print("Integer value:",number)
    except ValueError:
        print("Error: Invalid integer value!")

def main():
    string=input("Enter a string")
    convert_to_integer(string)

if __name__ == "__main__":
    main()

