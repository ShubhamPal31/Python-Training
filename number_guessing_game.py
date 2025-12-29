import random
def main():
    random_number = random.randrange(1, 101)
    print("-------------GUESSING GAME-----------")
    num = int(input("Guess the number from 1 to 100: "))

    while num!=random_number:
        diff = num-random_number
        if num<1:
            num = int(input("You went down the lower limit, guess from 1 to 100 please: "))
        elif num>100:
            num = int(input("You went out of upper limit, guess from 1 to 100 please: "))
        elif diff<0:
            num = int(input("You guessed lower, please try a higher value: "))
        else:
            num = int(input("You guessed higher, please try a lower value: "))

    print("Yayy!! You guessed the number, thanks for playing")

if __name__=="__main__":
    main()