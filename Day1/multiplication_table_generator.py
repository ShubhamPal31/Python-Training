def main():
    num = int(input("Enter a number: "))
    end = int(input("Enter the last number you want in the multiplication table: "))
    print(f"The multiplication table of {num} is:")
    for i in range(1, end+1):
        print(f"{num} * {i} = {num*i}")

if __name__=="__main__":
    main()