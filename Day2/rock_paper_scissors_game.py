import random
def rock_paper_scissors():
    print("WELCOME TO THE ROCK PAPER SCISSORS GAME")
    user = 0
    computer = 0
    choice_list = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choice_list)
    choice = input("Choose rock, paper or scissors (choose quit to stop the game): ")

    while choice!='quit':
        if computer_choice==choice:
            print("Its a Tie!!")
        elif choice=='rock':
            if computer_choice=='paper':
                computer += 1
            else:
                user += 1
        elif choice=='paper':
            if computer_choice=='scissors':
                computer += 1
            else:
                user += 1
        elif choice=='scissors':
            if computer_choice=='rock':
                computer += 1
            else:
                user += 1
        else:
            print("Invalid input!")
        print("Current Score:")
        print(f"You = {user}    |   computer = {computer}")
        print("---------------------------------------------------")
        computer_choice = random.choice(choice_list)
        choice = input("Choose rock, paper or scissors (choose quit to stop the game): ") 
    print("Thanks for playing!")
        

if __name__=="__main__":
    rock_paper_scissors()